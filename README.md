# 🛡️ Projeto Cyquest: Simulador de Sequestro de Dados (CyLock)

## ## Visão Geral
O **Cyquest** é uma ferramenta de simulação de sequestro digital (Ransomware Ético) desenvolvida para a liga acadêmica **CyLock**. O objetivo é demonstrar o impacto de ataques de criptografia em sistemas desprotegidos e validar planos de recuperação de dados.

---

## ## 👥 Divisão de Responsabilidades

### ### 1. Arquitetura de Criptografia
* **Tarefa:** Desenvolvimento do **Motor de Cifragem/Decifragem**.
* **Responsabilidade:** Criar as funções que transformam arquivos originais em dados ilegíveis e a função inversa que utiliza uma chave para restaurar o conteúdo. Deve garantir a integridade dos dados para que a simulação seja 100% reversível.

### ### 2. Sistema de Arquivos e Varredura
* **Tarefa:** Desenvolvimento do **Módulo de Busca e Identificação**.
* **Responsabilidade:** Criar o script recursivo que percorre o diretório alvo, identifica arquivos por extensões (fotos, vídeos, documentos) e gera a lista de caminhos (paths) para o processamento do motor.

### ### 3. Design de Interface e Nota de Resgate
* **Tarefa:** Desenvolvimento da **Interface de Usuário e Alertas**.
* **Responsabilidade:** Criar a janela de aviso (pop-up), gerar os arquivos de texto de instrução (`.txt`) e implementar o script que altera o papel de parede do sistema operacional após a conclusão do sequestro.

### ### 4. e QA (Garantia de Qualidade)
* **Tarefa:** **Laboratório de Testes e Documentação Defensiva**.
* **Responsabilidade:** validar a eficácia do decifrador, realizar auditoria de performance e redigir o manual de mitigação e defesa contra o ataque simulado.

---

## ## 🚀 Passo a Passo para a Implementação

### ### Passo 1: Definição do Protocolo
* Listar as extensões alvo (Ex: `.jpg, .png, .pdf, .docx, .mp4`).

### ### Passo 2: Mapeamento e Varredura
* O módulo de busca deve listar todos os arquivos elegíveis em uma pasta de teste.
* **Segurança:** Validar filtros para ignorar arquivos críticos do sistema operacional.

### ### Passo 3: Execução do Motor Criptográfico
* Implementar a leitura binária (`rb`) e escrita binária (`wb`).
* Aplicar o algoritmo (Ex: AES-256) para cifrar o conteúdo e renomear os arquivos.

### ### Passo 4: Ativação do Impacto Visual
* Disparar a interface de usuário assim que o motor concluir a lista de arquivos.
* Alterar o papel de parede e exibir a janela de "Resgate" da CyLock.

### ### Passo 5: Validação da Recuperação
* Inserir a chave no módulo de decifração.
* Verificar se todos os arquivos retornaram ao estado original e abrem sem erros.

### ### Passo 6: Compilação Final
* Transformar os scripts Python em um executável único (`.exe`) para demonstração.
