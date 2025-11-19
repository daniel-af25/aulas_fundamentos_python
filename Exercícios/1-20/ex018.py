from time import sleep #Importa aoenas a funçao time da biblioteca sleep, e deixa utilizar diretemanete sem colocar time. antes
#Se quisesse podia importar a biblioteca inteira atraves do import time mas o script ficaria mais pesado e teria de colocar time. antes da funçao em questao

qtkm = float(input("Qual a quantidade de km percorridos pelo carro alugado?\n --> "))
sleep(0.5)
qtdias = int(input("Qual a quantidade de dias que o mesmo foi alugado?\n --> "))
taxadia = 60
taxakm = 0.456
sleep(0.5)
print()
print("A calcular custos", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".")
print("A quantidade que deve pagar pelo carro alugado é a seguinte:", float((qtkm*taxakm) + (qtdias*taxadia)), "€.")