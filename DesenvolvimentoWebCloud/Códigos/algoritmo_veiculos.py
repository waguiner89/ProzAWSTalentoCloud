qtde_rodas = int(input("Digite a quantidade de rodas do veiculo: "))
peso = int(input("Digite o peso bruto em quilogramas: "))
qtde_pessoas = int(input("Digite a quantidade máxima de pessoas no veiculo: "))

if qtde_rodas <= 3:
    print("Categoria A")
elif qtde_rodas == 4 and qtde_pessoas <= 8 and peso <= 3500:
    print("Categoria B")
elif qtde_rodas >= 4 and peso >= 3500 and peso <= 6000:
    print("Categoria C")
elif qtde_rodas >= 4 and qtde_pessoas > 8:
    print("Categoria D")
elif qtde_rodas >= 4 and peso > 6000:
    print("Categoria E")
else:
    print("Tudo errado")