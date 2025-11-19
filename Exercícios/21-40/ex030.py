print("-- BEM VINDO AO JOGO PEDRA/PAPEL/TESOURA ---")
decisao_user = input("ESCOLHA PEDRA / PAPEL / TESOURA\n --> ").strip().lower()
escolhas = ["pedra", "papel", "tesoura"]
decisao_pc = random.choice(escolhas)
if (decisao_user == "pedra" and decisao_pc == "papel"):
    print(f"PERDESTE! O PC UTILIZOU {decisao_pc}! PAPEL GANHA A PEDRA!\n")
elif (decisao_user == "pedra" and decisao_pc == "tesoura"):
    print(f"GANHASTE! O PC UTILIZOU {decisao_pc}! PEDRA GANHA A TESOURA!\n")
elif (decisao_user == "pedra" and decisao_pc == "pedra"):
    print(f"EMPATASTE! O PC UTILIZOU {decisao_pc}! PEDRA EMPATA COM PEDRA!\n")
elif (decisao_user == "papel" and decisao_pc == "tesoura"):
    print(f"PERDESTE! O PC UTILIZOU {decisao_pc}! TESOURA GANHA A PAPEL!\n")
elif (decisao_user == "papel" and decisao_pc == "pedra"):
    print(f"GANHASTE! O PC UTILIZOU {decisao_pc}! PAPEL GANHA A PEDRA!\n")
elif (decisao_user == "papel" and decisao_pc == "papel"):
    print(f"EMPATASTE! O PC UTILIZOU {decisao_pc}!\n")
elif (decisao_user == "tesoura" and decisao_pc == "pedra"):
    print(f"PERDESTE! O PC UTILIZOU {decisao_pc}! PEDRA GANHA A TESOURA!\n")
elif (decisao_user == "tesoura" and decisao_pc == "papel"):
    print(f"GANHASTE! O PC UTILIZOU {decisao_pc}! TESOURA GANHA A PAPEL!\n")
elif (decisao_user == "tesoura" and decisao_pc == "tesoura"):
    print(f"EMPATASTE! O PC UTILIZOU {decisao_pc}!\n")
print("OBRIGADO POR UTILIZARES O MEU PROGRAMA.")