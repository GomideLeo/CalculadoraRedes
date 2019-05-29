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
        while (True):
            ptRede = getPt("conexão de rede (simples)")
            if ptRede > 2*ptTelecom:
                print ("Existem mais pontos que portas, digite um novo numero")
            else:
                break
        if ptRede !=-1:
            while (True):
                ptCFTV = getPt("CFTV IP")
                if ptRede+ptCFTV > 2*ptTelecom:
                    print ("Existem mais pontos que portas, digite um novo numero")
                else:
                    break
            if ptCFTV !=-1:
                while (True):
                    ptVoz = getPt("voz sobe IP")
                    if ptRede+ptCFTV+ptVoz > 2*ptTelecom:
                        print ("Existem mais pontos que portas, digite um novo numero")
                    else:
                        break
                if ptVoz !=-1:
                    break

ptTotal = ptRede+ptCFTV+ptVoz

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


if 2*ptTelecom-(ptTotal)>0:
    print("\nVocê tem "+str(2*ptTelecom-(ptTotal))+" tomadas inutilizadas")

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
        "  -> "+str(ptRede+ptCFTV+ptVoz)+" tomadas fêmeas RJ-45 ("+str(ptRede+ptCFTV)+" "+catRede+" e "+str(ptVoz)+" cat 5e);\n"
        "  -> "+str(ptTelecom)+" espelhos 4\"x2\";")
if ptRede != 0:
    print("  -> "+str(ptRede)+" patch cords (rede)-"+catRede)+";"
if ptCFTV != 0:
    print("  -> "+str(ptCFTV)+" patch cords (CFTV)-"+catRede+";")
if ptVoz != 0:
    print("  -> "+str(ptVoz)+" patch cords (Voz)-cat 5e;")
print("  -> "+str(ptTelecom+ptTotal)+" etiquetas ("+str(ptTelecom)+" p/ espelho e "+str(ptTotal)+" p/ tomada):")

if catRede == "cat 5e":
    print("\nMalha Horizontal: \n"
            "  -> "+str(ptTotal)+" Cabos UTP  cat 5e;\n"
            "  -> "+str(2*(ptTotal))+" etiqutas;")
else:
    print("\nMalha Horizontal: \n"
            "  -> "+str(ptTotal)+" Cabos UTP ("+str(ptRede+ptCFTV)+" "+catRede+" e "+str(ptVoz)+" cat 5e);\n"
            "  -> "+str(2*(ptTotal))+" etiquetas;")

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
    print("  -> "+str(ptRede)+" patch cable (azul)-"+catRede+";")
if ptCFTV != 0:
    print("  -> "+str(ptCFTV)+" patch cords (vermelho)-"+catRede+";")
if ptVoz != 0:
    print("  -> "+str(ptVoz)+" patch cords (amarelo)-"+catRede+";")

print("\nMiscelânea: \n"
        "  -> "+str(4*(tamRack*qtdRack))+" porcas-gaiola;\n"
        "  -> "+str(24*(math.ceil((ptTotal)/24)))+" etiqutas p/ patch panel;\n"
        "  -> "+str(2*ptTotal)+" etiqutas p/ patch panel;\n"
        "  -> Abracadeiras de plastico;\n"
        "  -> Abracadeiras de velcro;")

print("\nObrigado por usar a Lista de Convidados, até a próxima!")
