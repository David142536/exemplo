import sqlite3 # biblioteca de servidor de banco de dados 


# esta função cria um banco de dados chamado exemplo.db e uma tabela chamada usuarios 
def criar_tabela():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTEGER)''')
    conexao.commit()
    conexao.close()

# implementação das operações CRUD
# Create (criar):
def adicionar_usuario(nome,idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conexao.commit()
    conexao.close()

# Read (ler):
def listar_usuarios():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

# Update (atualizar):
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('UPDATE usuarios SET nome = ?, idade = ?WHERE id = ?', (nome, idade, id))
    conexao.commit()
    conexao.close()

    #Delete (deletar):
def deletar_usuario(id):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()


#testando o CRUD
def menu():
    criar_tabela()
    while True:
        print("/n1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            adicionar_usuario(nome, idade)
        elif escolha == '2':
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif escolha == '3':
            id = int(input("ID do usuário: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            atualizar_usuario(id, nome, idade)
        elif escolha == '4':
            id = int(input("ID do usuário a deletar: "))
            deletar_usuario(id)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")

            menu()