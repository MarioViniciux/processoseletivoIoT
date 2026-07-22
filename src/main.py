"""
Sistema de Monitoramento Termal e de Acesso.

Este script monitora o estado de uma porta (aberta/fechada) via um sensor mecânico/magnético (botão)
e a variação de temperatura de um ambiente utilizando o sensor MPU6050 via protocolo I2C. 
O sistema emite alertas caso a porta fique aberta por um tempo excessivo ou ocorra uma 
degradação térmica abrupta, e conta com uma lógica de estabilização para retornar ao estado seguro.
"""

from machine import Pin, I2C
import time
 
# ==========================================
# Configuração de Hardware
# ==========================================

# Configuração do barramento I2C para comunicação com o sensor
i2c = I2C(0, scl=Pin(19), sda=Pin(18), freq=400000)

# Endereços e registradores do MPU6050
MPU_ADDR = 0x68
PWR_MGMT_1 = 0x6B
TEMP_OUT_H = 0x41
 
# Configuração do pino do sensor da porta (com resistor pull-up interno)
btn = Pin(5, Pin.IN, Pin.PULL_UP)
 
# ==========================================
# Parâmetros do Sistema
# ==========================================

VARIATION_LIMIT_Y = 3.0     # graus C - variacao abrupta maxima tolerada
TIME_LIMIT_X = 5000         # ms - tempo maximo com a porta aberta
STABILIZATION_MS = 600      # ms - tempo que as condicoes seguras devem se manter antes de normalizar
LOOP_INTERVAL_MS = 100      # intervalo do loop infinito
 
def mpu_init():
    """
    Inicializa e acorda o MPU6050.
    
    Por padrão, o MPU6050 inicia no modo "sleep". Esta função escreve no 
    registrador de gerenciamento de energia para desativar o modo de economia.
    """
    i2c.writeto_mem(MPU_ADDR, PWR_MGMT_1, b'\x00')
 
def read_temperature():
    """
    Lê o registrador de temperatura do MPU6050 e converte o valor bruto para graus Celsius.
    
    Returns:
        float: Temperatura lida pelo sensor em graus Celsius.
    """
    data = i2c.readfrom_mem(MPU_ADDR, TEMP_OUT_H, 2)
    raw = (data[0] << 8) | data[1]

    # Tratamento para valores com sinal de 16 bits (complemento de dois)
    if raw > 32767:
        raw -= 65536

    # Fórmula de conversão do datasheet do MPU6050
    return (raw / 340.0) + 36.53 
 
def is_door_closed():
    """
    Verifica o estado atual da porta baseando-se no nível lógico do pino.
    
    Como o pino usa PULL_UP interno, o estado pressionado/fechado leva 
    o nível lógico para BAIXO (0).
    
    Returns:
        bool: True se a porta estiver fechada, False caso contrário.
    """
    return btn.value() == 0
 
def new_state():
    """
    Cria e inicializa o dicionário de estado do sistema.
    
    Returns:
        dict: Dicionário contendo as variáveis de controle de tempo, status dos alarmes 
              e a temperatura de referência.
    """
    return {
        "reference_temperature": None,      # (float) Temperatura base para cálculo de variação
        "open_since": None,                 # (int) Timestamp de quando a porta foi aberta
        "door_alarm_active": False,         # (bool) Flag do alarme de porta aberta
        "active_thermal_alarm": False,      # (bool) Flag do alarme de variação térmica
        "normalized_since": None,           # (int) Timestamp de quando o ambiente voltou ao normal
    }
 
