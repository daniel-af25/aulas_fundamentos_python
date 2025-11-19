from time import sleep

print("Welcome to the IEFP Company!\n")
sleep(0.5)
print(f"You don't have an account, please register one.")
sleep(0.5)
name_user = input("Username: ").strip()
email_user = input("Email: ").strip()
test1_email = email_user.find("@")
test2_email = email_user.find(".")
if (test1_email == -1 or test2_email == -1):
    print()
    print("Invalid Email! Please register a valid email.")
    email = input("Email: ").strip()
else:
    print("Valid Email!\n")
passw_user = input("Password: ").strip()
passwv_user = input("Confirm Password: ").strip()
if (passwv_user != passw_user):
    print("The passwords aren't the same.\n")
    passw_user = input("Password: ").strip()
    passwv_user = input("Confirm Password: ").strip()
    print("Valid Password!\n")
else:
    print("Valid Password!\n")
print("Registering Acount", end=".")
sleep(0.5)
print(end=".")
sleep(0.5)
print(end=".")
print()
print("Account successfully created!\n")
sleep(1)
print("[ 1 ] - Login")
print("[ 2 ] - Sair\n")
option_user = int(input("Choose an option.\n --> "))
print()
if (option_user == 1):
    attempt_name_user = input("Username: ")
    attempt_passw_user = input("Password: ")
    if (name_user != attempt_name_user or passw_user != attempt_passw_user):
        print("Invalid Login!")
        sleep(1)
        print()
        attempt_name_user = input("Username: ")
        attempt_passw_user = input("Password: ")
        if (attempt_name_user != name_user or attempt_passw_user != passw_user):
            print("You are blocked from this site! 1+ Failed entry.")
        else:
            print()
            print("Successfuly logged in!")
    else:
        print()
        print("Successfuly logged in!")
elif(option_user == 2):
    print("Closing site", end=".")
    sleep(0.5)
    print(end=".")
    sleep(0.5)
    print(end=".")
else:
    print("Not an available option!\n")
    print("Closing site", end=".")
    sleep(0.5)
    print(end=".")
    sleep(0.5)
    print(end=".")


#OBS: Validação apenas feitas com uma tentativa extra visto apenas ser possivel utilizar conhecimentos adquiridos ate ao momento durante a aula.
