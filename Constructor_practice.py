# #Define a class Person with a constructor that initializes the name and age
# # of a person. Create two objects of this class and print their attributes.
#
# class Person:
#     def __init__(self,name , age):
#         self.name=name
#         self.age=age
#
#
# p1=Person("Jhon" , 30)
# print("HEY My name is ",p1.name)
# print("I am",p1.age)
#
# #Q.2Create a class Car with a constructor that takes the brand and model as parameters.
# # Instantiate the class with different values and print the car details.
#
# class Car:
#     def __init__(self,brand , model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#
#
# car_1=Car("Mecedes" , "Mercedes-AMG S 63 E","2024")
# print(car_1.brand)
# print(car_1.model)
# print(car_1.year)
#
# #3.Write a class Rectangle with a constructor that initializes the length and width.
# # Create a method to calculate the area of the rectangle.
#
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area_of_rectangle(self):
#         area=self.length* self.breadth
#         return area
#
# rect=rectangle(2,6)
# print(rect.length)
# print(rect.breadth)
# print(rect.area_of_rectangle())
#
# #4.Design a class Book with a constructor that accepts the title, author, and year.
# # Create an object for a book and print all the attributes.
# class Book:
#     def __init__(self,title,author,year):
#         self.title=title
#         self.author=author
#         self.year=year
#
#
# book=Book("Harry Potter" , "JK Rowling", "2-6-2024")
# print(book.title , book.author ,book.year)
#
# #5.Define a class Student with a constructor that takes the student's name and roll number. Print out the student's details using an object.
#
# class Student:
#     def __init__(self, name , roll_no):
#         self.name=name
#         self.roll_no=roll_no
#
# Student_1=Student("James" , "1190")
# print(Student_1.name)
# print(Student_1.roll_no)
#
# #6.Create a class BankAccount with a constructor that initializes the account holder’s name and balance.
# # Print the account details using the constructor.
# class BankAccount:
#     def __init__(self,acc_holder_name , balance):
#         self.acc_holder_name=acc_holder_name
#         self.balance=balance
#
# B=BankAccount("Aishwarya" , 12345678)
# print(B.acc_holder_name)
# print(B.balance)
#
# #7.Write a class Circle with a constructor that initializes the radius. Write a method to calculate the circumference.
#
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def circumference_of_circle(self):
#         cicum=2*3.14* self.radius
#         return cicum
#
# c=Circle(4.5)
# print(c.circumference_of_circle())
#
# #8.Create a class Employee that initializes the employee's ID and salary.
# #Instantiate the class with different values and print the employee's ID and salary.
#
# class Employee:
#     def __init__(self,employee_Id , salary):
#         self.employee_Id=employee_Id
#         self.salary=salary
#
#
# emp=Employee(10101 , 500000)
# print(emp.employee_Id , emp.salary)

#9.Design a class Laptop that takes the brand, processor, and RAM in the constructor. Create two laptop objects and display their details.

# class Laptop:
#     def __init__(self,brand , processor , RAM):
#         self.brand=brand
#         self.processor=processor
#         self.RAM=RAM
#
# laptop=Laptop("Lenovo","SnapDragaon" ,"32 GB")
# print("The Laptop is of brand Hp ",laptop.brand)
# print("The Laptop processor is " , laptop.processor)
# print("The laptop RAMm is ",laptop.RAM )
#
#
# #10.Write a class Movie that initializes the title and duration of a movie. Instantiate the class for different movies and print the details.
#
# class Movie :
#     def __init__(self,movies_names):
#         self.movies_names=movies_names
#
#
# m=Movie(["Harry Potter","Bridgerton","MAxton Hall","3 Idiots"])
# print(m.movies_names)

# ****************************************************************************************************************************************

# Constructor with method

#1.Create a class Account with a constructor that initializes the account balance.
# Add methods deposit and withdraw to update the balance. Implement a method to print the final balance after transactions.

# class Account:
#     def __init__(self,balance,amount):
#         self.balance=balance
#         self.amount=amount
#
#     def deposit(self,amount,balance):
#         self.balance+=amount
#         print("Deposited amount in account")
#
#     def withdraw(self,balance,amount):
#         self.balance-=amount
#         print("debited from account")
#
# acc=Account(100000 , 1500)
# print(acc.balance)
# print(acc.amount)
#
# print(acc.deposit())
# print(acc.withdraw())


#Write a class Student with a constructor that takes a student's name and marks. Create methods to calculate and display the grade based on marks.

