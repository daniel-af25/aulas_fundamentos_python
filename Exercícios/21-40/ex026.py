nota1 = float(input("INSIRA A PRIMEIRA NOTA:\n --> "))
nota2 = float(input("INSIRA A SEGUNDA NOTA:\n --> "))
nota3 = float(input("INSIRA A TERCEIRA NOTA:\n --> "))
nota4 = float(input("INSIRA A QUARTA NOTA:\n --> "))
nota5 = float(input("INSIRA A QUINTA NOTA:\n --> "))

if ((nota1+nota2+nota3+nota4+nota5)/5 >= 9.5):
    print(f"PASSADO , MEDIA: {(nota1+nota2+nota3+nota4+nota5)/5}")
elif ((nota1+nota2+nota3+nota4+nota5)/5 > 8 and (nota1+nota2+nota3+nota4+nota5)/5 <9.5 ):
    print(f"EM RECUPERAÇAO , MEDIA: {(nota1 + nota2 + nota3 + nota4 + nota5) / 5}")
elif ((nota1+nota2+nota3+nota4+nota5)/5 < 8 ):
    print(f"REPROVADO , MEDIA: {(nota1 + nota2 + nota3 + nota4 + nota5) / 5}")
else:
    print("ERRO!")
print()
print("FIM DO PROGRAMA.")


