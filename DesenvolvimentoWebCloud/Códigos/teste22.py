idade = 1
casadog = 0
casado = 1
solteirog = 0
mediaida =0
porcent = 0
solteiro = 1
viuvag = 0
viuva = 1
idadev = 0
divorcg = 0
divorc = 1
idade = int(input("Digite sua idade: "))
while idade >= 1:
    opcao = int(input("Escolha o estado civil: 1-Casado - 2-Solteiro - 3-Viúva(o) - 4-Divorciado \n"))
    print("                                                                               ")
    if opcao == 1:
       casadog = casadog + casado
       idade = int(input("Digite sua idade: "))
    elif opcao == 2:
       solteirog = solteirog + solteiro
       idade = int(input("Digite sua idade: "))
    elif opcao == 3:
       viuvag = viuvag + viuva
       idadev = idadev + idade
       mediaida = idadev / viuvag
       idade = int(input("Digite sua idade: "))
    elif opcao == 4:
       divorcg = divorcg + divorc
       totalesc = casadog + viuvag + solteirog + divorcg
       porcent = (divorcg*100) / totalesc
       idade = int(input("Digite sua idade: "))
print("Quantidade de casados ", casadog)
print("Quantidade de solteiros", solteirog)
print("Média da idade de pessoas viúvas(os)", mediaida)
print("Porcentagem divorciados", porcent,"%")
input()
