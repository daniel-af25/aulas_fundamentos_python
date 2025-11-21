from datetime import datetime


current_year = datetime.now().year
credito = dict()



credito["Nome"] = input("Qual o seu nome? ")
credito["Nascimento"] = int(input("Qual o seu ano de nascimento? "))
credito["Rendimentos_Mensais"] = int(input("Rendimentos Mensais (€)? "))
while(credito["Rendimentos_Mensais"] <= 0):
    credito["Rendimentos_Mensais"] = int(input("Rendimentos Mensais (€)? "))
credito["Despesas_Mensais"] = int(input("Despesas Mensais (€)? "))
while(credito["Despesas_Mensais"] <= 0):
    credito["Despesas_Mensais"] = int(input("Despesas Mensais (€)? "))
credito["Montante_Credito"] = int(input("Montante Crédito (€)? "))
while(credito["Montante_Credito"] <= 0):
    credito["Montante_Credito"] = int(input("Montante_Credito(€)? "))
credito["Prazo_Anos"] = int(input("Prazo Anos? "))
while(credito["Prazo_Anos"] <= 0):
    credito["Prazo_Anos"] = int(input("Prazo Anos(€)? "))
print("\n\n\n\n\n\n")
credito["Idade"] = current_year - credito["Nascimento"]
credito["Remanescente"] = credito["Rendimentos_Mensais"] - credito ["Despesas_Mensais"]
credito["Montante"] =   (credito["Montante_Credito"] / (credito["Prazo_Anos"] * 12))
if (credito["Remanescente"] > credito["Montante"]):
    credito["Situação"] = "Aprovado"
else:
    credito["Situação"] = "Reprovado"

if (credito["Situação"] == "Aprovado"):
    print(f"Parabéns {credito["Nome"]}, com {credito["Idade"]} anos!\n\n O seu crédito foi aprovado.\n {(credito["Montante"]):.2f} / {(credito["Prazo_Anos"] * 12)} Meses")
else:
    print(f"{credito["Nome"]}, infelizmente o seu crédito foi reprovado.")