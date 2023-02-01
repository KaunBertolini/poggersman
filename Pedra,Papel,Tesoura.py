from os import system
import random
import time


system("cls")

print('''

   ###############################

           Bem vindo ao
    PEDRA, PAPEL ou TESOURA!


   ###############################
''')

print('''

      MENU
  ############
   PEDRA - [0]
   PAPEL - [1]
   TESOURA - [2]
 ##############

''')

PEDRA = 0
PAPEL = 1
TESOURA = 2


jogada = int(input("Digite a sua jogada: "))
jogadapc = random.randint(0, 2)

time.sleep(1)
print("Pedra...")
time.sleep(1)
print("Papel...")
time.sleep(1)
print("Tesoura!!!")

time.sleep(2)
system("cls")

if jogadapc == 0:
    print("O COMPUTADOR ESCOLHEU PEDRA!")
    if jogada == 0:
        print("VOCÊ JOGOU PEDRA!")
        print("EMPATE!")
    elif jogada == 1:
        print("VOCÊ JOGOU PAPEL!")
        print("VOCÊ GANHOU!")
    elif jogada == 2:
        print("VOCÊ JOGOU TESOURA!")
        print("O COMPUTADOR GANHOU!")
    else:
        print("Jogada inválida inválida")

elif jogadapc == 1:
   print("O COMPUTADOR JOGOU PAPEL!")
   if jogada == 0:
    print("VOCÊ JOGOU PEDRA!")
    print("O COMPUTADOR GANHOU!")
   elif jogada == 1:
        print("VOCÊ JOGOU PAPEL!")
        print("EMPATE!")
   elif jogada == 2:
     print("VOCÊ JOGOU TESOURA!")
     print("VOCÊ GANHOU!")
   else:
        print("Jogada inválida")

elif jogadapc == 2:
    print("O COMPUTADOR JOGOU TESOURA!")
    if jogada == 0:
      print("VOCÊ JOGOU PEDRA!")
      print("VOCÊ GANHOU!")
    elif jogada == 1:
        print("VOCÊ JOGOU PAPEL")
        print("O COMPUTADOR GANHOU!")
    elif jogada == 2:
        print("VOCÊ JOGOU TESOURA")
        print("EMPATE!")
    else:
        print("Jogada inválida")