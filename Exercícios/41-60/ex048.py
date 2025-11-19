from time import sleep
n = 0
while True:
    n = int(input("Tabuada: "))
    if (n==0 or n<0):
        print(f"Saindo do programa", end=".")
        sleep(0.5)
        print(end=".")
        sleep(0.5)
        print(end=".")
        break
    else:
        for c in range(1,11):
            print(f"{n} X {c} = {n*c}")
            print()