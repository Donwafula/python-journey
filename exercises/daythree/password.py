# Program to prompt user for password

password = input("Enter password: ")

while password != "python":
    password = input("Wrong password. Re-enter: ")

print("Access granted")
