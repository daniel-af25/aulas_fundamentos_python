expressao = input("Digite uma expressao matemática: ")

if (expressao.count("(") == expressao.count(")")):
    print(f"Expressão Correta.")
else:
    print(f"Expressão Incorreta.")