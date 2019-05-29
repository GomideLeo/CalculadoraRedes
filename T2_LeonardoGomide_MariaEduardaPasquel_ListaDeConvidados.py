import math

def getPt(str):
    print("Qual o numero de pontos de "+str+"? (-1 para corrigir valores):")
    while True:
        try:
            return int(input())
            break
        except ValueError:
            print("Digite um numero inteiro!")

print("\nBem vindo à Lista de Convidados, seu aplicativo para organizar festas de rede estruturada"
    "\nComece especificando sua rede para podermos ajudá-lo:\n")
while (True):
    ptTelecom = getPt("telecom")
    if (ptTelecom != -1):
        ptRede = getPt("conexão de rede (simples)")
        if ptRede !=-1:
            while (True):
                ptCFTV = getPt("CFTV IP")
                if ptCFTV > 2*ptTelecom+ptRede:
                    print ("Existem mais pontos que portas, digite um novo numero")
                else:
                    break
            if ptCFTV !=-1:
                while (True):
                    ptVoz = getPt("voz sobe IP")
                    if ptCFTV+ptVoz > 2*ptTelecom+ptRede:
                        print ("Existem mais pontos que portas, digite um novo numero")
                    else:
                        break
                if ptVoz !=-1:
                    break

ptTotal = 2*ptTelecom+ptRede

print("\nQual o tamanho médio em metros da malha horizontal")
while True:
    try:
        tamMedio = int(input())
        if tamMedio > 90:
            print("\nEsse cabo está meio longo, você deveria diminuí-lo!"
                    "\nQual o novo tamanho:")
        else:
            break
    except ValueError:
        print("Digite um numero inteiro!")

while True:
    print("\nQual categoria será utilizada para dados?"
        "\n 0 para cat 5e"
        "\n 1 para cat 6"
        "\n 2 para cat 6a"
        "\n 3 para cat 7"
        "\n 4 para cat 7a")
    while True:
        pass
        try:
            catRede = int(input())
            break
        except ValueError:
            print("Digite um numero inteiro!")
    if catRede == 0:
        catRede = "cat 5e"
        break
    if catRede == 1:
        catRede = "cat 6"
        break
    if catRede == 2:
        catRede = "cat 6a"
        break
    if catRede == 3:
        catRede = "cat 7"
        break
    if catRede == 4:
        catRede = "cat 7a"
        break
    print("Valor inválido!")

print("\nO rack vai ser aberto ou fechado?"
    "\n 0 para aberto"
    "\n 1 para fechado")
while True:
    while True:
        try:
            tipoRack = int(input())
            break
        except ValueError:
            print("Digite um numero inteiro!")
    if tipoRack == 0 or tipoRack == 1:
        break
    else:
        print("Valor inválido!")


tamTotal = 4*math.ceil((ptTotal)/24)
tamTemp = tamTotal
qtdRack = 1
while tamTemp  > 48:
    tamTemp -= 48
    qtdRack += 1
if tipoRack == 0:
    tamTotal += qtdRack*4
else:
    tamTotal += qtdRack*6
tamTemp = tamTotal
novaQtdRack = 1
while tamTemp > 48:
    tamTemp -= 48
    novaQtdRack += 1
if qtdRack != novaQtdRack:
    if tipoRack == 0:
        tamTotal += (novaQtdRack-qtdRack)*4
    else:
        tamTotal += (novaQtdRack-qtdRack)*6
while True:
    tamTemp= 1.5*tamTotal
    novaQtdRack = 1
    while tamTemp > 48:
        tamTemp -= 48
        novaQtdRack += 1
    if novaQtdRack > qtdRack:
        if tipoRack == 0:
            tamTotal += (novaQtdRack-qtdRack)*4
        else:
            tamTotal += (novaQtdRack-qtdRack)*6
        qtdRack = novaQtdRack
    else:
        break
tamTotal= math.ceil(1.5*tamTotal)

tamRack = math.ceil(tamTotal/qtdRack)
if tamRack%2==1:
    tamRack += 1
if tamRack>=12 and tamRack%4:
    tamRack += 2

print("\nSua lista de materiais convidados para a festa de rede estruturada:")

print("\nÁrea de Trabalho: \n"
        "  -> "+str(ptTotal)+" tomadas fêmeas RJ-45 "+catRede+";\n"
        "  -> "+str(ptTelecom)+" espelhos 4\"x2\" furação dupla;\n"
        "  -> "+str(ptRede)+" espelhos 4\"x2\" furação simples;")
if ptRede != 0:
    print("  -> "+str(ptTotal-(ptCFTV+ptVoz))+" patch cords 3m (rede)-"+catRede+";")
if ptCFTV != 0:
    print("  -> "+str(ptCFTV)+" patch cords 1m (CFTV)-"+catRede+";")
if ptVoz != 0:
    print("  -> "+str(ptVoz)+" patch cords 3m (Voz)-"+catRede+";")
print("  -> "+str(ptTelecom+ptTotal)+" etiquetas ("+str(ptTelecom)+" p/ espelho e "+str(ptTotal)+" p/ tomada):")


print("\nMalha Horizontal: \n"
        "  -> "+str(ptTotal*tamMedio)+"m cabo UTP "+catRede+" ("+str(ptTotal)+" de "+str(tamMedio)+"m);\n"
        "  -> "+str(2*ptTotal)+" etiquetas;")

print("\nSala de Telecom: \n")
if tipoRack == 0:
    print("  -> "+str(qtdRack)+" racks abertos de "+str(tamRack)+"U;")
if tipoRack == 1:
    print("  -> "+str(qtdRack)+" racks fechados de "+str(tamRack)+"U;")
print("  -> "+str(math.ceil((ptTotal)/24))+" patch panels "+catRede+";\n"
        "  -> "+str(math.ceil((ptTotal)/24))+" stwitches;\n"
        "  -> "+str(2*math.ceil((ptTotal)/24))+" organizadores de cabo frontal;\n"
        "  -> "+str(qtdRack)+" bandejas;")
if tipoRack == 0:
    print("  -> "+str(qtdRack)+" organizadores laterais;")
if tipoRack == 1:
    print("  -> "+str(qtdRack)+" exaustores;")
if ptRede != 0:
    print("  -> "+str(ptTotal-(ptCFTV+ptVoz))+" patch cable 2,5m (azul)-"+catRede+";")
if ptCFTV != 0:
    print("  -> "+str(ptCFTV)+" patch cords 2,5m (vermelho)-"+catRede+";")
if ptVoz != 0:
    print("  -> "+str(ptVoz)+" patch cords 2,5m (amarelo)-"+catRede+";")

print("\nMiscelânea: \n"
        "  -> "+str(4*(tamRack*qtdRack))+" porcas-gaiola;\n"
        "  -> "+str(24*(math.ceil((ptTotal)/24)))+" etiqutas p/ patch panel;\n"
        "  -> "+str(2*ptTotal)+" etiqutas p/ patch cord;\n"
        "  -> "+str(qtdRack)+" pacotes de abracadeira de plastico;\n"
        "  -> "+str(3*qtdRack)+"m de abracadeira de velcro;")

print("\nObrigado por usar a Lista de Convidados, até a próxima!")
