import config
import pymysql.cursors


class Conexao:

    def __init__(self):
        self.conexao = pymysql.connect(host= config.HOST,
                                    user= config.USER,
                                    password= config.PASS,
                                    db= config.BD_NOME,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def insereBanco(self, sql, values):
        with self.conexao.cursor() as cursor:

            # Execute query.
            cursor.execute(sql, values)
            self.conexao.commit()
            print('Inserido com sucesso!')

    def updateBanco(self, sql, values):
        with self.conexao.cursor() as cursor:

            # Execute query.
            cursor.execute(sql, values)
            self.conexao.commit()
            print('Alterado com sucesso!')

    def selectBanco(self, sql, values):
        with self.conexao.cursor() as cursor:

            cursor.execute(sql, values)
            result = cursor.fetchone()

            if result:
                print('Usuario encontrado!')
            else:
                print('Usuario não encontrado!')

            return result

    def __del__(self):
        self.conexao.close()
        print('Close Connection')

