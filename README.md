# Sistema de Cálculo de Médias Escolares

<div style="text-align: center;">
    <img src="https://camo.githubusercontent.com/a9d8eec804fd767fe30d59ee913f6f07b2fe8765e6cf03170af749c59ac75988/68747470733a2f2f696d672e69636f6e73382e636f6d2f636f6c6f722f3235362f707974686f6e2e706e67" alt="Logo do Projeto" width="200"/>
</div>

## 📖 Descrição

O **Sistema de Cálculo de Médias Escolares** é uma aplicação desktop desenvolvida em Python. Ela permite que usuários insiram dados de alunos, calculem suas médias e verifiquem suas situações acadêmicas, tudo através de uma interface gráfica intuitiva.

## 🚀 Funcionalidades

- **Inserção de Dados**: Cadastre o nome do aluno e suas notas.
- **Cálculo Automático de Média**: Média calculada automaticamente.
- **Verificação de Situação**: Informa se o aluno está Aprovado, Em Recuperação ou Reprovado.
- **Exibição em Tabela**: Visualização organizada dos dados em uma tabela.
- **Persistência de Dados**: Salve e recupere dados em formato CSV ou XLSX.
- **Alteração e Exclusão**: Modifique ou remova registros conforme necessário.

## 💻 Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: Para a interface gráfica.
- **Pandas**: Para manipulação de dados.
- **OpenPyXL** (opcional): Para trabalhar com arquivos XLSX.

## 📦 Pré-requisitos

1. Ter o Python 3.x instalado.
2. Instalar as bibliotecas necessárias:

   ```bash
   pip install pandas openpyxl

🚧 Como Executar

1. Clone o Repositório ou baixe o código.
2. Prepare o Arquivo de Dados: Crie um `PlanilhaAlunos.csv` no diretório indicado no código.
3. Execute o Script:

   python nome_do_script.py

4. Interaja com a Aplicação: Insira dados e utilize as funcionalidades.

📂 Estrutura do Código
- Classe `PrincipalRAD`: Gerencia a interface e as operações de dados.
  - `__init__`: Inicializa a interface.
  - `carregarDadosIniciais`: Carrega dados de um arquivo CSV.
  - `fSalvarDados`: Salva dados em um arquivo CSV.
  - `fVerificarSituacao`: Calcula a média e situação do aluno.
  - `fCalcularMedia`: Insere dados na tabela.
  - `fAlterar`: Modifica registros existentes.
  - `fExcluir`: Remove registros da tabela.
    
🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

📜 Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais informações.

