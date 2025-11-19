string = input("Insira uma frase.\n--> ")

print(string.count("A"))
stringc = string[::-1]
print(f"A letra a aparece a primeira vez na posição {string.find("a")+1} e aparece a ultima vez na posiçao {stringc.find("a")+1}.")