#Smart Calculator :
# Python Project #1 – Smart Calculator

# Concepts you'll learn:

# Variables
# Data types
# Input/Output
# Functions
# if-else
# while loop
# Exception handling
# Modular programming



# while True:
#     try:
#         n=(int(input("enter the number - ")))
#         m=(int(input("enter second number - ")))
#         operation=input("Enter operation to be perform ")
#         op = ["+", "-", "*", "/"]
        
#         if operation == "+":
#             print(f"the sum of two number is - {n+m}")
#         elif operation == "-":
#                 print(f"the subtaction of two number is - {n-m} ")
#         elif operation =="*":
#                 print(f"the multiplication of two number is - {n*m} ")
#         elif operation == "/":
#             print(f"the division of two number is - {n/m} ")
#         elif operation not in op  :
#             print("input is not Valid! ")
#     except ValueError:
#         print("Enter Valid integer")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")


#     user = input("Do you want to continue? - \n1.Yes " "\n2.No \nEnter your choice: ")

#     if user == "1":
#         continue

#     elif user == "2":
#         print("Calculator closed")
#         break

#     else:
#         print("Given input is not acceptable")
      


#Implementing Dictionary :
while True:
    try:
        n=(int(input("enter the number - ")))
        m=(int(input("enter second number - ")))
        choice = input("Enter your choice: :\n1.Adiition  \n2.Substraction \n3.Multiplication \n4.Division \n5.Modulus \n6.floor Division \n7.Square \n")

        operation= {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/",
                "5": "%",
                "6": "//",
                "7": "**"
            }

        if choice not in operation:
            print("Invalid choice!")
            continue

        op = operation[choice]
   


        if op == "+":
            print(f"The sum of two numbers is = {n + m}")

        elif op == "-":
            print(f"The subtraction of two numbers is =  {n - m}")

        elif op == "*":
            print(f"The multiplication of two numbers is = {n * m}")

        elif op == "/":
            print(f"The division of two numbers is = {n / m}")

        elif op == "%":
            print(f"The modulus is = {n % m}")

        elif op == "//":
            print(f"The floor division is = {n // m}")

        elif op == "**":
            print(f"The result of power is = {n ** m}")

        # elif choice not in op:
        #     print("input is not Valid! ")

    except ValueError:
        print("Enter Valid integer")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    user = input("Do you want to continue?\n1. Yes\n2. No\nEnter your choice: ").strip()

    if user == "1":
        continue

    elif user == "2":
        print("Calculator closed")
        break

    else:
        print("Given input is not acceptable")
