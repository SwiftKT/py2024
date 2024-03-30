#locally created for pushing to git hub repository

print("Hello to Mihir from Tims")

# ctrl ~  Terminal open close ctrl j
#
# workbench.action.terminal.focus


# Python tutorial for beginners 1/106  Bro code
# print("I love pizza")
# print("It's really good")

# video 4
# name = input("Enter your name:  ")
# age = int(input("Enter your age"))
# print(f"Hello {name}")
# print(f"You are {age} years old")
# ----------------------
# adjective1 = input("Enter an adjective: ")
# noun = input("Enter a noun")
# adjective2 = input("Enter an adjective")
# verb = input("Enter a verb: ")
# adjective3 = input("Enter an adjective")
#
# print(f"Today I went to {adjective1} zoo.")
# print(f"In a exhibit, I saw {noun}")
# print(f"{noun} was {i} and {verb}ing")
# print(f"I was {adjective3}")
# -------------------------
# import os
# os.system('cls')
# length = float(input("Enter the length of a rectangle > "))
# width = float(input("Enter the width of a rectangle >"))
# area = length * width
# print("----------------------")
# print(f"The area is: {area}^2")
# print("----------------------")

# import os
# os.system('cls')
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like to buy?: "))
# total = price * quantity

# print(f"you have bought {quantity} x {item}/s") 
# print(f"Your toatal is: ${total}")

# import math
# import os
# os.system("cls")
# print("---------------------------")
# radius = float(input('Enter the radius of a circle: '))
# print("---------------------------")
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {circumference} ")
# print("---------------------------")

 

# print("---------------------------")
# radius = float(input('Enter the radius of a circle: '))
# print("---------------------------")
# area = math.pi * pow(radius, 2)
# print(f"The Area of the circle  is: {round(area)} ")
# print("---------------------------")
 
# import random
# import os

# os.system('cls')
# print(random.sample(range(1,51), 6))
# print("------------------")
# print(sorted(random.sample(range(1,51), 6)))
# print("-------------------")
# numbers = set(random.sample(range(1,51),6))
# print(numbers) 
# numbers = [random.choice(range(1,51)) for _ in range(6)]
# print (numbers)
# print("--------------------------")
# numbers = [random.sample((1,51), 6)]
# print (numbers)

# import random
# import os

# os.system('cls')
# print(random.sample(range(1,51), 6))
# print("------------------")
# print(sorted(random.sample(range(1,51), 6)))
# print("-------------------")
# numbers = sorted(random.sample(range(1,51),6))
# print(numbers) 






# import math
# import os
# os.system("cls")

# a = float(input("Enter side A:  "))
# b = float(input("Enter side B:  "))
# c = math.sqrt(pow(a, 2)+ pow(b,2))
# print(f"Side C = {c}")

# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result,3))
# elif operator == "-":   
#     result  = num1 - num2
#     print(round(result,3))
# elif operator == "*":   
#     result  = num1 * num2
#     print(round(result,3))
# elif operator == "/":   
#     result  = num1 / num2
#     print(round(result,3))

# else: 
#     print(f"{operator} is not a valid operator")
    
# import os

# os.system("cls")

# unit= input("Is this temperature in Celsius or Farenheit (C/F).:")
# temp = float(input("Enter the temperature: "))
# if unit == "C" or "c":
#     temp = round((9 * temp) / 5 + 32, 1 )
#     print(f"The temperature in Farenheat is: {temp} ")
# elif unit == "F" or "f":
#     temp = round((temp -32) * 5 / 9, 1 )
#     print(f"The temperature in Celsius is: {temp} ")
# else:
    
#     print(f"{unit} is an invalid unit of measurement")
    
          

   
# import os
# os.system("cls")
# print("-----------------")
# username = input("Enter a username: ")
# if len(username)  > 12:
#     print("Your user name can't be more than 12 characters" )
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces") 
# elif not username.isalpha():
#     print("Your user name can't contain numbers")   
# else: 
#     print(f"Welcome  {username}")  
# 
#  Python compound interest calculator           
# import os
# os.system("cls")

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")
        
