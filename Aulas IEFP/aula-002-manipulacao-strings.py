string = "Python é Poderoso"
teste = "Afonso"

#Fatiamento de Strings / String Slicer
print(string[7]) # é
print(string[-1]) # ultimo caracter
print(string[0:6]) # palavra python
print(string[:6]) # palavra python
print(string[9:]) # palavra poderoso
print(string[::2]) # inicio ao fim de 2 em 2
print(string[::-1]) # mostra a string ao contrario

#Analise de String / String Analisys
print(len(string)) # Tamanho da String
print(string.count("o")) # Quantas vezes aparece o o
print(teste.count("o")) # Mais um exemplo
print("Python" in string) # Devolve true ou false
print("python" in string) # Devolve true ou false
print(string.find("e")) # Devolve a posiçao do solicitado
print(string.find("olé")) # nao encontra e devolve -1
print(string.startswith("Python")) # devolve true ou false
print(string.endswith("Poderoso")) # devolve true ou false



#Transformação de String / String Transfiguration
string = input("Digite uma frase\n--> ").strip().lower() # Boa pratica ao ler strings incluir sempre .strip() e .lower()

print(len(string))
print(len(string.strip()))
print(len(string))
print(len(string.rstrip()))
print(string.lower())
print(string.upper())
print(len(string.replace(" ", "")))