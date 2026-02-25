define_password = str(input("Set a password: "))
attempts = 3
while attempts > 0:
    confirm_password = str(input("Confirm youe password: "))
    if confirm_password == define_password:
        print("Correct password")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print (f"incorrect password. Try again! \nYou still have {attempts} attempts")
        else:
            print ("You have used all your attempts")
