import mysql.connector as mysql

conexao = mysql.connect(
    host='localhost',
    user='root',
    password='Moreir@',
    database='alunos',
)
cursor = conexao.cursor()

# testando o crud e implementando o primeiro registro 
# nome = 'Adriel'
# idade = 20
# comando = f'INSERT INTO lista (nome, idade) VALUES ("{nome}", {idade})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# implementando as funções do crud
while True:
    print()
    print("1. Para adicionar itens")
    print("2. Para vizualizar os itens do banco de dados")
    print("3. Para atualizar um item no banco de dados")
    print("4. Para deletar um item do banco de dados")
    print()
    a = input("Insira uma opção ou digite 'sair' para encerrar: ")
        # CREATE
    if a == '1':
        nome = input("Insira um nome: ")
        idade = input("Insira a idade: ")
        comando = f'INSERT INTO lista (nome, idade) VALUES ("{nome}", {idade})'
        cursor.execute(comando)
        conexao.commit()
        print("Aluno cadastrado com sucesso!")

        # READ
    elif a == '2':
        comando = f'SELECT * FROM lista'
        cursor.execute(comando)
        resultado = cursor.fetchall() # lê o banco de dados
        for linha in resultado:
            print(linha)

        # UPDATE
    elif a == '3':
      cursor = conexao.cursor()
      id_usuario = input("Digite o id do item que deseja atualizar: ") 
      sql = "UPDATE lista SET nome = %s, idade = %s WHERE id_alunos = %s"
      novo_nome = input("Digite o novo nome: ")
      nova_idade = input("Digite a nova idade: ")
      valores = (novo_nome, nova_idade, id_usuario)
      cursor.execute(sql, valores)
      conexao.commit()
      print("Registro atualizado com sucesso!")

        #DELETE
    elif a == '4':
        deletar = int(input("Digite o id do aluno que deseja excluir: "))
        comando = f'DELETE FROM lista WHERE id_alunos = "{deletar}"'
        cursor.execute(comando)
        conexao.commit()
    
    elif a == 'sair':
        break

cursor.close()
conexao.close()