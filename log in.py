import json


def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = {"name": name, "email": email, "password": password}
    with open("users.txt", "a") as file:
        file.write(json.dumps(user) + "\n")
    print("Registration successful!")


def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as file:
        for line in file:
            user = json.loads(line)
            if user["email"] == email and user["password"] == password:
                print("Login successful!")
                return
    print("Invalid email or password.")


while True:
    choice = input("Enter '1' to register, '2' to login, or '3' to exit: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")