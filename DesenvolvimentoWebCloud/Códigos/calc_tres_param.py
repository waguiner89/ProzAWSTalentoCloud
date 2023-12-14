def calculadora (num1, num2, ope):
    if ope == 1:
        res = num1 + num2
    elif ope == 2:
        res = num1 - num2
    elif ope == 3:
        res = num1 * num2
    elif ope == 4:
        if num2 != 0:
            res = num1 / num2
        else:
            print ("Erro! Impossivel divisao por ZERO!")
            return 0
    else:
        print ("Opcao invalida! Escolha entre 1-Soma / 2-Subtracao / 3-Multiplicacao / 4-Divisao")
        return 0
    return res

resultado = calculadora(10, 0, 4)
print (resultado)
