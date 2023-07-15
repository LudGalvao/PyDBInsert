# PyDBInsert

Este é um sistema básico de inserção de dados desenvolvido em Python. Ele permite gerenciar clientes, produtos e pedidos, além de exibir os dados em uma interface gráfica.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- **Clientes**: é possível cadastrar novos clientes fornecendo informações como CPF, nome, endereço e e-mail.
- **Produtos**: é possível cadastrar novos produtos fornecendo informações como ID do produto, nome, descrição e preço.
- **Pedidos**: é possível registrar pedidos relacionando clientes e produtos. É necessário fornecer informações como ID do pedido, quantidade do produto, data do pedido, CPF do cliente e ID do produto.

Além disso, o sistema permite visualizar os dados dos clientes, produtos e pedidos em tabelas formatadas.

## Requisitos

O sistema requer os seguintes requisitos:

- Python 3.x
- Bibliotecas: pandas, pyodbc, tkinter, tabulate

Certifique-se de ter as bibliotecas instaladas antes de executar o programa. Caso não estejam instaladas, você pode instalá-las usando o gerenciador de pacotes `pip`.


## Configuração

Antes de executar o programa, é necessário configurar os dados de conexão com o banco de dados. No arquivo `main.py`, localize as seguintes linhas de código:

```python
# Dados da conexão
server = "DESKTOP-BODCT7F"
database = "Mercado"

# Codigo funcionando
