nome = input("insira nome do aluno: ")
nota1 = float(input("insira nota 1: "))
nota2 = float(input("insira nota 2: "))

media = (nota1 + nota2)/2

print("aluno: ", nome)
if media >= 6:
    print("Situação: aprovado")
else:
    print("Situação: reprovado")