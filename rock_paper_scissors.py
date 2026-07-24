import random

player = int(input("Escolha: \n1) Pedra \n2)Papel \n3) Tesoura \n"))
comp = random.randint(1, 3)
choice_p = ""

if(player == 1):
    print("Você escolheu: Pedra")
elif(player == 2):
    print("Você escolheu: Papel")
elif(player == 3):
    print("Você escolheu: Tesoura")
else:
    print("Número inválido.")
    exit()


if(comp == 1):
    print("Seu adversário escolheu: Pedra")
elif(comp == 2):
    print("Seu adversário escolheu: Papel")
else:
    print("Seu Adversário escolheu: Tesoura")

if(player == 1 and comp == 1):
    print("EMPATE!")
elif(player == 1 and comp == 2):
    print("Você perdeu.")
elif(player == 1 and comp == 3):
    print("Você venceu")
elif(player == 2 and comp == 1):
    print("Você venceu")
elif(player == 2 and comp == 2):
    print("EMPATE!")
elif(player == 2 and comp == 3):
    print("Você perdeu.")
elif(player == 3 and comp == 1):
    print("Você perdeu.")
elif(player == 3 and comp == 2):
    print("Você venceu")
else:
    print("EMPATE!")

