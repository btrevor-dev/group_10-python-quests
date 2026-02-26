#!/usr/bin/python3

correct_password = "magic123"

user_password = input("Enter the password: ")

if user_password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")
