# Busca Vagas Gupy

Este projeto é um scraper de vagas de emprego que utiliza o **Selenium** para buscar e extrair informações de vagas no portal **Gupy**. A implementação atual tem como objetivo retornar apenas as vagas mais recentes (até 10 vagas) para cada termo de pesquisa fornecido.

## Pré-requisitos

Antes de executar o código, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/013renan/busca-vagas-gupy.git
   cd busca-vagas-gupy
   ```
   
2. Crie um ambiente virtual (opcional, mas recomendado):

  ```bash
  python -m venv venv
  ```

3. Ative o ambiente virtual:
   
  No Windows:   
  ```bash
  venv\Scripts\activate
  ```

  No macOS/Linux:   
  ```bash
  source venv/bin/activate
  ```

 4. Instale as dependências necessárias:

  ```bash
  pip install -r requirements.txt
  ```

## Uso

1. Abra o arquivo `busca_vagas.py` e defina os termos de pesquisa e a data mínima no início do script.

  ```python
  termos_pesquisa = ['analista de dados', 'analista bi']
  data_minima = '01-11-2024'
  ```

2. Execute o script:

  ```bash
  python busca_vagas.py
  ```

3. Após a execução, um arquivo chamado `vagas.csv` será gerado na mesma pasta, contendo as vagas encontradas.

## Observações

>O código utiliza sessões ativas no Selenium, permitindo a interação dinâmica com o site da Gupy.
>A implementação atual retorna apenas as vagas mais recentes, limitando a busca a um máximo de 10 vagas para cada termo pesquisado.

## Estrutura do Projeto

>`busca_vagas.py`: O código principal que realiza a busca de vagas.
>`requirements.txt`: Lista de dependências do projeto.
>`README.md`: Este arquivo com instruções sobre o projeto.

   

    

