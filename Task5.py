#Write a program which will ask for two numbers from a user.
#Then offer a menu to the user giving them a choice of operator:
#e.g. –Enter “a” if you want to add“b” if you want to subtract
#Include +, -, /, *, ** square (to the power of).
#Once the user has selected which operator they wish to use, perform the calculation

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
# a = num1 + num2
print ("Thanks you have entered " + str(num1) + " for your first number and " + str(num2) + " for your second number")
print ("Now choose which operation you would like to perform")
print ("a for +, b for -, c for *, d for //, e for **")
choice = input ("pick a letter representing the operation you wish to perform ")
print ("you picked " + choice + ", here's your answer")
if choice == "a":
    print(num1 + num2)
elif choice == "b":
    print( num1 + num2)
elif choice == "c":
    print(num1 * num2)
elif choice == "d":
    print(num1 // num2)
elif choice == "e":
    print(num1 ** num2)