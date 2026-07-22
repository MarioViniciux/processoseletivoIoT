# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo:** Mário Vinícius Campinas Souza
- **GitHub:** <a href="https://github.com/MarioViniciux" target="_blank">MarioViniciux</a>

---

## Visão Geral da Solução

O projeto tem como objetivo criar uma solução embarcada para controle de qualidade e auditoria em ambientes sensíveis, como áreas refrigeradas e estufas, prevenindo a degradação de insumos e o sobreaquecimento de componentes. Para isso, o sistema simulado monitora continuamente o tempo de abertura de uma porta e a temperatura do ambiente. Ele calcula variações térmicas abruptas e aciona alertas automáticos via comunicação Serial caso a porta permaneça aberta além do limite permitido ou ocorra uma elevação brusca de temperatura, informando também o momento em que o sistema retorna às condições seguras e se estabiliza.
A interação do usuário com o sistema ocorre diretamente no simulador, onde é possível acionar o botão físico para simular a abertura e o fechamento da porta, além de ajustar manualmente os valores de temperatura lidos pelo sensor MPU6050. O acompanhamento de todas as ações, disparos de alarmes e da normalização do ambiente é feito de forma passiva através da leitura das mensagens de log impressas no terminal da interface Serial.

---

## Arquitetura do Sistema Embarcado

#### Fluxo principal do programa
- **Inicialização:** o microcontrolador configura os pinos, "acorda" o sensor MPU6050 (desativando o modo sleep via I2C), cria a estrutura inicial de estados e imprime a mensagem obrigatória "Sistema de Monitoramento Inicializado".  
- **Loop infinito:** a cada iteração, o programa segue uma rotina sequencial:Coleta de Dados: Lê o estado atual do botão e a temperatura instantânea do registrador do MPU6050.  
- **Análise:** submete os dados às funções lógicas (check_open_door, check_temperature e check_normalization) para validar as regras de negócio.  
- **Descanso:** pausa o processamento por 100 milissegundos (INTERVALO_LOOP_MS) antes de iniciar o próximo ciclo.

#### Estrutura de estados e temporizações
- **Gerenciamento de estado:** o sistema não utiliza funções de bloqueio como grandes time.sleep(). Em vez disso, ele mantém um dicionário (criado pela função new_state()) que atua como uma máquina de estados simples. Este dicionário guarda as flags dos alarmes (alarme_porta_ativo, alarme_termico_ativo), a temperatura_referencia e os carimbos de tempo dos eventos.  
- **Controle não-bloqueante:** o cálculo do tempo de porta aberta (limite de 5000 ms) e o tempo de estabilização térmica (limite de 600 ms) são feitos utilizando as funções time.ticks_ms() e time.ticks_diff(). Isso calcula a diferença entre o momento atual e o instante em que o evento começou, permitindo que as outras verificações continuem rodando em paralelo.

#### Interação entre os componentes
- **Botão &#8594; ESP32:** o botão opera como um fim de curso configurado com um resistor interno de pull-up. Quando está pressionado (nível lógico 0), o ESP32 entende que a porta está fechada; ao ser solto (nível lógico 1), o ESP32 detecta a abertura.  
- **MPU6050 &#8596; ESP32:** a comunicação ocorre via protocolo I2C. O ESP32 requisita dados dos registradores específicos de temperatura do MPU6050, processa o valor bruto (lidando com complemento de dois) e aplica a fórmula matemática para obter o valor em graus Celsius.  
- **ESP32 &#8594; Serial Monitor:** ao cruzar os dados dos sensores e detectar que os limiares configurados (variação &#916;T &#8805; 3.0&#8451; ou tempo de porta aberta excedido) foram ultrapassados, o ESP32 atua disparando logs de texto específicos via comunicação UART (Serial), que servem tanto para o usuário quanto para a leitura da automação de testes (CI).

---

## Componentes Utilizados na Simulação

1. **Placa microcontroladora (ESP32 DevKit C v4):** identificada no diagrama pelo ID esp, é o cérebro do sistema embarcado. Responsável por executar o firmware (main.py), coletar os dados dos sensores, processar as lógicas de temporização e de variação térmica, além de gerenciar o envio das mensagens de status pela interface Serial. 

