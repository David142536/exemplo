import pandas as pd

#listas de perguntas
questions = [
    ["Qual é a capital da frança?", "Paris", "Londres", "Berlim", "Roma", 1],
    ["Qual é o resultado de 8 + 5?", "12", "13", "15", "18", 2],
    ["Quem pintou a Mona Lisa?", "Pablo Picasso", "Leonardo Da Vinci", "Van Gogh", "Warhol", 2],
    ["Quanto é 6 multiplicado por 7?", "40", "42", "43", "45", 2],
    ["Qual é o maior planeta do sistema solar?", "Saturno", "Júpiter", "Urano", "Marte", 2],
    ["Quem escreveu a obra 'Dom Quixote'?", "Machado de Assis", "Miguel de Servantes", "Jorge Luis Borges", "Rachel de Queiroz", 2],
    ["Qual é a fórmula química da água?", "NaCI", "O³", "CO²", "H²O", 4],
]

#Criar dataframe do pandas
df = pd.DataFrame(questions, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

#Salvar no arquivo excel
df.to_excel("questions.xlsx", index=False)

print("Perguntas inseridas com sucesso!")