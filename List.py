Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Student=["Anthony" , "Maths",90,2024]
print (Student)
['Anthony', 'Maths', 90, 2024]
Student[3]=2023
print(Student)
['Anthony', 'Maths', 90, 2023]
Student[2]="Anthony@gmail.com"
print(Student)
['Anthony', 'Maths', 'Anthony@gmail.com', 2023]
#For Adding 2 List
list=[13,14,16,17,18]
print
<built-in function print>
9
print(list)
[13, 14, 16, 17, 18]
combinedList=list+Student
print(cpmbinedList)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(cpmbinedList)
NameError: name 'cpmbinedList' is not defined. Did you mean: 'combinedList'?
print(combinedList)
[13, 14, 16, 17, 18, 'Anthony', 'Maths', 'Anthony@gmail.com', 2023]
print(list*3)
[13, 14, 16, 17, 18, 13, 14, 16, 17, 18, 13, 14, 16, 17, 18]

NestedList=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(NestedList)
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print
<built-in function print>
9
print(NestedList+Student)
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], 'Anthony', 'Maths', 'Anthony@gmail.com', 2023]
#Methods of the list
list.append(19,20,21,22,23,24,25)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list.append(19,20,21,22,23,24,25)
TypeError: list.append() takes exactly one argument (7 given)
print(list)
[13, 14, 16, 17, 18]
list.append(19)
print (list)
[13, 14, 16, 17, 18, 19]
list.extend([20,21,22,23,24,25])
print(list)
[13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
list.insert
<built-in method insert of list object at 0x0000022B1E168600>
list.insert(1,12)
print(list)
[13, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
list.insert(11)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list.insert(11)
TypeError: insert expected 2 arguments, got 1
list.insert(0.11)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list.insert(0.11)
TypeError: insert expected 2 arguments, got 1
list.insert(0,11)
print(list)
[11, 13, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
list.remove(13)
print(list)
[11, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#To remove by its position
list.pop(3)
16
print(list)
[11, 12, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25]
list.pop()
25
print(list)
[11, 12, 14, 17, 18, 19, 20, 21, 22, 23, 24]
list.count()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list.count()
TypeError: list.count() takes exactly one argument (0 given)
list.count(2)
0
list.count(18)
1
list.insert (3,15)
print(list)
[11, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24]
list.extend([15,16,17 ,15, 19 ,10])
print(list)
[11, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 15, 16, 17, 15, 19, 10]
list.count(15)
3
list.sort()
print(list)
[10, 11, 12, 14, 15, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
list.reverse()
print(list)
[24, 23, 22, 21, 20, 19, 19, 18, 17, 17, 16, 15, 15, 15, 14, 12, 11, 10]
list.copy()
[24, 23, 22, 21, 20, 19, 19, 18, 17, 17, 16, 15, 15, 15, 14, 12, 11, 10]
print(list)
[24, 23, 22, 21, 20, 19, 19, 18, 17, 17, 16, 15, 15, 15, 14, 12, 11, 10]
list.sort()
print(list)
[10, 11, 12, 14, 15, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
del list [2]
print(list)
[10, 11, 14, 15, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
list.pop(3)
15
print(list)
[10, 11, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
print(list[0:5])
[10, 11, 14, 15, 15]
print(list[0:])
[10, 11, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
print
<built-in function print>
print(list[:15])
[10, 11, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23]
print(list[5:15])
[16, 17, 17, 18, 19, 19, 20, 21, 22, 23]
list.len()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list.len()
AttributeError: 'list' object has no attribute 'len'
len(list)
16
print(len(list))
16
print(list)
[10, 11, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
listone=list.sort()
print (listone)
None
lis=sorted(list)
print(lis)
[10, 11, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
liss=list.sort()
print(liss)
None
print(list)
[10, 11, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24]
ages=[23,24,25,26,27]
age=reversed(ages)
print (age)
<list_reverseiterator object at 0x0000022B1E17D630>
age=list(reversed(ages))
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    age=list(reversed(ages))
TypeError: 'list' object is not callable
TypeError: 'list' object is not callable
SyntaxError: invalid syntax
#Copy
list=[20,30,79,09,45,39,40]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
list=[20,30,79,9,45,39,40]
list.copy()
[20, 30, 79, 9, 45, 39, 40]
print
<built-in function print>
print(list)
[20, 30, 79, 9, 45, 39, 40]
import sys
print(f"The max value occupied by (List) {sys.getsizeof(list)}")

The max value occupied by (List) 120
The max value occupied by (List) 120
SyntaxError: invalid syntax
#Create a list of Customer details , perform CRUD -

CustomerDetails=["Alice" , "alice123@gmail.com" , 5551]
CustomerDetails=["Alice" , "alice123@gmail.com" , 5551]
CustomerDetails=["Alice" , "alice123@gmail.com" , 5551,
                 "Bob" , "bob32@gmail.com" , 5512,
                 "Collin" , "Col@gmail.com",5513]
print(CustomerDetails)
['Alice', 'alice123@gmail.com', 5551, 'Bob', 'bob32@gmail.com', 5512, 'Collin', 'Col@gmail.com', 5513]
CoustomerDetails.append("Dev" , "dev@gmail.com" , 5514)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    CoustomerDetails.append("Dev" , "dev@gmail.com" , 5514)
NameError: name 'CoustomerDetails' is not defined. Did you mean: 'CustomerDetails'?
# Initial list of customers
customers = [
    {"id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com"},
    {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com"},
    {"id": 3, "name": "Charlie Brown", "email": "charlie.brown@example.com"}
]
print(
    
SyntaxError: multiple statements found while compiling a single statement
customers = [
    {"id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com"},
    {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com"},
     {"id": 3, "name": "Charlie Brown", "email": "charlie.brown@example.com"}]
print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}]
new_customer={"id":4, "name":"Dev","email":"Dev@gmail.com"}
customers.append(new_customer)
customers.append(new_customer)
print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}]
>>> #Create
>>> customers = [
...     {"id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com"},
...        {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com"},
...      {"id": 3, "name": "Charlie Brown", "email": "charlie.brown@example.com"}]
>>> print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}]
>>> #Read
>>> print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}]
>>> #Update
>>> new_customer={"id":4, "name":"Dev","email":"Dev@gmail.com"}
>>> KeyboardInterrupt
>>> customers.append(new_customer)
>>> print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}]
>>> customers.insert(1,new_customer)
>>> print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}]
>>> #Delete
>>> customers.remove(4)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    customers.remove(4)
ValueError: list.remove(x): x not in list
>>> customers.remove("id":4)
SyntaxError: invalid syntax
>>> remove_customer={'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}
>>> customers.remove(remove_customer)
>>> print
<built-in function print>
>>> print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}]
>>> #read
customer_id(customers,2)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    customer_id(customers,2)
NameError: name 'customer_id' is not defined. Did you mean: 'customers'?
#Delete
cust=customers.pop(2)
print(cust)
{'id': 3, 'name': 'Charlie Brown', 'email': 'charlie.brown@example.com'}
print
<built-in function print>
print(customers)
[{'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}, {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com'}, {'id': 4, 'name': 'Dev', 'email': 'Dev@gmail.com'}]
