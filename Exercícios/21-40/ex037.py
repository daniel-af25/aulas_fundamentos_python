numero = int(input("Insira um numero.\n---> "))
contador = 0
for c in range (1,numero):
    if (numero % c == 0):
        contador += 1
print()
if (contador >= 3):
    print(f"O numero {numero} não é um numero primo!")
else:
    print(f"O numero {numero} é um numero primo!")