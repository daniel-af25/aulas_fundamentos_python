tuple = ("The Witcher III", "29.99€", "Hollow Knight: Silk Song", "19.50€",
         "Monster Hunter Wilds", "69.99€", "Stardew Valley", "13.99€",
         "DRAGON QUEST XI S: Echoes of an Elusive Age", "39.99€", "Digimon Story Time Stranger"
         , "69.99€", "Ghost of Tsushima Director's Cut", "40.19€", "God Of War", "49.99€" )
space = " "
price = "price"
symbol = "-"
symbol2 = "."
print("               =_=_=_=_=_=_= LIST OF PRICES =_=_=_=_=_=_=")
print(symbol * 80)
print("GAME",end=":")
print(space*69, end="PRICE:")
print()
print(symbol * 80)
for c in range(0, len(tuple),2):
    print(f"{tuple[c]}", symbol2 * (73-len(tuple[c])), end="")
    print(tuple[c+1])