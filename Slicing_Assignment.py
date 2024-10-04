Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q.1
import numpy as np
arr=np.zeros(10)
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
import numpy as np
arr=np.zeros(10)
print(f'array of 10 zeros\n{arr}')
array of 10 zeros
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#array of 10 ones:
array=np.ones(10)
print(f'array of 10 ones\n{array}')
array of 10 ones
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
##Array of 10 fives
arr_ay=np.fives(10)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    arr_ay=np.fives(10)
  File "C:\Users\kiran\AppData\Local\Programs\Python\Python312\Lib\site-packages\numpy\__init__.py", line 428, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'fives'
arr_ay=np.full(10,5)
                         
print(f'array of 10 fives : {arr_ay}')
                         
array of 10 fives : [5 5 5 5 5 5 5 5 5 5]

#Q.2:
                         
matrix=np.array(2,10)
                         
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    matrix=np.array(2,10)
TypeError: Cannot interpret '10' as a data type
>>> matrix=np.arange(2,11)
...                          
>>> new_matrix=matrix.reshape(3,3)
...                          
>>> print(new_matrix)
...                          
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
>>> #Q.3:
...                          
>>> arr=np.arange(12,39)
...                          
>>> print(arr)
... 
[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
 36 37 38]
>>> #Q.4
...                          
>>> my_list=[1, 2, 3, 4, 5, 6, 7, 8]
...                          
>>> arr=np.array(my_list)
...                          
>>> print(f'list to array:\n{arr})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'list to array:\n{arr}')
...       
list to array:
[1 2 3 4 5 6 7 8]
>>> #Tuples to array:
...       
>>> tup=(1,2,3,4,5,6,7,8)
...       
>>> arr=np.array(tup)
...       
>>> print(f'tuple to array:\n{tup}')
...       
tuple to array:
(1, 2, 3, 4, 5, 6, 7, 8)