# while rate <= 0:
#     rate = float(input("Enter the rate amount: "))
#     if rate <= 0:
#         print("rate can't be less than or equal to zero") 
# while time <= 0:
#     time = float(input("Enter the time in years: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero") 
            
# total = principle * pow((1 + rate / 100), time)

# print(f"Balance after {time} years/s: ${total}")

# import os
# class Language:
#     def __init__(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
#     def message(self):
#         print("My name is " + self.name)
        
# languages = [Language("Python"), Language("JavaScript")]

# for language in languages:
#     language.message()

# print(languages)

# ----------------
# random.sample(list(set(l_dup)), 3)
# https://github.com/nkmk/python-snippets/blob/8451f39a11a8ee4ec3d2649cf512a1bf1e8532f1/notebook/random_sample.py#L37-L41
# --------------------
# import random
# import os
# l_dup = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
# print(l_dup)
# print(random.sample(l_dup, 3))

# print(set(l_dup))
# # {0, 1, 2, 3}

# print(random.sample(list(set(l_dup)), 3))
# # [0, 2, 1]
# import os
# import random

# os.system("cls")
# numbers = sorted(random.sample(range(1,51),6))
# print(numbers) 
# print( sorted(random.sample(range(1,51),6)))

# print(random.sample(list(set(range(1,51))),6))
# print(random.sample(list(set(range(1,51))),6))
# print(random.sample(list(set(range(1,51))),6))

 
# for x in reversed(range(1, 11, 2)):
#     print(x)
# for x in (range(1, 11, 2)):
#     print(x)
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x, end="")
    
 

# rows = int(input("Enter the # of rows:  "))
# columns = int(input("Enter the # of columns:  "))
# symbol = input("Enter a symbol to use:  ")


# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()


# import os
# import time
# os.system("cls")

# my_time = int(input("Enter the time in seconds: "))
# for x in range(0, my_time):
#     print(x)
#     time.sleep(my_time)

# print("TIME'S UP!")
# import os
# import time
# os.system("cls")

# my_time = int(input("Enter the time in seconds: "))
# # for x in reversed (range(0, my_time)):
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(my_time)

# print("TIME'S UP!")
# import time
# my_time = int(input("Enter the time in seconds: "))
 
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x /60) % 60
#     hours = int(x /3600) 
    
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!") 

# import os
# os.system("cls")

# sum_odd_digits = 0
# sum_even_digits = 0
# total = 0

# # Step 1
# card_number = input("Enter a credit card #: ")
# card_number = card_number.replace("-", "")
# card_number = card_number.replace(" ", "")
# # Reversing the string
# card_number = card_number[::-1]

# # step 2
# for x in card_number[::2]:
#     sum_odd_digits += int(x)
    
# # step 3
# for x in card_number[1::2]:
#     x = int(x) * 2
#     if x >= 10:
#         sum_even_digits += (1 + (x % 10))
#     else:
#         sum_even_digits +=x
        
# # Step 4
# total = sum_odd_digits + sum_even_digits
# # Step 5
# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")

# print(card_number)

# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutalbe, but Add/Remove OK. NO duplicates
# Tuple = ()  ordered and unchangeable. Duplicates OK. FASTER 

# fruits = ["apple", "orange", "banana", "coconut" ]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# fruits.append("pineapple")
# fruits.remove("pineapple")
# fruits.insert(0, "pineapple")

# fruits.sort()
# fruits.reverse()
# fruits.clear()

# video 22 Shopping cart
# foods = [] 
# prices = []
# total = 0
# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR CART -------")
# for food in foods:
#     print(food, end=" ")
# for price in prices:
#     total += price

# print(f"Your total is: ${total}")

# Video 23 python 2d collections

# import os
# os.system("cls")
# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]

# # for collection in groceries:
# #     print(collection)
# for collection in groceries:
#     for food in collection:
#         # print(food)
#         print(food, end=" ")
#     print()
   
   
# touple        
# import os
# os.system("cls")
# groceries = ({"apple", "orange", "banana", "coconut"},
#              {"celery", "carrots", "potatoes"},
#              {"chicken", "fish", "turkey"})

# # for collection in groceries:
# #     print(collection)
# for collection in groceries:
#     for food in collection:
#         # print(food)
#         print(food, end=" ")
#     print()
        
        
# # touple        
# import os
# os.system("cls")
        
# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9 ),
#            ("*", 0, "#") )   
# for row in   num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()
        
# #   Video 26 
#   DECORATOR DECORATOR
# import os
# os.system("cls")
# def start_end_decorator(func):
#     def wrapper():
#         print('Kurian or start')   
#         func()  
#         print("Thomas or end")
#     return wrapper
# @start_end_decorator
# def print_name():
#     print('Kuttammanal')

# # print_name = start_end_decorator(print_name)

# print_name()
# DEOCRATOR 2 DECORATOR 2
# import functools
# def my_decorator(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do.... print('Kurian or start')   
#         result = func(*args, **kwargs)  
#         # Do.... print("Thomas or end")
#         return result
#     return wrapper


# @my_decorator
# def add5(x):
#     return x + 5




# print_name = start_end_decorator(print_name)

# result = add5(10)
# print(result)


# result = add5(20)
# print(help(add5))
# print(add5.__name__)

# Repeat decorator
# import functools

# def repeat(num_times):
#     def deocorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return deocorator_repeat
        
# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}') 
      
# greet("Alex")

# ###############################
# Stacked deocroator
# ###############################
# import functools
# def start_end_decorator(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper

# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}= {v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper
        
# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting       
        
# say_hello("Alex")




         
# --------------------------------------
# import functools

# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0
        
#     def  __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f'This is executed {self.num_calls} times')
#         return self.func(*args, **kwargs)

# @CountCalls
# def say_hello():
#     print('Hello')
    
# say_hello()    

# Generator example
# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -=1
# cd = countdown(4)        
    
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# 
 

# os.system("cls")
# print("=INTERMEDIATE PYTHON FREECODECAMP.ORG=")
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#        nums.append(num)
#        num += 1
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
        
# print(sum(firstn(5)))
# print(sum(firstn_generator(5)))
       
# import os
# import sys
# os.system("cls")
# print("INTERMEDIATE PYTHON FREECODECAMP.ORG")
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#        nums.append(num)
#        num += 1
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
        
# print(sys.getsizeof(firstn(100)))
# print(sys.getsizeof(firstn_generator(100)))

# import os
# os.system("cls")
# print()
# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a 
#         a, b = b, a + b
        

# fib = fibonacci(30)
# for i in fib:
#     print(i)



# import os
# import sys
# os.system("cls")
# mygenerator =  (i for i in range(1000000) if i % 2 == 0)
# print(sys.getsizeof(mygenerator))

# mylist =  [i for i in range(1000000) if i % 2 == 0]
# print(sys.getsizeof(mylist))

# for i in mygenerator:
#     print(i)
    

# Process: An instance of a program (e.g a Python interpretor) 

# Take advantage of multiple CPU and cores  
# Seperate memory space -> Memory is not shared between process
# Great for CPU-bound processing
# New process is started independently from other processes
# Processes are interruptable/killable
# One GIL for each process -> avoids GIL limitation

# Heavyweight
# Starting a process is slower that starting a thred
# More memory
# IPC (inter-process communication) is more complicated

# Threads
# Threads: An entity within a process that can be scheduled(also known as 
# "lightweight process)
# A process can spawn multiple threads
#
# + All threads within a process share the same memory
# + Lightweight
# + Starting a thread is faster than sharing a process
# + Great for I/O-bound tasks
# 
# - Threading is limited by GIL: Only one thread at a time
# - No effect for CPU-bound tasks
# - Not interruptable/killable
# - Careful with race conditions 
#
# GIL: Global interpreter lock
# - A lock that allows only one theread at a time to execute in Python
# - Needed in CPython because memory management is not thread-safe
#
# - Avoid:
#   -Use multiprocessing
#   -Use a different, free-threaded Python implementation(Jython, IronPython)
#   -use  python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
# from threading import Thread

# def square_numbers():
#     for i in range(100):
#         i * i
    
# if __name__ == "__main__":
#     threads = []
#     num_threads = 10
    
#     # create threads
#     for i in range(num_threads)
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
        
#     # start threads
#     for thread in threads:
#         thread.start()
#     # join thread in threads:
#        print('end main')
       
      
# from threading import Thread, Lock
# import time

