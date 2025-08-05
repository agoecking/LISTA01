nomeProdutoUm = input("Insira nome do produto: ")
nomeProdutoDois = input("Insira nome do produto: ")
nomeProdutoTres = input("Insira nome do produto: ")

valorProdutoUm = float(input("Insira valor do produto: "))
valorProdutoDois = float(input("Insira valor do produto: "))
valorProdutoTres = float(input("Insira valor do produto: "))

total = valorProdutoUm + valorProdutoDois + valorProdutoTres

if total > 100:
    desconto = total * 0.1
    total = total - desconto

print("Compra de: ", nomeProdutoUm, " ", nomeProdutoDois, " ", nomeProdutoTres, " é: ", total)