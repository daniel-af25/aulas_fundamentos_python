string = input("Insira o seu primeiro e ultimo nome.\n--> ").strip()
print(f"Olá {string} o seu registo está completo.")
string2 = (string[0]).lower()
string3 = (string[string.find(" "):]).lower()
print(f"O seu email é {string2.rstrip()}.{string3.lstrip()}@empresa.pt")


