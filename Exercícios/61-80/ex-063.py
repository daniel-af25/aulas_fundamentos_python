'''
Cria um programa que crie palpites para o Euromilhões.
O programa deve perguntar quantas chaves serão guardadas
e deve sortear aleatoriamente 5 números de 1 a 50 [sem repetir]
e 2 estrelas de 1 a 12 [sem repetir].
Cada sorteio deve ser guardado numa lista composto
'''



from time import sleep
from random import randint


print("=_=_=_= Gerador de Chaves EUROMILHÕES =_=_=_=_=\n")
opcao = 0
num = 0
chave = list()
numeros = list()
estrelas = list()
while (opcao != 2):
    print("[ 1 ] - Gerar Chave Euromilhões")
    print("[ 2 ] - Sair do Programa\n")
    opcao = int(input("Escolhe uma opção:\n--> "))
    print()
    match(opcao):
        case 1:
               while(len(numeros) < 5):
                   num = randint(1, 50)
                   if (num in numeros):
                       while(num in numeros):
                            num = randint(1, 50)
                   else:
                       numeros.append(num)
               while (len(estrelas) < 2):
                   num = randint(1, 12)
                   if (num in estrelas):
                       while (num in estrelas):
                           num = randint(1, 12)
                     estrelas.append(num)
               chave.append(numeros[:])
               chave.append(estrelas[:])

        case 2:
            print("Saindo do programa",end=".")
            sleep(0.5)
            print(end=".")
            sleep(0.5)
            print(end=".")

