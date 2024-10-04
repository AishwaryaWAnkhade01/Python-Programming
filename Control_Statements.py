# def user():
#         try:
#             username = input("Enter your username: ")
#             if not username.isalpha():
#                 raise ValueError("Entered invalid input.")
#             return username
#         except ValueError as e:
#             print(e)
#
# username= user()
# print(f"Welcome, {username}!")


# def user():
#       try:
#             username = input("Enter your username: ")
#             if not username.isalpha():
#                   print("ENtered Wrong input")
#       except ValueError:
#             print("User name must contain alphabetic values only")
#       else:
#             print(username)
#
#
# print(user())
#
# count=0
# while(count<3):
#       count=count+1
#       print("Hello Geek")









































# # #List with CRUD operation
# #
# #ZeroDivisionError
#
# try:
#       a=int(input("Enter calue of a : "))
#       b=int(input("ENter value of b : "))
#       res=a/b
# except ValueError:
#       print("You have taken incorrect input type")
# except ZeroDivisionError:
#       print("You cannot divide by zero")
# else:
#       print("Result: ",res)
#
# #Print StackTrace :
#
#































# # list=["jhon" , 101 , 'Mumbai',  30]
# # # print(list)
# # print('Case-1')
# # list.append(990)
# # print(list)
# # print('Case:2')
# # list.insert(2,119)
# # print(list)
# # # delete
# # print('Case-3')
# # list.remove(101)
# # print(list)
# #
# # print("Conversion")
# # print("list to tuple")
# # t=tuple(list)
# # print(t)
# # print("\n")
#
# print("Tuples")
#
# tuple=("Ali" , 110, "Delhi" , 28)
# print(tuple)
# # print('Case-1')
# # tuple.insert(2,300)
# # print(tuple)
# #
# # print('case-2')
# # tuple.pop(110)
# # print(tuple)
#
# print("Conversion")
# print(" tuple list to")
# l=list(tuple)
# print(l)
# print("\n")
#
#
# #set
# print("Sets")
# set={"Max" , 190 , "Banglore", 27}
# print(set)
#
# print('Case-1')
# set.add("India")
# print(set)
#
# print("Case-2")
# set.remove(190)
# print(set)
#
# print("Case-3")
# set.discard(190)
# print(set)
#
#
# print('Case-4')
# set.clear()
# print(set)
#
#
# ##Important methods of sets
# print("Set Method-1 : Union")
#
# set1={"Alice" , "Jhon" , "Peter" , "Collin" , "Katee" , 104 , 102}
# set2={101, 102, 103 , 104, 105 ,"Jhon" , "Alice"}
# print(set1|set2)
# #this method allows to merge the two different sets containing dfiffferent value
# #set does not allow duplicates value
#
#
# print("Method 2: Intersection")
# print(set1^set2)
#
# #using this method set that contain duplicates value does not print it removes
# #the value which is in Set A and Set B only print the unique value from both the set
#
#
# print("method 3 : differecne")
#
# set_1={101,102,103,104,105}
# set_2={103,104,109,108,110}
# print(set_1-set_2)
# print(set_2-set_1)
#
#
# #difference method is a method of set which compare both the sets and present the value from set 1 and set two which are not same
# #it display the value of set 1 which is not present in set 2
# #and vice versa for set 2
#
# #This method allows
#
# print("Method 4 : Symmetric Difference")
# print(set_1.symmetric_difference(set_2))
#
# #symmetric difference  does the same as differece but this time this merge
# #the the two sets into one and display the non duplicate value from both the sets
#
# print("Dictionary")
# #dictionary
# dict={"empid" : 109 ,
#       'name': "James" ,
#       "city":"hyderabad" ,
#       "age":25}
# print(dict)
# print(dict["name"])
# print(dict["city"])
# new=dict.get("name")
# print(new)
# n=dict.items()
# print(n)
#
# m=dict.values()
# print(m)
#
# dict.update({"name": "Ruby" , "age":27}, )
# print(dict)
#
# dict.pop("name")
# print(dict)
#
# dict.keys()
# print(dict)
#
#
#
#
# #
# #
# #
# # lis=[10,20,30,40,50,60,70,80,90,100]
# # print(lis)
# # print("List to tuple")
# # t=tuple(lis)
# # print(t)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # X=int(input())
# # # Y=int(input())
# # # Z=int(input())
# # # n=int(input())
# # # S= [[x,y,z] for x in range[X+1] for y in range[Y+1] for z in range [Z+1] if x+y+z!=n ]
# # # print(S)
# # #
# # #
# # #
# # #
# # # X = int(input())
# # # Y = int(input())
# # # Z = int(input())
# # # n = int(input())
# # #
# # # series = [[x, y, z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x + y + z != n]
# # # print(series)
# # #
# #
# # # n = int(input().strip())
# # # scores = list(map(int, input().strip().split()))
# # #
# # #
# # # unique_scores = set(scores)
# # # sorted_scores = sorted(unique_scores, reverse=True)
# # #
# # # runner_up_score = sorted_scores[1]
# # #
# # #
# # # print(runner_up_score)
# #
# # #List
# #
# # list=["Alice", "New York", 101, "bob", "California", 102]
# # print(list)
# #
# # #Tuple
# #
# # tuple=("Alice", "New York", 101, "bob", 'california', 102)
# # print(tuple)
# #
# # #Set
# # Set = {'empid': 101, 'name': "Ally", 'city': 'sydney', 'age': 30}
# #
# # print(Set)
# #
# # dict={"name":"Jhon",
# #       'empid':440,
# #       'city': "Mumbai",
# #       "age":30}
# #
# #
# #
# #
# #
# # print(list)
# # # lis=[1, 2, 3, 4]
# # # t =tuple(lis)
# # # print(t)
# #
# #
# # # #Tuple to list
# # # tup = (1, 2, 3, 4)
# # # my_list = list(tup)
# # # print(my_list)
# # #
# # # #List to Set Conversion
# # #
# # # my_list = [1, 2, 3, 4, 4]
# # # my_set = set(my_list)
# # # print(my_set)
# # #
# # # #tuple to set
# # # my_tuple = (1, 2, 3, 4, 4)
# # # my_set = set(my_tuple)
# # # print(my_set)
# # #
# # # # Using curly braces
# # # my_dict = {
# # #     "name": "Alice",
# # #     "age": 25,
# # #     "city": "New York"
# # # }
# # #
# # # print(my_dict)
# #
# #
# # # List to Tuple: Converts a mutable list into an immutable tuple.
# # # List to Set: Converts a mutable list into a mutable set, with duplicates removed.
# # # Tuple to Set: Converts an immutable tuple into a mutable set, with duplicates removed.
# # # Duplicates:
# # #
# # # List to Tuple: Preserves all elements, including duplicates.
# # # List to Set: Removes duplicates from the list.
# # # Tuple to Set: Removes duplicates from the tuple.
# # # Order:
# # #
# # # List to Tuple: The order of elements is preserved.
# # # List to Set: The order is not preserved; sets are unordered.
# # # Tuple to Set: The order is not preserved; sets are unordered.
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # # Login Form Logic
# # # #
# # # # username s =["Aishwarya" , "Vidhyanshi"]
# # # # password s =["10123" , "78965"]
# # # # expiry_dat e =[30 ,-1]
# # # #
# # # # def create_account():
# # # #     while True:
# # # #         usernam e =input("Enter a new username: ")
# # # #         if username in usernames:
# # # #             print("Username already exits " "\n" "Please choose a different username" )
# # # #         else:
# # # #             passwor d= int(input("Enter a new password: "))
# # # #             expiry_day s =int(input("Enter the password expiry days : "))
# # # #
# # # #             username.append(username)
# # # #             passwords.append(password)
# # # #             expiry_days.append(expiry_days)
# # # #             print("Account created successfully! ")
# # # #             break
# # # #
# # # # def login_fitness():
# # # #     attempts = 3
# # # #     while attempts >0:
# # # #         username = input("Enter your username : ")
# # # #         password = input("Enter your PIN : ")
# # # #         if username in usernames:
# # # #             index = usernames.index(username)
# # # #             if passwords[index] == password:
# # # #                 if expiry_date[index] > 0:
# # # #                     print("Login Successful! ")
# # # #                     print("Welcome to Your Fitness App ")
# # # #                     return
# # # #                 else:
# # # #                     print("Your password has expired ." "\n" "Please reset Your password.")
# # # #                 break
# # # #             else:
# # # #                 print("Incorrect PIN")
# # # #
# # # #                 attempts -= 1
# # # #                 if attempts > 0:
# # # #                     print(f"You have {attempts} attempts are left.")
# # # #                     break
# # # #                 else:
# # # #                     print("Login Failed.")
# # # #                     print("No attempts left ")
# # # #                     break
# # # #
# # # #
# # # # # #Program 1
# # # # #
# # # # # # total = 0
# # # # # # for i in range(1, 16, 2):
# # # # # #     total += i
# # # # # # print(f"Sum of odd numbers up to 15: {total}")
# # # # #
# # # # # #Program 2
# # # # #
# # # # # # #Skipping  Weekend From the list
# # # # # # days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# # # # # # for day in days:
# # # # # #     if day == "Saturday" or day == "Sunday":
# # # # # #         continue
# # # # # #     print(f"Work day: {day}")
# # # # #
# # # # # #Program 3
# # # # # #
# # # # # # books = ["Sherlock Holmes", "The Hobbit", "Harry Potter"]
# # # # # #
# # # # # # search_book = input("Enter the book name to search: ")
# # # # # #
# # # # # # found = False
# # # # # #
# # # # # # for book in books:
# # # # # #     if book == search_book:
# # # # # #         print(f"Found the book: {book}")
# # # # # #         found = True
# # # # # #         break
# # # # # #
# # # # # # if not found:
# # # # # #     print("Book not found.")
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #Searching for a  Book
# # # # # # books = []
# # # # # # num_books = int(input("Enter the number of books: "))
# # # # # # for i in range(num_books):
# # # # # #     book = input(f"Enter the name of book {i+1}: ")
# # # # # #     books.append(book)
# # # # # #
# # # # # # search_book = input("Enter the book name to search: ")
# # # # # # for book in books:
# # # # # #     if book == search_book:
# # # # # #         print(f"Found the book: {book}")
# # # # # #         break
# # # # # #
# # # # #
# # # # # #Program 4
# # # # # # daily_water_intake  = [2.0, 2.5, 1.8, 2.2, 2.3, 2.0, 1.9]
# # # # # # total_water_intake = 0
# # # # # # day = 2
# # # # # # print("Daily Water Intake Report:")
# # # # # # print("-" * 50)
# # # # # # for water in daily_water_intake:
# # # # # #     print(f"Day {day}: {water} liters")
# # # # # #     total_water_intake += water
# # # # # #     day += 1
# # # # # # print("-" * 30)
# # # # # # print(f"Total water consumption for the week: {total_water_intake :.2f} liters")
# # # # # # avg_daily_intake = total_water_intake / len(daily_water_intake)
# # # # # # print(f"Average daily water consumption: {avg_daily_intake:.2f} liters")
# # # # #
# # # # # # print("-" * 40)
# # # # # # print("Summary:")
# # # # # # print("Ensure to stay hydrated and maintain a consistent water intake throughout the week.")
# # # # # # print("Remember, Hydrate to Feel Great! :) ")
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #Q.1
# # # # #
# # # # # #Assignment Statemnet
# # # # #
# # # # # # a = 20
# # # # # # b=50
# # # # # # print(a+b)
# # # # #
# # # # # #Assigning the value with operator
# # # # #
# # # # # # num=100
# # # # # # num+=50
# # # # # # print("The result of the assign num is :" , num)
# # # # # #
# # # # #
# # # # # #Conditional Statement
# # # # #
# # # # # #If Condition :
# # # # # #
# # # # # # age = int(input("Enter your age"))
# # # # # # if age >= 18:
# # # # # #     print("You are Eligible for PAN card Application")
# # # # #
# # # # # # If-else:
# # # # # #
# # # # # # Score= int(input("Enter the score you secured"))
# # # # # #
# # # # # # if Score>=85 :
# # # # # #     print("Your are eligible for CSE Stream")
# # # # # # else:
# # # # # #     print("Your are not Eligible for CSE Stream")
# # # # # #
# # # # # # print("All the best for your future Endevaour!!!! :)")
# # # # #
# # # # #
# # # # # #If-elIf:
# # # # # # names = ["Alice", "BOB", "Collin"]
# # # # # # emp_ids = [101, 102, 103]
# # # # # #
# # # # # # employee_name = input("Enter Your name: ")
# # # # # # employee_id = int(input("Enter Your ID: "))
# # # # # #
# # # # # # if employee_name in names and employee_id in emp_ids:
# # # # # #     print("Your Access is Granted")
# # # # # #     print("Welcome!!!")
# # # # # # elif employee_name not in names:
# # # # # #     print("Your Access is Denied due to incorrect name.")
# # # # # # else:
# # # # # #     print("Your Access is Denied due to incorrect ID.")
# # # # #
# # # # #
# # # # #
# # # # # # number_1 = int(input("Enter the First  number : "))
# # # # # # number_2 = int(input("Enter the Second  number : "))
# # # # # #
# # # # # # temp = number_1
# # # # # # num1_=number_2
# # # # # # num_2=temp
# # # # # # print(f"Swapped numbers: num1 = {number_1}, num2 = {number_2}")
# # # # #
# # # # # # for number in range(1, 21):
# # # # # #     if number % 2 == 0:
# # # # # #         continue
# # # # # #
# # # # # #     if number > 15:
# # # # # #         print("Number greater than 15 found, exiting the loop.")
# # # # # #         break
# # # # # #
# # # # # #     print(f"Odd number: {number}")
# # # # #
# # # # # # Convert Kilometers to Miles
# # # # #
# # # # # # kilometers = float(input("Enter distance in kilometers: "))
# # # # # #
# # # # # # conversion_factor = 0.621371
# # # # # #
# # # # # #
# # # # # # miles = kilometers * conversion_factor
# # # # # #
# # # # # # print(f"Distance in miles: {miles:.2f}")
# # # # #
# # # # # # Calculate Simple Interest
# # # # #
# # # # #
# # # # # principal = 200
# # # # # rate_of_interest = 5
# # # # # time = 5
# # # # #
# # # # # simple_interest = (principal * rate_of_interest * time) / 100
# # # # #
# # # # # print(f"Simple Interest on Rs. 200 for 5 years at 5% per year: Rs. {simple_interest:.2f}")
# # # # #
# # # # #
# # # # #
# # # #
# # # #
# # # # number = int(input("Enter the number : "))
# # # #
# # # # for i in range (1,11):
# # # #     table = number * i
# # # #     print(f"The table of the {number} x {i} is : " , table )
# # # # # # List of military vehicles with their maintenance costs
# # # # # # Each entry is a tuple (vehicle_name, maintenance_cost)
# # # # # maintenance_costs = [
# # # # #     ("Tank", 50000),
# # # # #     ("Helicopter", 70000),
# # # # #     ("Truck", 30000),
# # # # #     ("Jeep", 20000),
# # # # #     ("Boat", 40000)
# # # # # ]
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # # Initialize total maintenance cost
# # # # # total_cost = 0
# # # # #
# # # # # # Calculate the total maintenance cost and print individual vehicle costs
# # # # # print("Vehicle Maintenance Costs:")
# # # # # for vehicle_name, cost in maintenance_costs:
# # # # #     total_cost += cost
# # # # #     print(f"{vehicle_name}: ${cost:,}")
# # # # #
# # # # # # Calculate the average maintenance cost per vehicle
# # # # # average_cost = total_cost / len(maintenance_costs)
# # # # #
# # # # # # Print the total and average maintenance costs
# # # # # print(f"\nTotal Maintenance Cost: ${total_cost:,}")
# # # # # print(f"Average Maintenance Cost per Vehicle: ${average_cost:,.2f}")
# # # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # List of departments with their budget allocations
# # # # # Each entry is a tuple (department_name, allocated_budget)
# # # # # department_budgets = [
# # # # #     ("Education", 5000000),
# # # # #     ("Health", 7500000),
# # # # #     ("Transportation", 3000000),
# # # # #     ("Defense", 10000000),
# # # # #     ("Environment", 2000000)
# # # # # ]
# # # #
# # # # # Initialize total budget
# # # # # total_budget = 0
# # # # #
# # # # # # Calculate the total budget and print individual department budgets
# # # # # print("Department Budget Allocations:")
# # # # # for department_name, budget in department_budgets:
# # # # #     total_budget += budget
# # # # #     print(f"{department_name}: ${budget:,}")
# # # # #
# # # # # # Calculate the average budget allocation
# # # # # average_budget = total_budget / len(department_budgets)
# # # # #
# # # # # # Print the total and average budget allocations
# # # # # print(f"\nTotal Budget Allocation: ${total_budget:,}")
# # # # # print(f"Average Budget Allocation: ${average_budget:,.2f}")
# # # #
#1.
a=10
b=5
result=a and b
