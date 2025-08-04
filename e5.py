idade = int(input("Insira idade: "))

if idade < 12:
    classificacao = "Crianca"
elif idade < 17:
    classificacao = "Adolescente"
elif idade < 59:
    classificacao = "Adulto"
elif idade >= 60:
    classificacao = "Idoso"

print(classificacao)