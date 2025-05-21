# adicionando a lista 
lista_tarefas = []

#adicionando o loop, continua enquanto verdade, até o momento não tem quesito nenhum 
while True:
    novo_item = input("Adicionar tarefas para adicionar à lista (ou 'sair' para encerrar): ")
    if novo_item.lower() == 'sair': #lower padroniza todas as letras deixando todas minúsculas
        break
    lista_tarefas.append(novo_item) #adicionando cada item a lista 

# mostrando na tela os itens da lista 
print("itens na lista: ")
quantidade = len(lista_tarefas) # len conta a quantidade 
# loop para mostrar na tela cada item da lista 
for novo_item in lista_tarefas:
    print()
    print(novo_item)
    print()
print(f"A quantidade de produtos é: {quantidade}") # mostrando a quantidade

# if caso o usuário não queira atualizar nenhum item 
z = bool(input("Responda 'sim' ou 'não' se quer atualizar algum item da lista: "))
for z in range(True) : # loop obrigatório para colocar o continue
    if z == "não" or "nao" or "Não" or "Nao":
        continue
else:
    #ter a opção de atualizar cada item da lista 
    i = int(input("Digite o número do item da lista que deseja atualizar, começando por 1: "))
    i = i - 1
    lista_tarefas[i] = input("Digite pelo que deseja atualizar o item: ")
    # mostrando os itens na tela
    print("itens na lista: ")  
    # loop para mostrar na tela cada item da lista 
    for novo_item in lista_tarefas:
        print()
        print(novo_item)
        print()