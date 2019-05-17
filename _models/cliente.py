from _models import conexao
import config

class Cliente:

    def __init__(self, nome, cpf, data_nasc, email, tel):
        self.connection = conexao.Conexao()
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.email = email
        self.tel = tel

    def insereCliente(self):
        # Query
        sql = f"INSERT INTO {config.TABLE_CLIENTE} (nome, cpf, data_nasc, email, tel) VALUES (%s, %s, %s, %s, %s)"
        values = (f'{self.nome}', f'{self.cpf}', f'{self.data_nasc}', f'{self.email}', f'{self.tel}')

        self.connection.insereBanco(sql, values)

    def updateCliente(self):
        # Query
        sql = f"UPDATE {config.TABLE_CLIENTE} SET nome= %s , cpf= %s , data_nasc= %s, email = %s, tel = %s " \
            f"WHERE nome = %s"
        values = (f'{self.nome}', f'{self.cpf}', f'{self.data_nasc}', f'{self.email}', f'{self.tel}', f'{self.nome}')

        self.connection.updateBanco(sql, values)

    def selectCliente(self):
        # Query
        sql = f"SELECT id_cliente, nome, cpf, data_nasc, email, tel FROM {config.TABLE_CLIENTE} WHERE nome = %s"
        values = f'{self.nome}'

        select = self.connection.selectBanco(sql, values)
        print(select)


pessoa = Cliente.selectCliente()