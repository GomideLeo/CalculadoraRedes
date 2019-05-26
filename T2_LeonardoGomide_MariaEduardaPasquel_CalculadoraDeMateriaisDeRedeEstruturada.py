



print("Digite o numero de pontos de telecom:")
while True:
    try:
        ptTelecom = int(input())
        break
    except ValueError:
        print("Digite um numero inteiro:")