# class Student:
#     def __init__(self , name , marks):
#         self.name=name
#         self.marks=marks
#
#     def get_grade(self):
#         if 90<= self.marks <=100:
#             print("A")
#         elif 80<=self.marks <=90:
#             print("B")
#         elif 70<=self.marks<=80:
#             print("C")
#         elif 60<=self.marks<=70:
#             print("D")
#         else:
#             print("Fail")
#
#
# student=Student("Eloise" , 98)
# student.get_grade()


# Define a class Rectangle with a constructor to initialize length and width. Add methods to calculate the area and perimeter of the rectangle.


class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area_of_rect(self,length,width):
        area= length * width
        print(f" The area of rectangle is {area} meter square")

rect=Rectangle(4,2)
rect.area_of_rect(8,4)


#Q.4Design a class BankAccount with methods for depositing and withdrawing money.
# The constructor initializes the account balance. Include a method to check the balance.

class Bank_Account:
    def __init__(self ,account_balance):
        self.acc_bal=account_balance


    def check_balance(self):
        # new=input("Enter 1 for checking balance")
        # if new==1:
            print(f"Your Current Balance amount is {self.acc_bal}")
        # else:
        #     print("ThankYou!!!")

    def Deposit(self,amount):
        # deposit=input("Deposit money")
        # print(deposit)
        if amount >0:
            self.acc_bal+= amount
            print(f"Money is Deposited {amount} in account")


    def Withdraw(self,amount):
        if 0< amount<=self.acc_bal:
            self.acc_bal-= amount
            print(f"Withdraw of money {amount} and currect balance is {self.acc_bal}" )

bank=Bank_Account(10000)
bank.check_balance()
bank.Deposit(3000)
bank.Withdraw(1000)
bank.check_balance()

#Q.5Create a class Employee with a constructor that initializes the employee's name, ID, and salary.
# Add a method give_raise to increase the salary by a given percentage and another method to display the details.

class Employee:
    def __init__(self , name, empId,salary):
        self.name =name
        self.empId=empId
        self.salary=salary

    def display_details(self):
        print(f"Employee name:{self.name}")
        print(f"Employee Id : {self.empId}")
        print(f"Employee Salary :{self.salary}")

    def give_raise(self,salary):
        new=self.salary*0.5
        new_salary=self.salary+new
        print(f"The salary is increase by 5% {new_salary}")







emp=Employee("Mukesh" , "123456" , 19000)
emp.display_details()
emp.give_raise(19000)




#Q.6Write a class Book that has a constructor for initializing the title, author, and pages.
#Add methods read_pages to keep track of how many pages you’ve read and status to print the percentage of the book completed.

# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.auhtor=author
#         self.pages=pages
#
#     def read_pages(self,pages):
#         if pages>=50:
#             print("You read a book 50 %")
#         elif pages>=30:
#             print("30% book is read")
#         elif pages>=20:
#             print("20% book is read")
#         elif pages>=10:
#             print("you are half a way")
#
#
# book=Book("Harry Potter" , "J.K Rowling" , 35)
# book.read_pages(35)


#Q.7Create a class Circle with a constructor that initializes the radius.
# Add methods to calculate both the circumference and area of the circle.

# class Circle:
#     def __init__(self , radius):
#         self.r=radius
#
#     def circumference(self):
#         if self.r>0:
#             c=2*3.14*self.r
#             return "The circumference of a circle is ",c
#
#     def area_of_circle(self,area):
#         area_circle=3.14*self.r
#         print(f"the area of circle is {area_circle}")
#
# circle=Circle(6)
# print(circle.circumference())
# circle.area_of_circle(4)

#Q.8Design a class Vehicle with a constructor that initializes the make and model.
# Add methods to start the vehicle, stop the vehicle, and display the vehicle information.
#
# class Vehicle:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#
#     def


#Session Work:

#Create a Rectangle class
# Create a class Rectangle that calculates the area and perimeter of a rectangle.
#
# Requirements:
#
# Attributes: length, width
# Methods:
# area() - Returns the area of the rectangle (length × width).
# perimeter() - Returns the perimeter of the rectangle (2 × (length + width)).


