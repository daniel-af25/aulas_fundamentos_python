laliga = ("Real Madrid", "Barcelona", "Villareal", "Real Betis",
          "Atletico Madrid", "Sevilla", "Elche", "Athletic Club",
          "Espanyol", "Alaves", "Getafe", "Osanuna", "Levante",
          "Rayo Vallecano", "Valencia", "Celta Vigo", "Real Oviedo",
          "Girona", "Real Sociedad", "Real Mallorca", "Las Palmas")


teste = False
for c in range(0, 4):
    print(f"{c+1}º Classificado - {laliga[c]}")
print()
for c in range(19, 15, -1):
    print(f"{c+1}º Classificado - {laliga[c]}")
print()

print("LaLiga por ordem alfabética:")
for equipa in sorted(laliga):
    print(f"\t {equipa}")

print()
for c in range(0,len(laliga)):
    if (laliga[c] == "Las Palmas"):
        print(f"Las Palmas -> {c}º lugar")
        teste = True
print()

if(teste == False):
    print("Las Palmas não estã na primeira divisão.")