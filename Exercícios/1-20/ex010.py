print("--- Calculadora ---")
print(" [ 1 ] - Tabuada")
print(" [ 2 ] - Calculadora")
print(" [ 3 ] - Fatorial")
print(" [ 4 ] - Números Primos\n")


opçao_utilizador = int(input("Escolha uma opção.\n --> "))
print()
if opçao_utilizador == 1:
    opçao = "Tabuada"
elif opçao_utilizador == 2:
    opçao = "Calculadora"
elif opçao_utilizador == 3:
    opçao = "Fatorial"
elif opçao_utilizador == 4:
    opçao = "Números Primos"
else:
    print("Opção Inválida! Por favor reinicie o programa.")

print("Escolheste a opção", opçao_utilizador,opçao)