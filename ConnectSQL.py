import pandas as pd
import pyodbc
from tkinter import *
from tkinter import messagebox
from tabulate import tabulate


class DatabaseConnection:
    def __init__(self, server, database):
        self.server = server
        self.database = database

    def connect(self):
        try:
            connection_string = (
                f"Driver=SQL Server;"
                f"Server={self.server};"
                f"Database={self.database};"
            )
            connection = pyodbc.connect(connection_string)
            print("Conexão feita com sucesso.")
            return connection

        except Exception as erro:
            print("Erro ao conectar ao banco de dados:")
            print(erro)
            exit()


class Cliente:
    def __init__(self, connection):
        self.connection = connection

    def insert_data(self, cpf, nome, endereco, email):
        try:
            cursor = self.connection.cursor()
            query = f"""INSERT INTO CLIENTES (CPF, Nome_Cliente, Endereco_Cliente, Email_Cliente)
            VALUES ('{cpf}', '{nome}', '{endereco}', '{email}')"""
            cursor.execute(query)
            cursor.commit()
            print("Dados do cliente inseridos com sucesso!")

        except Exception as erro:
            print("Erro ao inserir dados")
            print(erro)

    def select_data(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM CLIENTES"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Criar um DataFrame do pandas com os dados
            df = pd.DataFrame(
                [tuple(row) for row in rows],
                columns=[column[0] for column in cursor.description],
            )

            return df

        except Exception as erro:
            print("Erro ao selecionar dados")
            print(erro)


class Produtos:
    def __init__(self, connection):
        self.connection = connection

    def insert_data(self, id_produto, nome_produto, descricao, preco):
        try:
            cursor = self.connection.cursor()
            query = f"""INSERT INTO PRODUTOS (ID_Produto, Nome_Produto, Descricao_Produto, Preco_Produto)
            VALUES ({id_produto}, '{nome_produto}', '{descricao}', {preco})"""
            cursor.execute(query)
            cursor.commit()
            print("Dados inseridos com sucesso!")

        except Exception as erro:
            print("Erro ao inserir dados")
            print(erro)

    def select_data(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM PRODUTOS"
            cursor.execute(query)
            rows = cursor.fetchall()

            df = pd.DataFrame(
                [tuple(row) for row in rows],
                columns=[column[0] for column in cursor.description],
            )

            return df

        except Exception as erro:
            print("Erro ao selecionar dados")
            print(erro)


class Pedidos:
    def __init__(self, connection):
        self.connection = connection

    def insert_data(self, id_pedido, quantidade_produto, data_pedido, cpf, id_produto):
        try:
            cursor = self.connection.cursor()
            query = f"""INSERT INTO PEDIDOS (ID_Pedido, CPF, ID_Produto, Quantidade_Produto, Data_Pedido)
            VALUES ({id_pedido}, '{cpf}', {id_produto}, {quantidade_produto}, '{data_pedido}')"""
            cursor.execute(query)
            cursor.commit()
            print("Dados inseridos com sucesso!")

        except Exception as erro:
            print("Erro ao inserir dados")
            print(erro)

    def select_data(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM PEDIDOS"
            cursor.execute(query)
            rows = cursor.fetchall()

            df = pd.DataFrame(
                [tuple(row) for row in rows],
                columns=[column[0] for column in cursor.description],
            )

            return df

        except Exception as erro:
            print("Erro ao selecionar dados")
            print(erro)


class Janela_principal:
    def __init__(self, connection):
        self.connection = connection
        self.root = Tk()
        self.root.title("Sistema de Mercado")
        self.root.geometry("500x500")
        self.root.option_add("*Font", "Arial 12")

        # Botão para abrir a janela de Cliente
        cliente_button = Button(
            self.root, text="Cliente", command=self.open_cliente_window
        )
        cliente_button.pack(pady=10)

        # Botão para abrir a janela de Produtos
        produtos_button = Button(
            self.root, text="Produtos", command=self.open_produtos_window
        )
        produtos_button.pack(pady=10)

        # Botão para abrir a janela de Pedidos
        pedidos_button = Button(
            self.root, text="Pedidos", command=self.open_pedidos_window
        )
        pedidos_button.pack(pady=10)

        self.root.mainloop()

    def open_cliente_window(self):
        cliente_window = Toplevel(self.root)
        cliente_window.title("Cliente")
        cliente_window.geometry("500x500")
        cliente_window.option_add("*Font", "Arial 12")

        # Crie a interface da janela de cliente aqui

        cpf_label = Label(cliente_window, text="CPF:")
        cpf_label.pack()

        cpf_entry = Entry(cliente_window)
        cpf_entry.pack()

        nome_label = Label(cliente_window, text="Nome:")
        nome_label.pack()

        nome_entry = Entry(cliente_window)
        nome_entry.pack()

        endereco_label = Label(cliente_window, text="Endereço:")
        endereco_label.pack()

        endereco_entry = Entry(cliente_window)
        endereco_entry.pack()

        email_label = Label(cliente_window, text="Email:")
        email_label.pack()

        email_entry = Entry(cliente_window)
        email_entry.pack()

        save_button = Button(
            cliente_window,
            text="Salvar",
            command=lambda: self.save_cliente(
                cpf_entry.get(), nome_entry.get(), endereco_entry.get(), email_entry.get()
            ),
        )
        save_button.pack(pady=10)

        clear_button = Button(
            cliente_window,
            text="Limpar",
            command=lambda: self.clear_entries(
                cpf_entry, nome_entry, endereco_entry, email_entry
            ),
        )
        clear_button.pack(pady=10)

        view_button = Button(
            cliente_window, text="Visualizar", command=self.view_clientes
        )
        view_button.pack(pady=10)

    def save_cliente(self, cpf, nome, endereco, email):
        try:
            cliente = Cliente(self.connection)
            cliente.insert_data(cpf, nome, endereco, email)
            messagebox.showinfo(
                "Sucesso", "Dados do cliente inseridos com sucesso!"
            )
        except Exception as erro:
            messagebox.showerror("Erro", f"Erro ao inserir dados do cliente:\n{erro}")

    def view_clientes(self):
        try:
            cliente = Cliente(self.connection)
            df = cliente.select_data()
            self.display_dataframe(df)
        except Exception as erro:
            messagebox.showerror(
                "Erro", f"Erro ao exibir dados dos clientes:\n{erro}"
            )

    def display_dataframe(self, df):
        dataframe_window = Toplevel(self.root)
        dataframe_window.title("Dados dos Clientes")
        dataframe_window.geometry("600x400")

        # Criar um componente Text para exibir o DataFrame
        text_widget = Text(dataframe_window, font=("Courier", 10))
        text_widget.pack(fill=BOTH, expand=YES)

        # Converter o DataFrame para uma tabela formatada
        table = tabulate(df, headers="keys", tablefmt="psql")

        # Exibir a tabela na janela
        text_widget.insert(END, table)

    def open_produtos_window(self):
        produtos_window = Toplevel(self.root)
        produtos_window.title("Produtos")
        produtos_window.geometry("500x500")
        produtos_window.option_add("*Font", "Arial 12")

        # Crie a interface da janela de produtos aqui

        id_produto_label = Label(produtos_window, text="ID do Produto:")
        id_produto_label.pack()

        id_produto_entry = Entry(produtos_window)
        id_produto_entry.pack()

        nome_produto_label = Label(produtos_window, text="Nome do Produto:")
        nome_produto_label.pack()

        nome_produto_entry = Entry(produtos_window)
        nome_produto_entry.pack()

        descricao_label = Label(produtos_window, text="Descrição:")
        descricao_label.pack()

        descricao_entry = Entry(produtos_window)
        descricao_entry.pack()

        preco_label = Label(produtos_window, text="Preço:")
        preco_label.pack()

        preco_entry = Entry(produtos_window)
        preco_entry.pack()

        save_button = Button(
            produtos_window,
            text="Salvar",
            command=lambda: self.save_produto(
                id_produto_entry.get(),
                nome_produto_entry.get(),
                descricao_entry.get(),
                preco_entry.get(),
            ),
        )
        save_button.pack(pady=10)

        clear_button = Button(
            produtos_window,
            text="Limpar",
            command=lambda: self.clear_entries(
                id_produto_entry, nome_produto_entry, descricao_entry, preco_entry
            ),
        )
        clear_button.pack(pady=10)

        view_button = Button(
            produtos_window, text="Visualizar", command=self.view_produtos
        )
        view_button.pack(pady=10)

    def save_produto(self, id_produto, nome_produto, descricao, preco):
        try:
            produto = Produtos(self.connection)
            produto.insert_data(id_produto, nome_produto, descricao, preco)
            messagebox.showinfo(
                "Sucesso", "Dados do produto inseridos com sucesso!"
            )
        except Exception as erro:
            messagebox.showerror("Erro", f"Erro ao inserir dados do produto:\n{erro}")

    def view_produtos(self):
        try:
            produtos = Produtos(self.connection)
            df = produtos.select_data()
            self.display_dataframe(df)
        except Exception as erro:
            messagebox.showerror(
                "Erro", f"Erro ao exibir dados dos produtos:\n{erro}"
            )

    def open_pedidos_window(self):
        pedidos_window = Toplevel(self.root)
        pedidos_window.title("Pedidos")
        pedidos_window.geometry("500x500")
        pedidos_window.option_add("*Font", "Arial 12")

        # Crie a interface da janela de pedidos aqui

        id_pedido_label = Label(pedidos_window, text="ID do Pedido:")
        id_pedido_label.pack()

        id_pedido_entry = Entry(pedidos_window)
        id_pedido_entry.pack()

        quantidade_produto_label = Label(pedidos_window, text="Quantidade do Produto:")
        quantidade_produto_label.pack()

        quantidade_produto_entry = Entry(pedidos_window)
        quantidade_produto_entry.pack()

        data_pedido_label = Label(pedidos_window, text="Data do Pedido:")
        data_pedido_label.pack()

        data_pedido_entry = Entry(pedidos_window)
        data_pedido_entry.pack()

        cpf_label = Label(pedidos_window, text="CPF do Cliente:")
        cpf_label.pack()

        cpf_entry = Entry(pedidos_window)
        cpf_entry.pack()

        id_produto_label = Label(pedidos_window, text="ID do Produto:")
        id_produto_label.pack()

        id_produto_entry = Entry(pedidos_window)
        id_produto_entry.pack()

        save_button = Button(
            pedidos_window,
            text="Salvar",
            command=lambda: self.save_pedido(
                id_pedido_entry.get(),
                quantidade_produto_entry.get(),
                data_pedido_entry.get(),
                cpf_entry.get(),
                id_produto_entry.get(),
            ),
        )
        save_button.pack(pady=10)

        clear_button = Button(
            pedidos_window,
            text="Limpar",
            command=lambda: self.clear_entries(
                id_pedido_entry,
                quantidade_produto_entry,
                data_pedido_entry,
                cpf_entry,
                id_produto_entry,
            ),
        )
        clear_button.pack(pady=10)

        view_button = Button(
            pedidos_window, text="Visualizar", command=self.view_pedidos
        )
        view_button.pack(pady=10)

    def save_pedido(self, id_pedido, quantidade_produto, data_pedido, cpf, id_produto):
        try:
            pedido = Pedidos(self.connection)
            pedido.insert_data(id_pedido, quantidade_produto, data_pedido, cpf, id_produto)
            messagebox.showinfo(
                "Sucesso", "Dados do pedido inseridos com sucesso!"
            )
        except Exception as erro:
            messagebox.showerror("Erro", f"Erro ao inserir dados do pedido:\n{erro}")

    def view_pedidos(self):
        try:
            pedidos = Pedidos(self.connection)
            df = pedidos.select_data()
            self.display_dataframe(df)
        except Exception as erro:
            messagebox.showerror(
                "Erro", f"Erro ao exibir dados dos pedidos:\n{erro}"
            )

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, END)


def main():
    # Dados da conexão
    server = "DESKTOP-BODCT7F"
    database = "Mercado"

    # Conectando ao banco de dados
    db_connection = DatabaseConnection(server, database)
    connection = db_connection.connect()

    Janela_principal(connection)

    connection.close()


if __name__ == "__main__":
    main()
