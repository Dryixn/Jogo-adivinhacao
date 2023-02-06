print("=" * 80)
import random
from time import sleep
pensando = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = random.choice(pensando)
r = 'v'
palpites = 0
while r != n:
    r = int(input("Qual o número que o computador está pensando de 0 a 10? "))
    palpites += 1
    sleep(2)
    if r < n:
        print("Você errou, tente novmente um número maior.")
    if r > n:
        print("Você errou, tente novamente um número menor.")
    if r == n:
        print("Você acertou!")
print("Você precisou de {} palpites para acertar.".format(palpites))
print("FIM")
print("=" * 80)