# database_value = 0

# def increase(lock):
#     global database_value
    
#     #################################
#     # lock.acquire()
#     # local_copy = database_value
#     # # processing
#     # local_copy +=1
#     # time.sleep(0.1)
#     # database_value = local_copy
#     # lock.release()
#     ################################
#     with lock:
#         local_copy = database_value
#         local_copy +=1
#         time.sleep(0.1)
#         database_value = local_copy
      
        
    
# if __name__ == "__main__":
#     lock = Lock()
#     print('start value', database_value)
    
#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
    
#     print('end value', database_value)
    
#     print('end main')
    
    
# from threading import Thread, Lock
# from queue import Queue
# import time
    
# if __name__ == "__main__":
    
#     q = Queue()
#     q.put(1)
#     q.put(2)
#     q.put(3)
    
#     # 3 2 1  -->
#     first = q.get()
#     print(first)
#     q.task_done()
#     q.join()  # block the main thread until all items in the que are processed
    
#     # q.empty()
#     print('end main')
# Queue Thread  safe    
# from threading import Thread, Lock, current_thread
# from queue import Queue
# import time

# def worker(q, lock):
#     while True:
#          value = q.get() 
         
#          #processing
#          with lock:
#             print(f'in {current_thread().name} got {value}')
#          q.task_done()
     
# if __name__ == "__main__":
    
#     q = Queue()
#     lock = Lock()
#     num_threads = 10
#     for i in range(num_threads):
#         thread = Thread(target=worker, args=(q, lock))
#         # thread.daemon = True
#         thread.daemon = False
#         thread.start()

#     for i in range(1,21):
#         q.put(i)
    
#     q.join()
        
#     print('end main')



# from multiprocessing import Process
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)
# processes = []
# num_processes = os.cpu_count()
# # create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)
# # start
# for p in processes:
#     p.start()  
# p.start()      
# # join
# for p in processes:
#     p.join()
    
# print('end main')        

# from multiprocessing import Process, Value, Array
# import os
# import time

# def square_numbers():
#     for i in range(1000):
#         i * i
        
        
        
# if __name__ == "__main__":
        
#     processes = []
#     num_processes = os.cpu_count()
#     # number of CPUs on the machine. Usually a good choice for the number of processes
    
#     # create processes and assign a function for each process
#     for i in range(num_processes):
#         p = Process(target=square_numbers)
#         processes.append(processes)
    
#     # start all processes
#     for process in processes:
#         process.start() 
     
#     # wait for all processes to finish
#     # block the main program until these processes are finished
#     for process in processes:
#         process.join()
    
# print('end main')        

# from multiprocessing import Process, Value, Array, Lock
# import os
# import time
 
# def add_100(numbers, lock):  
#     for i in range(100):
#         time.sleep(0.01)
#         for  i in range(len(numbers)):
#             numbers[i] += 1   
         
# if __name__ == "__main__":
#     lock = Lock()
#     shared_array = Array('d', [0.0, 100.0, 200.00])  
#     print('array at beginning is', shared_array[:]) 
          
#     p1 = Process(target=add_100, args=(shared_array, lock) )
#     p2 = Process(target=add_100, args=(shared_array, lock) )
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()

#     # print('number at the end is', shared_number.value)
#     print('array at the end is', shared_array[:])
    # print('number at the end is', shared_number.value)
    # print('array at the end is', shared_array[:])
# # ---------------------------------------------


# from multiprocessing import Process, Value, Array, Lock
# import os
# from multiprocessing import Queue
# import time
 
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i * i) 

# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)        
         
# if __name__ == "__main__":
#     os.system("cls")
#     numbers = range(1,6)
#     q = Queue()
#     p1 = Process(target=square, args=(numbers, q)) 
#     p2 = Process(target=make_negative, args=(numbers, q) )
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     while not q.empty():
#         print(q.get())
# ---------------------------------------------
# # ---------------------------------------------

#  method in parallel
# from multiprocessing import Pool
# import os
 
 
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i * i) 

# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)   
# def cube(number):
#     return number * number * number

     
         
