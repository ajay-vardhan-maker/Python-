email = input("Enter email ID: ")

if "@" in email and "." in email:
    print("Valid email ID")
else:
    print("Invalid email ID")
