


def getPt(str):
    print("Digite o numero de pontos de "+str+"(-1 para corrigir valores):")
    while True:
        try:
            return int(input())
            break
        except ValueError:
            print("Digite um numero inteiro:")

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
            print("Digite um numero inteiro:")
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

print("\nO rack será aberto ou fechado?"
    "\n 0 para aberto"
    "\n 1 para fechado")
while True:
    pass
    try:
        tipoRack = int(input())
        break
    except ValueError:
        print("Digite um numero inteiro:")

if 2*ptTelecom-(ptRede+ptCFTV+ptVoz)>0:
    print("\nExistem "+str(2*ptTelecom-(ptRede+ptCFTV+ptVoz))+" tomadas inutilizadas")

if catRede == "cat 5e":
    print("\nÁrea de Trabalho: \n"
            "  -> "+str(ptRede+ptCFTV+ptVoz)+" tomadas fêmeas RJ-45 ("+str(ptRede+ptCFTV+ptVoz)+" cat 5e)\n"
            "  -> "+str(ptTelecom)+" espelhos 4\"x2\"")
    if ptRede != 0:
        print("  -> "+str(ptRede)+" patch cord (rede)- "+catRede)
    if ptCFTV != 0:
        print("  -> "+str(ptCFTV)+" patch cord (CFTV)- "+catRede)
    if ptVoz != 0:
        print("  -> "+str(ptVoz)+" patch cord (Voz)- cat 5e")
    print("  -> "+str(ptTelecom+ptRede+ptCFTV+ptVoz)+" etiquetas ("+str(ptTelecom)+" p/ espelho e "+str(ptRede+ptCFTV+ptVoz)+" p/ tomada)")

    print("\nMalha Horizontal: \n"
            "  -> "+str(ptRede+ptCFTV+ptVoz)+" Cabos UTP ("+str(ptRede+ptCFTV+ptVoz)+" cat 5e)\n"
            "  -> "+str(2*(ptRede+ptCFTV+ptVoz))+" etiquetas")
else:
    print("\nÁrea de Trabalho: \n"
            "  -> "+str(ptRede+ptCFTV+ptVoz)+" tomadas fêmeas RJ-45 ("+str(ptRede+ptCFTV)+" "+catRede+" e "+str(ptVoz)+" cat 5e)\n"
            "  -> "+str(ptTelecom)+" espelhos 4\"x2\"")
    if ptRede != 0:
        print("  -> "+str(ptRede)+" patch cord (rede)- "+catRede)
    if ptCFTV != 0:
        print("  -> "+str(ptCFTV)+" patch cord (CFTV)- "+catRede)
    if ptVoz != 0:
        print("  -> "+str(ptVoz)+" patch cord (Voz)-cat 5e")
    print("  -> "+str(ptTelecom+ptRede+ptCFTV+ptVoz)+" etiquetas ("+str(ptTelecom)+" p/ espelho e "+str(ptRede+ptCFTV+ptVoz)+" p/ tomada)")

    print("\nMalha Horizontal: \n"
            "  -> "+str(ptRede+ptCFTV+ptVoz)+" Cabos UTP ("+str(ptRede+ptCFTV)+" "+catRede+" e "+str(ptVoz)+" cat 5e)\n"
            "  -> "+str(2*(ptRede+ptCFTV+ptVoz))+" etiquetas")