# if __name__ == "__main__":
#     os.system("cls")
#     print()
#     numbers = range(10)
#     pool = Pool() 
#     #cube, nm map apply join close
#     result = pool.map(cube, numbers)
#     # pool.apply(cube, numbers[0])
#     pool.close()
#     pool.join()
#     print(result)
    
# ---------------------------------------------

# Intermediate python freecodecamp.org 
#  4:53/5:
# FUNCTION ARGUMENTS
# - The difference between argument and parameters
# - Positional and keyword arugments
# - Default arguments
# - Variable-length aruments(*args and **kwars)
# - Container unpacking into function arguments
# - Local vs. global aruments
# - Paramenter passing (by value or by reference)
# """"""

# import os
# os.system("cls")
# print()
# import os


# def foo(a, b, c):
#     print(a, b, c)

# my_list=[1,2,3]
# foo(*my_list)
# my_dict = {'a': 1, 'b': 2 , 'c': 3}
# foo(**my_dict)


# import os

# os.system("cls")
# print()

# def foo(a, b, *args, **kwargs):
#     print (a, b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print (key, kwargs[key])   

# foo(1, 2, 3, 4, 5, six=6, seven=7)


# import os
# os.system("cls")
# nums = [1,2,3,4]
# print([i * 3 for i in nums])

# import os
# os.system("cls")
# print()
# strings = ["intro", "to", "list", "comps"]
# print([i.upper() for i in strings])

 
# import os
# os.system("cls")
# print()
 

# nums = [1, 2, 3, 4, 5]
# def timesFive(num):
#     return  num * 5
    
# # results = []
# # for i in nums:
# #     i = timesFive(i)
# #     print("i", i)
# #     results.append(i)

# # print('results', results)
# # print()
# new_nums = [timesFive(i) for i in nums]
# print('results', new_nums)
    
# import os
# os.system("cls")
# print()
# nums = [1, 2, 3, 4, 5]
# def timesSix(num):
#     return  num * 6
# results = [timesSix(i) for i in nums  if i > 2]
# print('results', results)

import os
os.system("cls")
print()
# dicts = [{"name": "John"}, {"name": "Matt"}]
# # results =[]

# # for i in dicts:
# #     results.append(i['name'])

# results = [i['name']  + " python " for i in dicts]
# print("results", results)





# list1 = [1,2,3]
# # print([i * 5 if i == 3 else i for i in list1])
# print([i for  i  in list1])
# # print([i for  i  in list1 if i > 1])
# print([i * 5 if i == 3 else i for  i  in list1 if i > 2])
# print([i * 5 if i == 3 else i for  i  in list1])
# print([i * 5 if i == 3 else i for  i  in list1 if i == 1])
# print([i * 5 if i == 3 else i for  i  in list1 if i > 1])
# print([i * 5 if i == 3 else i for  i  in list1 if i > 10])

avail_units = {
    '101' : {
        'bedrooms' : 3,
        'bathrooms' : 2,
        'price' : 1625
    },    
    
    '215' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1550
    },
    '231' : {
        'bedrooms' : 1,
        'bathrooms' : 1,
        'price' : 1400
    },
    
    '431' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1550
    },
    
    '422' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1575
    },
    
    '123' : {
        'bedrooms' : 3,
        'bathrooms' : 2,
        'price' : 1675
    },
    
    '223' : {
        'bedrooms' : 2,
        'bathrooms' : 2,
        'price' : 1615
    },
     
    '515' : {
        'bedrooms' : 1,
        'bathrooms' : 1,
        'price' : 1610
    }, 
    
    '625' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1560
    },             
}

# Filter function - filter (function, iterable) 
#                 - Returns itmes from iterable based on some criteria

# def my_filter(unit_num):
#     if avail_units[unit_num]['price'] < 1600 and avail_units[unit_num]['bedrooms'] >=2:
#         return True
#     else:
#         return False

# x = list(filter(my_filter, avail_units))

# x = [key for(key, value) in avail_units.items() if value["price"] < 1600 and value["bedrooms"]>=2]
# x = [key for(key, value) in avail_units.items()]
# print(x)

# Higher Order function = a funcion that either:
# 1. Accepts a funciton, or returns a function

# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello")
#     print(text)

# hello(loud)
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y /x
#     return dividend
# divide = divisor(2)
# print(divide(10))

###############################