def check_open_door(state, closed_door):
    """
    Monitora o tempo em que a porta permanece aberta e ativa o alarme se ultrapassar o limite.
    
    Args:
        state (dict): Dicionário contendo o estado atual do sistema.
        closed_door (bool): Estado físico da porta no instante atual.
    """
    if not closed_door:
        # Marca o início do evento de porta aberta
        if state["open_since"] is None:
            state["open_since"] = time.ticks_ms()

        # Se o alarme ainda não foi ativado, verifica se o tempo limite foi atingido
        elif not state["door_alarm_active"]:
            elapsed = time.ticks_diff(time.ticks_ms(), state["open_since"])
            if elapsed >= TIME_LIMIT_X:
                state["door_alarm_active"] = True
                print("ALERTA: Porta aberta por muito tempo!")
    else:
        # Reseta o contador se a porta for fechada
        state["open_since"] = None
 
def check_temperature(state, closed_door, temp_atual):
    """
    Monitora a variação térmica para detectar degradações abruptas no ambiente.
    
    A temperatura de referência só é atualizada se a porta estiver fechada 
    e a variação estiver dentro dos limites seguros. 
    
    Args:
        state (dict): Dicionário contendo o estado atual do sistema.
        closed_door (bool): Estado físico da porta no instante atual.
        temp_atual (float): Temperatura atual lida pelo sensor.
        
    Returns:
        float: A diferença (delta_t) entre a temperatura atual e a temperatura de referência.
    """

    # Define a temperatura de referência inicial, caso ainda não exista
    if state["reference_temperature"] is None and closed_door:
        state["reference_temperature"] = temp_atual
 
    reference = state["reference_temperature"]
    delta_t = (temp_atual - reference) if reference is not None else 0.0
 
    # Dispara o alarme em caso de salto térmico acima do limite
    if delta_t >= VARIATION_LIMIT_Y:
        if not state["active_thermal_alarm"]:
            state["active_thermal_alarm"] = True
            print("ALERTA: Degradacao termica detectada!")

    # Caso não haja alarme e a porta esteja fechada, a variação é lenta/segura e a referência é atualizada
    elif closed_door and not state["active_thermal_alarm"]:
        state["reference_temperature"] = temp_atual
 
    return delta_t
 
def check_normalization(state, closed_door, temp_atual, delta_t):
    """
    Verifica se as condições do ambiente se mantiveram seguras por tempo suficiente
    para desligar os alarmes e normalizar o sistema.
    
    Condições seguras: Porta fechada e variação térmica abaixo do limite aceitável.
    
    Args:
        state (dict): Dicionário contendo o estado atual do sistema.
        closed_door (bool): Estado físico da porta no instante atual.
        temp_atual (float): Temperatura atual lida pelo sensor.
        delta_t (float): Variação térmica calculada pela função check_temperature.
    """
    safe_conditions = closed_door and delta_t < VARIATION_LIMIT_Y
    alarm_active = state["door_alarm_active"] or state["active_thermal_alarm"]
 
    if alarm_active and safe_conditions:
        # Inicia a contagem de tempo de normalização
        if state["normalized_since"] is None:
            state["normalized_since"] = time.ticks_ms()

        # Desliga alarmes se o tempo de estabilização for atingido
        elif time.ticks_diff(time.ticks_ms(), state["normalized_since"]) >= STABILIZATION_MS:
            state["door_alarm_active"] = False
            state["active_thermal_alarm"] = False
            state["reference_temperature"] = temp_atual
            state["normalized_since"] = None
            print("Status: Sistema Normalizado.")

    else:
        # Se houver instabilidade (porta abre ou delta_t sobe) antes do tempo, zera o contador
        state["normalized_since"] = None
 
# ==========================================
# Inicialização do Sistema
# ==========================================

mpu_init()
state = new_state()
 
print("Sistema de Monitoramento Inicializado")
 
# ==========================================
# Loop Principal
# ==========================================

while True:
    # 1. Coleta de Dados
    closed_door = is_door_closed()
    temp_current = read_temperature()
 
    # 2. Análise e Processamento
    check_open_door(state, closed_door)
    delta_t = check_temperature(state, closed_door, temp_current)
    check_normalization(state, closed_door, temp_current, delta_t)
 
    # 3. Intervalo de segurança
    time.sleep_ms(LOOP_INTERVAL_MS)