# class Rectangle:
#     def __init__(self , length,width):
#         self.length=length
#         self.width=width
#
#     def area(self):
#         if self.length > 0 and self.width > 0:
#             rectangle_area= self.length * self.width
#             print(f"The area of rectangle is : {rectangle_area}")
#         else:
#             print("length and width cannot be negative")
#
#     def perimeter(self):
#             perimeter_of_rect= 2 * self.length + self.width
#             print(f"The perimeter of a rectangle is : {perimeter_of_rect}")
#
# rect=Rectangle(8,-4)
# print(rect.area())
# print(rect.perimeter())
#
#
# #Create a Student class with grade functionality
# # Create a class Student that calculates the average of a student's grades.
# #
# # Requirements:
# #
# # Attributes: name, grades (a list of integers)
# # Methods:
# # add_grade(grade) - Adds a grade to the grades list.
# # get_average() - Returns the average of the grades.
# # get_grades() - Returns the list of all grades
#
#
# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.grades=[]
#
#     def add_grade(self,grade):
#         self.grades.append(grade)
#         print(f"grade ",grade,"is added in the list")
#
#
#     def get_average(self):
#         if self.grades:
#             avg=sum(self.grades)/len(self.grades)
#             print("The average of grades is ",avg)
#         else:
#             return 0
#
#
#
#     def get_grades(self):
#         print (self.grades)
#
#
#
#
# student=Student("Aishwarya")
# student.add_grade(40)
# student.add_grade(20)
# student.add_grade(60)
# student.get_average()
# student.get_grades()
#
#
# #Create a Library class with book management
# # Create a class Library that manages a collection of books.
# #
# # Requirements:
# #
# # Attributes: books (a list of book titles)
# # Methods:
# # add_book(book) - Adds a book to the collection.
# # remove_book(book) - Removes a book from the collection (if it exists).
# # list_books() - Prints all the books currently in the collection
#
# class Library:
#     def __init__(self,book_titles):
#         self.book_titles=[]
#
#     def add_book(self,book):
#         self.book_titles.append(book)
#         print(f"{self.book_titles} added in list")
#
#     def remove_book(self,book):
#         if book in  self.book_titles:
#             self.book_titles.remove(book)
#             print(f"Book '{book}'removed.")
#         else:
#             print(f"Book '{book}' is not in the list.")
#
#     def list_books(self):
#         return self.book_titles
#         print(f"current books in the list {book_titles}")
#
# lab=Library([])
# lab.add_book("Harry Potter")
# lab.add_book("MAxtonHall")
# lab.add_book("Bridgerton")
# lab.add_book("SAVE ME")
# lab.remove_book("MAxtonHall")
# lab.remove_book("Before YOu")
#
# lab.list_books()
#
#
# #Questions on list , methods constructor
#
# # What is the difference between a list's append() and extend() methods? Provide an example to demonstrate each.
#
# # Coding: Write a Python program to remove all occurrences of a specific element from a list using the remove() method.
#
# # append ()
#
# nw_list=[10,20,23,40,50]
# list=nw_list.append(70)
# print(f"The element is added in the list{nw_list}")
#
# #list_comprehension
#
# lis=[i for i in range (1,21)]
# lis.append(21)
# print(lis)
#
# #extend():
#
# lis=[10,20,30]
# lis.extend([80,90])
# print(lis)
#
# #programing question:
#
# #1.Write a Python program to remove all occurrences of a specific element from a list using the remove() method.
#
# # def remove_all (list,element):
# #     while element in list:
# #         list.remove(element)
# #         return list
# # list=[1,2,3,4,5,3,2,1,6,7,]
# #
# # ele=3
# #
# # result=remove_all(list,ele)
# # print(result)
# #
# #
# # #Q2.Write a Python program that creates a tuple and accesses its elements using both positive and negative indexing.
# #
# # tuple=(43,51,67,(89,70),96,100)
# # new=tuple[::-1]
# # print(new)
# #
# # t=tuple[-4]
# # print(t)
#
# #using constructor , methods,class
#
# class Person:
#     def __init__ (self,tp):
#         self.tp=tp
#
#     def ele_access(self):
#         element=self.tp[::-1]
#         return element
#
#     def ele_access_positive(self):
#         ele=self.tp[2]
#         return ele
#
#     def ele_access_negative(self):
#         elem=self.tp[-3]
#         return elem
#
#
#
#
# person=Person((10,20,34,56,(78,98),60,40))
# print(f"The elements of the tuple is ",person.ele_access())
# print(f" the second index element is {person.ele_access_positive()}")
# print(f" the number at index -3 is {person.ele_access_negative()}")
#
#
#
# print(f"****")
# print(f"***")
# print(f"**")
# print(f"*")
#
# #Q.6Given two sets, write a Python program to find their difference and symmetric difference using set methods.
#
#
# class Maths:
#     def __init__(self,set_A , set_B):
#         self.set_A=set_A
#         self.set_B=set_B
#
#     def difference(self):
#         diff=self.set_A-self.set_B
#         return diff
#
#     def symmetric_diff(self):
#         sym_diff=self.set_A ^ self.set_B
#         return sym_diff
#
# p={11,12,68,32,15,60,70,84,11,13}
# q={11,12,61,33,155,70,40,84,11,13}
#
# math=Maths(p,q)
# print(f"The difference between both the sets are : ",math.difference())
# print(f"The symmetric difference between voth the set are : {math.symmetric_diff()}")
#
#
# #Q.4 Coding: Write a Python program to merge two dictionaries. If a key exists in both dictionaries, add their values together.
#
# # dict_1={id:101 , "name" :"collin" , "sal":40000}
# # dict_2={id:102,"name":"collin","sal":4000,}
# #
# # dict_1.update(dict_2)
# # print(dict_1)
#
# class Dictionary:
#     def __init__(self,dict_a,dict_b):
#         self.dict_a=dict_a
#         self.dict_b=dict_b
#
#     def merge_dictionary(self):
#                self.dict_a.update(self.dict_b)
#                print(self.dict_a)
#
# dictionary=Dictionary({id:101 ,"name":"Anthony","Sal":4000},{id:101,"name":"Collin","sal":6000})
# dictionary.merge_dictionary()
#
#
# # Write a Python program to convert a list of tuples into a dictionary where the first element of the tuple is the key and the second element is the value.
#
#
# my_tuples=[("a",1) ,("b",2),("c",3) ,("d",4)]
# new_list=dict(my_tuples)
# print(new_list)
#
# class Convert:
#     def __init__ (self,my_tuples):
#         self.my_tuples=my_tuples
#
#     def tuple_to_dict(self):
#         new_list=dict(my_tuples)
#         print(new_list)
#
# my_tuples=[('id',101),('name',"anthony"),('sal',3000),('city','mumbai')]
#
#
#
# convert=Convert(my_tuples)
# convert.tuple_to_dict()
#
#
#
#
# class Student:
#     def __init__(self,name,country):
#         self._name=name
#         self.__country=country
#
#     def show(self):
#         print(f"name is {self.name} , country is {self.country}")
#
#
# student=Student("Aishwarya","India")
# # student.show()
# print(student._name)
# print(student.__country)