# def funcBuilder(x):
#     return lambda num: num + x

# addTen = funcBuilder(10)
# addTwenty = funcBuilder(20)

# print(addTen(7))
# print(addTwenty(7))

################################
# MAPMAP
# lambda num : num * num
# numbers = [3,7.12,18,20,21]
# squared_nums = map(lambda num : num * num,  numbers)
# print(list(squared_nums))

# FilterFilter
# numbers = [3,7,12,18,20,21] 
# lambda num : num % 2 != 0
# odd_nums = filter(lambda num : num % 2 != 0, numbers)
# print(list(odd_nums))

# REDUCEREDUCE
# from functools import reduce
# numbers = [1, 2, 3, 4, 5, 1]
# lambda acc, curr: acc + curr
# total = reduce(lambda acc, curr: acc + curr, numbers)
# total = reduce(lambda acc, curr: acc + curr, numbers, 10)
# print(total)
# print(sum(numbers))

# names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']
# char_count = reduce(lambda acc, curr: acc + len (curr), names, 0)

# print(char_count)

# a = [1, 2, 3]
# b = map(lambda i: i * 5, a)
# print(list(b))
# print(list(map(lambda i: i * 5  if i == 3 else i,  filter(lambda i: i > 1, a) )))

# print([i * 5 if i == 3 else i for i in a if i > 1])

# results = []
# for i in a:
#     if i > 1:
#         if i == 3:
#             i = i * 5
#         else:
#             i
#         results.append(i)


# print(results)


# nums = [1, 2, 3, 4]
# print([i for i in nums])
# print([i for i in nums if i > 1])
# print([i for i in nums if i > 2])
# print([i for i in nums if i > 1 if i != 3])
# print([i for i in nums if i > 1 and i != 3])

# nums = [1, 2, 3, 4]
# fruit = ['Apples', 'Peaches', 'Pears', 'Bananas']
# # print()
# # print([(i, f) for i in nums if i > 1 if i != 3   for f in fruit])
# print()
# print([(i, f) for i in nums if i > 1 if i for f in fruit])
# print()
# print([(i, f) for i in nums if i > 1 if i != 3   for f in fruit if f != "Pears" and f != "Apples"])
# print()

# for i in nums:
#     if i > 1:
#         if i != 3:
        
#             for f in fruit:
#                 if f != "Pears" and f != "Apples":
#                     print(i, f)


# map(function, iterable)
# a = [1, 2, 3, 4] 
# print([x  for x in a])
# print([x * 2 for x in a])

# print(list(map(lambda x: x * 2, a)))
# print(list((map(str, [1,2,3,4]))))
# print([str(x) for x in [1,2,3,4,5,6]])
# print([str(x) for x in [1,2,3,4] if x > 1])
# print(list(filter(lambda x: x > 1, map(int, [1,2,3,4]))))

# a = [1, 2, 3, 4]
# print([x * 2 for x in a])
# print(list(map(lambda x: x * 2, a )))
# def timesTwo(i):
#     return i * 2
# print(list(timesTwo(x) for x in a))
# print(list(map(timesTwo, a)))

 
 

# import os
# import sys
# os.system("cls")
# print("Intermediate python programming course freecode camp.org")
 
# reducereduce

# from functools import reduce  
# print(reduce(lambda x, y: x*y, [1,2,3,4]))    
# print(reduce(lambda x, y: x+y, [1,2,3,4]))    
# print(sum([i for i in [1,2,3,4]])) 

# to flaten
# b=[[1,2],[1,2],[1,2]]
# print([i for sublist in b for i in sublist])
# print(reduce(lambda x,y: x+y, b))
# print(reduce(lambda x,y: x if x > y else y, [1,2,3,4,5]))
# print(max ([1,2,3,4,5,6]))

# def addTwo(a, b):
#     return a +b
    
# print(reduce(addTwo, [1,2,3]))

# age_d  = {'Jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# print({k:v**2 for k, v in age_d.items()})

