lista_tarefas = []

while True:
    novo_item = input("Adicionar tarefas para adicionar à lista (ou 'sair' para encerrar): ")
    if novo_item.lower() == 'sair':
        break
    lista_tarefas.append(novo_item)

print("itens na lista: ")
quantidade = len(lista_tarefas)
for novo_item in lista_tarefas:
    print()
    print(novo_item)
    print()
print(f"A quantidade de produtos é: {quantidade}")