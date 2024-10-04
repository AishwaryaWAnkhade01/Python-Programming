Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1. Convert the below list into numpy array then display the array
... 
...  Input: my_list = [1, 2, 3, 4, 5]
...  
SyntaxError: invalid syntax
>>> my_list=[1,2,3,4,5]
>>> import numpy as np
a
>>> arr=np.array(my_list)
>>> print
<built-in function print>
>>> print(f'conversion of list into numpy array{arr}')
conversion of list into numpy array[1 2 3 4 5]
>>> #. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
... 
...  Input: my_list = [1, 2, 3, 4, 5]
...  
SyntaxError: unexpected indent
>>> my_list=[1,2,3,4,5]
>>> new_list=np.array(my_list)
>>> print(f'List into array: {new_list}')
List into array: [1 2 3 4 5]
>>> #First and last index:
>>> print(f'the fisr index element is {new_list[0]}')
the fisr index element is 1
>>> print(f'the last index element is {new_list[-1]}')
the last index element is 5
>>> #Multiply each element by 2
>>> result=new_list*2
>>> print(f'the new array elements after multiplying each by 2 : {result}')
the new array elements after multiplying each by 2 : [ 2  4  6  8 10]