# print({i : chr(65 + i) for i in range (4)})
# print({i : i for i in range (4)})
# print({i : i**2 for i in range (4)})
# print({i : str(i) for i in range (4)})
# age_d  = {'Jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# print({k:v for k,v in age_d.items()})
# print(age_d.items())
# age_d  = {'Jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# # printing only the keys not values
# # for i in age_d:
# #     print(i)
# print()
# print({k:v for k, v in age_d.items()}) 
# print()   
# # print({k:v for k, v in age_d.items() if v > 40}) 
# # print({(k if k == 'Jack' else):(v if  v == 38 else ) for k, v in age_d.items()}) 
# print({(k if k == 'Jack' else 'Brendan'): v for k, v  in age_d.items()}) 
# print({k:v for k, v in age_d.items()}) 

# age_d  = {'Jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# print({k:v for k, v in age_d.items()}) 
# print()
# print({k:('old' if v > 40 else 'young') for k, v  in age_d.items()} )

# print({(k):(v) for (k, v) in age_d.items()}) 
# print({(k if k == 'Jack' else 'Brendan'):v**2 for k, v  in age_d.items()}) 
   
# nums = [1, 2, 3, 4]
# fruits = ['Apples', 'Peaches', 'Pears', 'Oranges']

# print([(i,f) for i in nums for f in fruits])

# print()
# for i in nums:
#     for f in fruits:
#         print(i, f)

# print([(i,f) for i in nums for f in fruits for j in [10, 20, 30]])

# for i in nums:
#     for f in fruits:
#         for j in [10, 20,30]:
#             print(i, f, j)


# Flatening the list

# a = [[12,3], [55],[5,5,5]]
# print(a)
# print([item for sublist in a for item in sublist])

# touplessetdictionarylistoflist
# DoubleforLoops
# nums = [1, 2, 3, 4]
# fruits = ['Apples', 'Peaches', 'Pears', 'Oranges']

# print([(i,f) for i in nums for f in fruits])
# print()
# print([{i:f} for i in nums for f in fruits])

# print([set([i,f]) for i in nums for f in fruits])

#  zipzipzip
#  zipping -- shortest of the two list
# nums = [1, 2, 3, 4]
# fruits = ['Apples', 'Peaches', 'Pears', 'Oranges']

# print(list(zip(nums, fruits)))
# # unused values
# print([(i) for i in nums for f in fruits])
# print([(i,f) for i in nums for f in fruits])

# printing list comprehensions
# print([(i) for i in range(4)])
# def printReturnVal(val):
#     print("val:  ", val)
#     return val

# [printReturnVal(i) for i in range(4)]

# [print("hey", i ) or i for i in range(4)]

# [print("hey", i ) or str(i) for i in range(4)]


# tupletupletrailingcomma

# a = 1,
# print(a)
# print(type(a))

# print([(i for i in "hey")])
# # tuple((i for i in [1,2,3]))
# # tuple((i for i in "hey"))
# # initiating a tuple
# a = (i for i in (1,2,3)),
# print(type(a))
# print(a)
# print(*(i for i in range (100))),
# print()
# print((i for i in range (100))),
# tuple(list(i for i in range (100)))

#  set() setcomprehesion

# print(set([1,2,3]))

# a = {1, 2, 3}
# print(a)

# b={i for i in [1, 2, 3]}
# print(b)
# c={i:i for i in [1, 2, 3]}
# print(c)

# print({i*2 if i == 3 else i *3 for i in [1, 2, 3]})
# print({"hey", "bro", "hey"})


# enumerate

# print(list(enumerate("hey")))
# print(list(enumerate("heypython")))
# print(dict(enumerate("heypython")))

# for i, v in enumerate("hey"):
#     print(i), 
#     print("v", v)

# print()
# print({i for i in enumerate("hey")})
# print()
# print({i:v for i,v in enumerate("hey")})
# print()
# print({i for i,v in enumerate("hey")})
# print()

# print({v for i,v in enumerate("hey")})
# print()

# print({i + 1 : v for i,v  in enumerate("Hello World")})
# print({i + 10 : str(v) for i,v  in enumerate([666, 23, 55])})
# print({str(v) for index,v  in enumerate([666, 23, 55])})
# print(i for index,v  in [666, 23, 55])
# print([i for i in enumerate("hey")])
# print([(i,v) for i,v in enumerate("hey")])

# print({i:v for i, v in enumerate("Hello World")})
# print({(i,v) for i, v in enumerate("HHello world")})

