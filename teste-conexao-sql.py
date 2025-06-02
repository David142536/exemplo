import mysql.connector as mysql

try:
    conexao = mysql.connect(
        host='localhost',    # ou o IP do servidor
        port=3306,           # porta padrão do MySQL
        user='root',         # seu usuário
        password='Moreir@',  # sua senha
        database='MYSQL'  # nome do seu banco
    )
    print('Conectado com sucesso!')
except Exception as err:
    print('Houve um erro ao conectar')
    print(err)
finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexão encerrada.')