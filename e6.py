valorDeSaque = int(input("insira o valor de saque: "))

if valorDeSaque >= 100:
    print("Notas de 100: ", int(valorDeSaque / 100))
    valorDeSaque = valorDeSaque % 100
if valorDeSaque >= 50:
    print("Notas de 50: ", int(valorDeSaque / 50))
    valorDeSaque = valorDeSaque % 50
if valorDeSaque >= 20:
    print("Notas de 20: ", int(valorDeSaque / 20))
    valorDeSaque = valorDeSaque % 20
if valorDeSaque >= 10:
    print("Notas de 10: ", int(valorDeSaque / 10))
    