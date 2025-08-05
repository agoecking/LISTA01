quantidadeAlunos = int(input("Insira a quantidade de alunos: "))
soma = 0

for i in range(quantidadeAlunos):
    soma = soma + int(input("Insira nota: "))

print("Media: ", soma/quantidadeAlunos)