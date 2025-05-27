print("****Login****")
user = input("Username: ")
pwd = input("Password: ")
if user == "nit":
    if pwd == "nit123":
        print("Welcome")
    else:
        print("Invalid password")
else:
    print("Invalid username")