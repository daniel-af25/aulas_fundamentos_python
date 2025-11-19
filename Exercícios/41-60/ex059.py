nums = list()
numsp = list()
numsi = list()
c = 0
print("Para parar digite 0.")
print()
while True:
    c += 1
    num = int(input(f"Insira o {c} número: "))
    if(num == 0):
        break
    else:
        nums.append(num)
        if(num % 2 == 0):
            numsp.append(num)
        else:
            numsi.append(num)
print()
print(f"Lista Original: {nums}\n")
print(f"Lista Par: {numsp}\n")
print(f"Lista Impar: {numsi}\n")