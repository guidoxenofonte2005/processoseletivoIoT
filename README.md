# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

### 👤 Identificação do Candidato

- **Nome completo:** Guido Xenofonte de Almeida Gonçalves
- **GitHub:** guidoxenofonte2005

---

## 1️⃣ Visão Geral da Solução

O objetivo do projeto é ser um sistema de detecção de vazamentos de gás em fogões caseiros e/ou máquinas industriais que utilizam queima de gás para funcionamento, com o uso adicional de um modo extra para detectar presença de monóxido de carbono em um ambiente industrial.
O sistema utiliza dados de temperatura e gás no ambiente para identificar se está havendo queima correta, se há gás não sendo queimado ou se a temperatura ambiente está muito alta, notificando o usuário através de uma tela e de um buzzer conforme os dados são processados.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O programa principal (`main.py`) opera em um loop contínuo com intervalo de 2 segundos entre cada leitura, respeitando o tempo mínimo de resposta do sensor DHT22.

A cada iteração, o fluxo é:

1. Leitura da temperatura via DHT22
2. Leitura do nível de gás via ADC
3. Verificação do modo ativo pelo slide switch (GLP ou CO)
4. Chamada de `checkValues()` que retorna um dos estados: `OK`, `HOT`, `ALERT`, `DNG` ou `ERR`
5. Ação correspondente ao estado — atualização do display OLED e controle do buzzer

Os estados do sistema são:

- **OK** — gás dentro do limite seguro, buzzer desligado, tela exibe leitura normal
- **HOT** — gás seguro mas temperatura acima de 45°C, tela exibe alerta de temperatura
- **ALERT** — gás em nível intermediário, tela exibe aviso de verificação
- **DNG** — gás em nível de perigo, buzzer ativado, tela exibe alerta crítico
- **ERR** — modo inválido (nenhum switch ativo), tela exibe mensagem de erro

Os componentes são inicializados em `globals.py` e a lógica de exibição é encapsulada na classe `OledScreen` em `screen.py`.

---

## 3️⃣ Componentes Utilizados na Simulação

- **ESP32** — microcontrolador principal
- **Sensor MQ (wokwi-gas-sensor)** — leitura analógica do nível de gás via ADC
- **DHT22** — leitura de temperatura e umidade
- **Display OLED SSD1306 128x64** — exibe o estado atual do sistema via I2C
- **Buzzer** — atuador sonoro controlado via PWM, ativado apenas no estado de perigo
- **Slide Switch** — seleciona o modo de operação: posição 1 ativa modo GLP, posição 2 ativa modo CO

---

## 4️⃣ Decisões Técnicas Relevantes

**Separação em módulos:** o código foi dividido em `globals.py` (configuração de hardware e constantes), `screen.py` (lógica de exibição) e `main.py` (fluxo principal), facilitando manutenção e leitura.

**Constantes de limite nomeadas:** os thresholds de gás e temperatura foram definidos como constantes com nomes descritivos (`GAS_GLP_SAFE`, `GAS_CO_ALERT`, `TEMP_HOT`) em vez de números soltos no código, tornando os limites fáceis de ajustar e entender.

**Uso de `checkValues()`:** a lógica de decisão foi centralizada em uma função pura que recebe modo, gás e temperatura e retorna um estado textual. Isso separa a lógica de negócio das ações de hardware, facilitando testes e futuras modificações.

**Controle do buzzer via `init()`/`deinit()`:** em vez de controlar o duty cycle para silenciar, o PWM é completamente desativado com `deinit()` quando não necessário, evitando consumo desnecessário e ruído residual.

**Delay de 2 segundos:** o `utime.sleep_ms(2000)` respeita o intervalo mínimo de leitura do DHT22 e evita sobrecarga do processador no loop principal.

**Slide switch único para dois modos:** um único switch de três posições substitui dois botões separados, usando os pinos externos para cada modo e o pino central conectado ao VCC, com pull-down nos pinos de entrada.

---

## 5️⃣ Resultados Obtidos

O sistema inicializa corretamente e entra em operação contínua. O modo é selecionado pelo slide switch e o display exibe as informações correspondentes ao estado detectado. O buzzer é ativado exclusivamente no estado de perigo (`DNG`) e no estado de erro (`ERR`), sendo desativado em outros estados.

Todos os estados foram implementados e testados na simulação do Wokwi:
- Leitura dos sensores funcionando corretamente
- Transição entre estados refletida no display em tempo real
- Buzzer respondendo corretamente ao estado de perigo
- Separação de comportamento entre os modos GLP e CO

---

## 6️⃣ Comentários Adicionais (Opcional)

O maior desafio foi entender as limitações do MicroPython em relação ao Python convencional — a ausência de `match/case` e de vários módulos padrão exigiu adaptações na estrutura do código.

Uma melhoria relevante seria adicionar persistência do último modo ativo, para que ao religar o sistema ele retome o estado anterior sem depender do switch estar posicionado.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
