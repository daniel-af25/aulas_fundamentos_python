soma = 0
contador = 0
print("Para parar digite 0 ! \n")
num = 1
while True:
    if(num == 0):
        print(f"Soma total: {soma}\n")
        print(f"Total numeros: {contador-1}\n")
        break
    else:
        num = int(input("Insira um numero:\n --> "))
        soma += num
        contador += 1