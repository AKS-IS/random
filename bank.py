name = ""
dob = ""
count= 3
while count != 0:
    if name !="Arpit" and dob !="13112003" and count >= 0:
        name = input("\nEnter first name: ")
        dob = input("\nEnter date of birth of six digits: ")
        count-=1
        if name != "Arpit" and dob != "13112003" and count >= 0:
            print("\nYou have", str(count), "attempts left")
        if count==0:
            print("\nYou have reached your limit.")
            break
    else:
        print("\nWelcome to Swiss Bank")
        balance = '$154376550'
        print("Your account balance is :", balance)
        break



