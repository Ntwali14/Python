print("******LOGIN******")
user = input("username: ")
pwd = input("password: ")
if user == "Arm":
    if pwd == "1234":
        print("Welcome in this bih")
    else:
        print("Invalid password")
else:
    print("Invalid username")