# Accessing private member variables:

# class Student:
#     def __init__(self,name,country):
#         self.__name=name
#         self.__country=country
#
#     def __access (self):
#         print(f"my name is {self.__name} i live in {self.__country}")
#
#     def show(self):
#         self.__access()
#
# student=Student("Aishwarya","India")
# print(student.get__country())

#class with Encapsulation....

# 1. Class and Object Creation
# Question: Create a class Student with attributes name and age. Define a method display() that prints the student's details. Create two objects of the class and display their details.

class Student:
    def display(self,name,age):
        name=name
        age=age
        print(f'my name is {name} and my age is {age}')

student=Student()
student.display('aishwarya',23)


#Write a Python program that defines a class Rectangle with attributes length and width.
#Use a constructor to initialize these values. Also, create a method area() to return the area of the rectangle.

class Rectangle:
    def __init__(self,length,width):
     self.len=length
     self.width=width

    def area(self):
        area_of_rectangle=self.len*self.width
        return area_of_rectangle
rectangle=Rectangle(5,3)
print(rectangle.area())

#Question: Create a class Person with attributes name and age, and a method display().
# Inherit a class Employee from Person and add an additional attribute salary. Override the display() method to include salary.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'The name is {self.name}, the age is {self.age}')

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def display_info(self):
            print(f'salary is {self.salary}')



employee=Employee('Aishwarya',23,150000)
employee.display()
employee.display_info()



# 4. Polymorphism
# Question: Write a Python program that defines two classes Cat and Dog. Both classes should have a method sound() that prints different sounds for each.
# Write a function that takes an object and calls the sound() method, demonstrating polymorphism.

class Cat:

    def sound(self,sound):
        sound='bark'
        print(f'cat {sound} is ')

class Cat:
    def sound(self):
        sound = 'Meow'
        print(f'The cat sound is {sound}')

class Dog(Cat):
    def sound(self):
        sound = 'Bark'
        print(f'The dog sound is {sound}')

# Creating an object of the Dog class
dog = Dog()

# Calling the sound method twice
dog.sound()  # Output: The dog sound is Bark
dog.sound()  # Output: The dog sound is Bark

# Encapsulation (Private Attributes)
# Question: Create a class Account with a private attribute balance.
# Write methods to deposit an amount and check the balance. Ensure that the balance cannot be accessed directly from outside the class.

class Account:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print('balance')
        else:
            print('transaction fail')

    def get_balance(self):
        return self.__balance

bal=500
account=Account(bal)
account.deposit(4000)
print(account.get_balance())


#Polymorphism:
















































