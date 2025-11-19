while True:
    numero = int(input("Insira um numero 0-20.\n--> "))
    if (numero > 20 or numero < 0):
        print("Numero Inválido!\n")
        continue
    else:
        break
numeros = ("Zero", "Um", "Dois", "Três", "Quatro",
           "Cinco", "Seis", "Sete", "Oito", "Nove",
           "Dez", "Onze", "Doze", "Treze", "Quatorze",
           "Quinze", "Dezasseis", "Dezassete", "Dezoito",
           "Dezanove", "Vinte")
print()
print(f"{numeros[numero]}")




