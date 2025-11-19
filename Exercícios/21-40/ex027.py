num_1 = int(input("Insira o primeiro numero:\n --> "))
num_2 = int(input("Insira o segundo numero:\n --> "))

if (num_1>num_2):
    print(f"{num_1} > {num_2}")
elif (num_2>num_1):
    print(f"{num_2} > {num_1}")
elif (num_2==num_2):
    print(f"{num_2} = {num_1}")
else:
    print("ERRO!")
print()
print("FIM DO PROGRAMA!")
