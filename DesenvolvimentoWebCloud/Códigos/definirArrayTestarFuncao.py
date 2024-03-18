def procura_elemento (elem, arr):
    achou = False
    comprimento = len(arr)

    for i in range(comprimento):
        if (arr[i] == elem):
            achou = True

    if (achou == True):
        print("Achamos o nome: " + elem)
    else:
        print("Nome nao achado")

nomes = ["Rafael", "Wagner", "Sofia", "Verônica"]
procura_elemento("Wagner", nomes)