# errorhandling error handling

# import sys
# def catch(func, handle = lambda e: e, *args, **kwargs)
#     try:
#         return func(*args, **kwargs)
#     except Exception as e:
#         return handle(e)
    

# eggs =  e(1, 5, 0, 5, 2)
# eggList = None 
# try:
#     eggList =[egg for egg in eggs]
#     # eggList = [catch(lambda: 1/egg) for egg in eggs]
    
# except:
#     print("Exception: " ,sys.exc_info()[0])

# print("eggList:  ", eggList)


# import sys
# def catch(func, handle = lambda e: e, *args, **kwargs):
#     try:
#         return func(*args, **kwargs)
#     except Exception as e:
#         return handle(e)
    

# eggs =  e(1, 5, 0, 5, 2)
# eggList = None 
# try:
#     # eggList =[egg for egg in eggs]
#     eggList = [catch(lambda: 1/egg) for egg in eggs]
    
# except:
#     print("Exception: " ,sys.exc_info()[0])

# print("eggList:  ", eggList)

# print (["hello" for i in range(10)])
# print (["hello" for  unused  in range(10)])
# print (["hello" for _ in range(10)])


# some_stuff = [("key", "value"), ("key2", "value")]
# print(some_stuff)


# # print(["hello" for key, value in some_stuff])
# print([key for key, value in some_stuff])
# print([value for key, value in some_stuff])
# print([value for _, value in some_stuff])

# new_list = [1,2,3, [],[], '',[], 5]
# print([x for x in new_list if x != []])
# print(list(filter(lambda x:x != [], new_list)))
# print([x for x in new_list if x])


# CLASSCLASSCLASSCLASS
# 2M Python Dev  How to use classses and oop in python
# mini project
# class Member:
    
#     def __init__(self, name, member_id):
#         self.name = name
#         self.number_id = member_id
#         self.book_borrowed = []
        
#     def borrow_books(self, book): 
#         if book.copies > 0:
#             self.book_borrowed.append(book.title)
#             book.update_copies(-1) 
#         else:
#             print(f"Sorry {self.name} we don't have {book.title}")
            
#     def return_book(self, book):
#         if book in self.book_borrowed:
#             self.book_borrowed.remove(book.title)
#             book.update_copies(1)
            
#         else: 
#             print(f'Sorry {self.name} you have\'t borrowed {book.title}')    
        
# class Book:
#     def __init__(self, tiltle, author, isbn, copies):
#         self.title = tiltle
#         self.author = author
#         self.isbn = isbn
#         self.copies = copies
        
#     def display_info (self):
#         return (f"\tTitle: {self.title}\n\tAuthor: {self.author}"
#                 f"\n\tISBN: {self.title}\n\tCopies: {self.copies}")
        
#     def update_copies(self, change):
#         self.copies += change
        
# book1 = Book("1984", "George Orwell", "12345", 5)
# book2 = Book("To kill a Mockingbird", "Harper Lee", "67890", 3)
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "54321", 4 )

# print(book3.display_info())
# print()

# # book3.update_copies(6)
# book3.copies += 9
# print(book3.display_info())

# member1 = Member("Alice", "M001")
# member2 = Member("Bob", "M002")

# print("Before Borrowing")
# print(book1.display_info())
# print()
# print(book2.display_info())


# print('_' * 50)
# # borrowing books
# member1.borrow_books(book1)
# member2.borrow_books(book2)

# print("After Borrowing")
# print(book1.display_info())
# print()
# print(book2.display_info())

# print('-' * 50)
# #returning books
# member1.return_book(book1)
# member2.return_book(book2)
# member2.return_book(book2)

# print("After returning")
# print(book1.display_info())
# print()
# print(book2.display_info())


# Ridwanray 
# Object Oriented Programming with Python - Full Course

# class User:
#     def __init__(self, email, age):
#         self.email = email
#         self.age = age


# user1 = User("1@gmail.com", 10)
# user2 = User("1@gmail.com", 10)

# print("Before updated: " , user1.email)
# user1.email = "3@gmail.com"
# print("After update: " , user1.email)

# import array
# for name in array.__dict__:
#     print(name)
    
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))    
    
    
    
    
    

        