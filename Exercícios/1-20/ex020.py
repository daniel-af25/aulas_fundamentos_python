nomec = input("Digite o seu nome completo.\n--> ").strip()

print(nomec.upper())
print(nomec.lower())
print(nomec.replace(" ", ""))
print(len(nomec.replace(" ", "")))
print(len(nomec[:nomec.find(" ")]))