2. **Sensor inercial (MPU6050):** identificado no diagrama pelo ID imu1, atua especificamente como o sensor de temperatura do ambiente monitorado. Comunica-se com o ESP32 via protocolo I2C para fornecer as leituras térmicas utilizadas no cálculo da variação de temperatura (&#916;T).

3. **Botão físico (Pushbutton):** identificado no diagrama pelo ID btn1, atua como um sensor de fim de curso para simular o estado da porta do ambiente (geladeira, estufa, etc.). Ele monitora a integridade física do isolamento: o estado pressionado sinaliza porta fechada, enquanto o estado solto sinaliza porta aberta.

4. **Monitor serial (Interface UART):** presente nas conexões lógicas de transmissão e recepção (TX/RX) do diagrama, serve como interface de comunicação de saída. É por meio dela que o ESP32 transmite logs de inicialização, alertas de exposição prolongada ou degradação térmica, permitindo a leitura tanto pelo usuário quanto pela esteira de testes automatizados (CI).
---

## Decisões Técnicas Relevantes

- **Organização modular do código e funções:** o código no arquivo main.py foi estruturado de maneira modular, separando as lógicas de negócio em funções específicas de leitura (read_temperature, is_door_closed) e de processamento (check_open_door, check_temperature, check_normalization). Essa decisão mantém o laço principal de execução (while True) limpo e de fácil interpretação.
- **Uso de constantes parametrizadas:** as regras que definem os limiares de acionamento de alarme foram isoladas em constantes globais no início do script, como LIMITE_TEMPO_X (5000 ms) e LIMITE_VARIACAO_Y (3.0&#8451;). Isso permite que os parâmetros do sistema sejam ajustados rapidamente em um único local, sem a necessidade de buscar valores fixos espalhados pelas funções lógicas.
- **Gerenciamento de estado baseado em dicionário:** o rastreamento contínuo das condições do sistema foi centralizado em uma estrutura de dados de dicionário (gerada pela função new_state()). Em vez de criar múltiplas variáveis globais independentes, esse dicionário consolida informações críticas, como a temperatura de referência, as flags de ativação dos alarmes e os carimbos de tempo (timestamps) de abertura e de estabilização.  
- **Estratégia de temporização não-bloqueante:** como o firmware deve responder estritamente aos estímulos para validação na esteira de testes (CI) do Wokwi, evitou-se o uso de comandos que parassem a execução, como funções bloqueantes longas. A lógica de controle de tempo foi construída com as funções time.ticks_ms() e time.ticks_diff(), que calculam continuamente a diferença de tempo de forma concorrente às leituras dos sensores no laço principal.

---

## Resultados Obtidos

- **O que funciona corretamente:** o firmware realiza com sucesso a leitura contínua do sensor de temperatura MPU6050 via I2C e do estado do botão físico. As lógicas de controle de tempo operam de maneira não-bloqueante, o que permite monitorar os milissegundos decorridos com a porta aberta e calcular a variação térmica (&#916;T) simultaneamente no loop principal.
- **Quais requisitos foram atendidos:** o código atende a todos os requisitos críticos de automação exigidos pela esteira de testes do Wokwi CI. O microcontrolador imprime com exatidão as mensagens seriais parametrizadas: a mensagem de inicialização, os disparos de falha, e o aviso de segurança e restauração
- **Resultado observado na simulação do Wokwi:** seguindo os parâmetros estipulados para os testes, ao soltar o botão e mantê-lo assim por 5000 ms ou mais, o alerta de exposição prolongada é acionado no terminal Serial. Se a temperatura subir abruptamente em 3.0°C em relação à referência segura, o alerta de degradação térmica dispara imediatamente. Ao anular os riscos simulados (fechando a porta e normalizando a temperatura lida pelo sensor), o sistema aguarda a janela de estabilização de 600 ms e reporta o retorno bem-sucedido ao seu estado de operação normal.

---

## Comentários Adicionais (Opcional)

- **Dificuldades encontradas:** o principal desafio técnico foi conciliar a lógica de temporização não-bloqueante para monitorar os dois eventos críticos simultaneamente (tempo de porta aberta e variação térmica) sem pausar o laço principal. Além disso, foi necessário ter uma atenção rigorosa aos detalhes para garantir que todas as mensagens da interface Serial fossem impressas com a grafia exata exigida pela automação de testes do CI.
- **Limitações da solução:** a utilização do sensor inercial MPU6050 cumpre o requisito de ler a temperatura local, apesar de ser um sensor voltado para giroscópio/acelerômetro. O uso de um sensor dedicado (como um DHT22) seria mais preciso. Outra limitação é o botão físico que simula a porta de forma binária (aberta/fechada), o que não permite detectar cenários onde a porta fica apenas encostada ou com uma pequena fresta.
- **Melhorias que faria com mais tempo:** seria interessante evoluir o projeto para uma arquitetura IoT completa, adicionando a configuração da rede Wi-Fi do ESP32 para publicar os logs e dados de temperatura em um dashboard na nuvem via protocolo MQTT. Também adicionaria um display local (como um OLED I2C) para que a equipe do ambiente refrigerado pudesse acompanhar o status da temperatura e os alarmes visualmente, sem depender apenas do console Serial.

---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
