from time import sleep

print("Welcome to the IMC Calculator made in Python!\n")
sleep(0.5)
print("Please enter the following values in Kilograms/Meters:\n")

user_weight = float(input("Weight(KG): "))
user_height = float(input("Height(m): "))
print()
print("Calculating", end=".")
sleep(0.3)
print(end=".")
sleep(0.3)
print(end=".")
imc_user = float((user_weight)/(user_height*user_height))
print()
if (imc_user < 18.5):
    print(f"{imc_user:.2f} - Belown normal weight, better starting eating more!\n")
elif (imc_user > 18.5 and imc_user < 24.5):
    print(f"{imc_user:.2f} - Normal weight, you are doing good!\n")
elif (imc_user > 25.5 and imc_user < 29.9):
    print(f"{imc_user:.2f} - Overweight, start watching what you are eating!\n")
elif (imc_user > 30.0 and imc_user < 34.9):
    print(f"{imc_user:.2f} - Obesity level 1, maybe go to a nutricionist!\n")
elif (imc_user > 35.0 and imc_user < 39.9):
    print(f"{imc_user:.2f} - Obesity level 2, go tou your family doctor to get you recommendations!\n")
elif (imc_user > 40.0):
    print(f"{imc_user:.2f} - Obesity level 3 / Morbid Obesity, go to your local hospital ASAP, you are in for a ride!!!!!\n")

print("Closing program", end=".")
sleep(0.3)
print(end=".")
sleep(0.3)
print(end=".")
