from time import sleep

idade = ""
altura = ""
peso = ""

while True:
    if (idade == "V" or idade == "F"):
        break
    else:
        idade = input("Qual a tua idade (V/F)?\n--> ").upper().strip()
while True:
    if (altura == "V" or altura == "F"):
        break
    else:
        altura = input("Qual a tua altura (V/F)?\n--> ").upper().strip()
while True:
    if (peso == "V" or peso == "F"):
        break
    else:
        peso = input("Qual o teu peso(V/F)?\n--> ").upper().strip()
