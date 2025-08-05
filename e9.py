palavra = input("Insira palavra: ")

if palavra == palavra[::-1]:
    print("Palíndromo")
else:
    print("Não é palíndromo.")