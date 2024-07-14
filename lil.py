# print("hello jyoti")
# print("hello \"jyoti\"")
# print("hello \njyoti")
# print("hello jyoti \n aap kaisi ho?")
# print("hello jyoti \n\t aap kaisi ho?")

# a="hello"
# print(a)

# b=20
# print(b)

# a=input("Enter your value: ")
# print(a)

# name="jyoti"
# age=80
# print(f"Hey my name is {name} and I'm {age} years old.")

# integer=42       #int
# float=2.30        #float
# complex=2 + 3j   #complex

# print("Integer:",integer)
# print("Float:",float)
# print("Complex:",complex)

# a=True    #bool
# print("Boolean value:" ,a)

# d=None    #none
# print("None value :" ,d)

# c = b"jyoti"
# print("Byte:", c)

# print(type(integer))
# print(type(float))
# print(type(complex))
# print(type(a))
# print(type(d))
# print(type(c))

# a=int("1234")
# print(type(a))

# b=float(1234)
# print(type(b))

# # assigning value
# integer=42       #int
# float=2.30        #float
# complex=2 + 3j   #complex

# print("Integer:",integer)
# print("Float:",float)
# print("Complex:",complex)

# a=True    #bool
# print("Boolean value:" ,a)

# d=None    #none
# print("None value :" ,d)

# c = b"jyoti"
# print("Byte:", c)

# # type check
# print(type(integer))
# print(type(float))
# print(type(complex))
# print(type(a))
# print(type(d))
# print(type(c))

# # type conversion
# Integer=str(integer)
# Float=str(float)
# print("Integer type changes to" ,type(Integer))
# print("Float type changes to" ,type(Float))


#arthematic operators
# +, -, *, /, //, %, **

# a=5
# b=10

# c=a+b
# d=a-b
# e=a*b
# f=b/a
# g=b//a
# h=b%a
# i=a**b

# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)

#relational operators

# ==, !=, >, <, >=, <=

# result= (10==5)    #False
# print(result)
# result= (10!=5)    #true
# print(result)
# result= (10>5)    #true
# print(result)
# result= (10<5)    #False
# print(result)
# result= (10>=10)    #true
# print(result)
# result= (10<=5)    #False
# print(result)

# Logical Opetayors

# and, or, not.

# result= (True and False)
# print(result)

# result= (True or False)
# print(result)

# result= not False
# print(result)

# Bitwise Operators

# &, |, ^, ~, <<, >>

# result= 10&5      # 1010 & 0101 = 0000
# print(result)

# result= 10|5      # 1010 | 0101 = 1111
# print(result)

# result= 10^5      # 1010 | 0101 = 1111
# print(result)

# result=~10
# print(result)     # ~1010 = ......11110101

# result=10<<2      # 1010<<2=101000
# print(result)

# result=10>>2      # 1010>>2=10
# print(result)

# String Operators

# +, *, "in" and "not in"

# result="hello"+" "+"Jyoti"
# print(result)

# result="hello "*3
# print(result)

# result="H"in "Hello"
# print(result)
# result="H" not in "Hello"
# print(result)


# WAP to enter your fist name and last name  and print it in reverse order

# fname=input("Enter your first name : ")
# lname=input("Enter your last name : ")
# print(f"Hello {lname} {fname} 🥰")
# print("Hello"+" "+lname+" "+fname)

# WAP to find area and circumference of circle

# r=int(input("Enter radius : "))
# pi=3.14

# area=pi*r**2
# print("Area of circle : ",area)

# circf=2*pi*r
# print("Circumference of circle : ",circf)

# WAP to find area of triangle

# b=float(input("Enter the base of triangle : "))
# h=float(input("Enter height of triangle "))

# area=0.5*b*h
# print("Area of triangle : ",area)

# WAP to convert the temprature from degree celcius to farenhiet

# c=float(input("Enter the temperature : "))

# f=(c*9/5)+32

# print("Temperature in farenhiet is ", f)

## Conditional Statements   (if / elif / else)

# age = int(input("Enter your age: "))

# if age>=18:
#     print("You are Adult ")
# elif age>=13:
#     print("You are a teenager")
# else:
#     print("You are a child ")


# num = int(input("Enter a number: "))

# if num>0:
#     print("The number is positive")
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# else:
#     print("The number is not positive")

# To check if the no. is multiple of 5 & 7 both

# n=int(input("\033[33mEnter the number to check if the no is multiple of both 5 and 7: \033[0m"))
# if n%5==0 and n%7==0:
#     print("\33[32m", "Multiple of both 5 & 7", "\033[0m")
# else :
#     print("\033[31m", "Not multiple of both of 5 & 7" , "\033[0m")

## sasta calculator

# calc=input("Select the option to perform calculation\n a. add\n b. sub\n c. multiply\n d. divide\n")

# if calc=='a':
#     num1=int(input("Enter 1st number: "))
#     num2=int(input("Enter 2nd number: "))
#     print(f"Sum = {num1 + num2}")
# elif calc=='b':
#     num1=int(input("Enter 1st number: "))
#     num2=int(input("Enter 2nd number: "))
#     print(f"Difference = {num1 - num2}")
# elif calc=='c':
#     num1=int(input("Enter 1st number: "))
#     num2=int(input("Enter 2nd number: "))
#     print(f"Product = {num1 * num2}")
# elif calc=='d':
#     num1=int(input("Enter 1st number: "))
#     num2=int(input("Enter 2nd number: "))
#     print(f"Divide = {num1 / num2}")
# else:
#     print("Please select from the given options ")


## loops   while & for 
# start
#   |           <-
#   |             |
# condition----statement
#   |
#  end

## While loop

# count=1
# while count<=5:
#     print(count)
#     count+=1   #count = count+1

# i=3
# while i>0:
#     j=3
#     while j>0:
#         print(f"i:{i}, j: {j}")
#         j-=1
#     i-=1
#     print()

# WAP to find the sum of first n natural numbers using while

# n=int(input("Enter a positive integer: "))
# total=0
# i=1
# while i<=n:
#     total+=i
#     i+=1
# print(f"The sum of first {n} natural number is {total}")

# WAP to calculate the factorial of given number

# n=int(input("Enter a positive integer: "))
# factorial=1
# i=1
# while i<=n:
#     factorial*=i
#     i+=1
# print(f"The factorial of {n} is {factorial}")

# WAP where the user has to guess a secret number between 1 & 100. the program should keep asking the user to guess until they guess it right.

# import random
# secret_number= random.randint(1,100)
# guess = None
# while guess != secret_number:
#     guess = int(input("Guess the number between 1 & 100: "))
#     if guess < secret_number:
#         print("Too Low!")
#     elif guess > secret_number:
#         print("Too High!")
#     else:
#         print("Congratulations! You guessed it right.🥰")

# WAP that take any positive integer 'n' and prints the sequence according to the collatz conjecture. The conjecture is as follows: if n is even , divide it by 2; if n is odd, multiply it by 3 and add 1. repeat it until n becomes 1.

# n=int(input("Enter a positive number: "))
# while n!=1:
#     print(n,end=" ")  
#     if n%2==0:
#         n=n//2
#     else:
#         n=3*n+1
# print(n)

# WAP to take a positive integer and calculate the sum of its digit using a while loop.

# n=int(input("Enter a positive number: "))
# sum_of_digits = 0
# while n>0:
#     digit=n%10  
#     sum_of_digits += digit   
#     n=n//10  
# print(f"The sum of digits is {sum_of_digits}")

# WAP to reverse a given number using a while loop.

# n=int(input("Enter a positive number: "))
# reversed_number = 0
# while n>0:
#     digit=n%10
#     reversed_number = reversed_number*10+digit
#     n=n//10
# print(f"The reversed number is {reversed_number}")

# WAP that print the first'n' numbers in the fibonacci sequence using a while loop

# n=int(input("Enter a positive integer: "))
# a,b=0,1
# count=0
# while count<n:
#     print(a,end=" ") 
#     a,b=b,a+b
#     count+=1

# WAP to check if a given number is prime using a while loop

# num= int(input("Enter a positive integer: "))
# if num >1:
#     i=2
#     is_prime=True
#     while i<num:
#         if num%i==0 :
#             is_prime=False
#             break
#         i+=1
#     if is_prime:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")
# else:
#     print(f"{num} is not a prime number")

# WAP to keeps taking integer inputs from the user and adds them to a total sum until the user enters 0 . then print the sum total.

# total_sum=0 
# while True:
#     num=int(input("Enter a number (0 to stop): "))   
#     if num==0:
#         break
#     total_sum+=num
# print(f"The total sum is {total_sum}")

##  pattern using while

# n=int(input("Enter the number: "))
# i=0
# while i<n:#rows
#     j=0
#     while j<n:#columns
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=0
# while i<n:#rows
#     j=0
#     while j<n:#columns
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# while i<=n:#rows
#     j=1
#     while j<=n:#columns
#         print(n-j+1,end=" ")
#         j+=1
#     print()
#     i+=1

# n=int(input("Enter a number: "))
# i=1
# k=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(k,end=" ")
#         j+=1
#         k+=1
#     print()
#     i+=1


# n=int(input("Enter the number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1

# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# k=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         j+=1
#         k+=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(n-i+1,end=" ")
#         j+=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(n-j+1,end=" ")
#         j+=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# while i<=n: # rows
#     j=1
#     while j<=i: # spaces
#         print(" ",end=" ")
#         j+=1
#     j=n
#     while j>=i: # columns
#         print(j,end=" ")
#         j-=1
    
#     print()
#     i+=1

# n=int(input("Enter the number: "))
# i=1
# while i<=n:
#     k=i-1
#     while k:
#         print(" ",end=" ")
#         k-=1
#     j=n+1-i
#     while j>=1:
#         print(j,end=" ")
#         j-=1
#     print()
#     i+=1
    
# n=int(input("Enter the number: "))
# i=1
# while i<=n:
#     k=n-i
#     while k:
#         print(" ",end=" ")
#         k-=1

#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
    
#     l=i-1
#     while l:
#         print(l,end=" ")
#         l-=1

#     print()
#     i+=1

## special heart pattern

# n=int(input("Enter the value of n: "))
# col = 2*n-1
# row = col - (col-1)/2

# i=0
# while i<=n:
#     j=n-1
#     while j>=i:
#         print(" ",end=" ")
#         j-=1
#     j=i
#     while j>=1:
#         print("❤️",end=" ")
#         j-=1
#     j=i
#     while j>=1:
#         print("❤️",end=" ")
#         j-=1
#     j=n-1
#     while j>=i:
#         print(" ",end=" ")
#         j-=1
#     j=n-1
#     while j>=i:
#         print(" ",end=" ")
#         j-=1
#     j=i
#     while j>=1:
#         print("❤️",end=" ")
#         j-=1
#     j=i
#     while j>=1:
#         print("❤️",end=" ")
#         j-=1
#     print()
#     i+=1

# newR=2*row
# i=1
# while i <= newR:
#     j=0
#     while j<i:
#         print(" ",end=" ")
#         j+=1
#     j=newR+1-i
#     while j>1:
#         print("❤️",end=" ")
#         j-=1
#     j=newR+1-i
#     while j>1:
#         print("❤️",end=" ")
#         j-=1
#     print()
#     i+=1


## for loop

# fruits=["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)    

# range()

# for i in range(5):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# fruits=["apple","banana","cherry"]
# for i in range(len(fruits)):
#     print(f"Index: {i}, fruit: {fruits[i]}")

# numbers=list(range(5))
# print(numbers)

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()

# i=3
# while i>0:
#     j=3
#     while j>0:
#         print(f"i: {i}, j:{j}")
#         j-=1
#     i-=1
#     print()

# for i in range (1,6):
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# for i in range(5):#1,2,3,4
#     print(i)
# else:
#     print("sorry no i ")

# for i in range(6): #0, 1, 2, 3, 4, 5
#     print(i)
#     if i==4:
#         break
# else:
#     print("sorry no i ")

# continue 

# for i in range(1,10):# 1, 2, 3, 4, 5, 6, 7, 8, 9
#     if i%2==0:  # 2, 4, 6, 8
#         continue
#     print(i)

# break 

# for i in range (1,10):
#     if i==5:
#         break
#     print(i)

# pass

# for i in range (1,10):
#     if i%2==0:
#        pass
#     else:
#         print(i)

# WAP to print numbers from 1 to 10 usimg for loop

# for i in range(1,11):
#     print(i)

# WAP to find the sum of all elements in a list using for loop

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total+=num
# print(f"The sum of list is {total}")

# WAP to calculate the factorial of a given number using for loop

# n = int(input("Enter a positive number: "))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print(f"The factorial is {factorial}")

# WAP to reverse a string using for loop

# s=input("Enter a string: ") 
# reversed_string = " "
# for char in s:
#     reversed_string = char + reversed_string
# print(f"The reversed string is {reversed_string}")

# WAP to find the maximum in a list using for loop

# numbers = [3, 5, 2, 8, 1]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(f"The maximum number in a list is {max_num}")

# WAP to print the 'n' numbers in the fibonacci sequence uaing for loop

# n = int(input("Enter the number: "))
# a , b = 0 , 1
# for i in range(n):
#     print(a,end=" ")
#     a, b = b , a+b

# WAP to print all prime numbers between 1 to 50 using for loop

# for num in range(2,51):
#     is_prime = True
#     for i in range (2,int (num**0.5)+1):
#         if num%i==0:
#             is_prime = False
#             break
#     if is_prime :
#         print(num,end=" ")

# WAP to create a list of square of numbers from 1 to 10  using a for loop

# square = [i**2 for i in range(1,11)]
# print(square)

# WAP to  print multiplication table from 1 to 5 using nested for loop

# for i in range (1,6):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")
#     print()

# WAP to take a list of integers and print the sum of the digits of each numbers using a for loop

# numbers = [123, 456, 789]
# for num in numbers: 
#     sum_of_digits = 0
#     for digit in str(num): 
#         sum_of_digits += int(digit)
#     print(f"The sum of digits in {num} is {sum_of_digits}")

# WAP to count the occurance of each character in a string using for loop

# s = input("Enter a string: ")
# char_count = {}  
# for char in s:
#     if char in char_count:
#         char_count[char]+=1
#     else:
#         char_count[char]=1
# print(char_count)

# WAP to find the transpose of a 2x2 matrix using a nested  for loop

# matrix = [[1,2],[3,4]]
# transpose = [[0,0],[0,0]]

# for i in range (len(matrix)):
#     for j in range (len(matrix[0])):
#         transpose [j][i]= matrix[i][j]

# print("Orignal matrix: ")
# for row in matrix:
#     print(row)
# print("Transpose matrix: ")
# for row in transpose:
#     print(row)

# Pattern 

# n = int(input("Enter the no of rows: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the no of rows: "))
# for i in range (n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the no of rows: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the no of rows: "))
# for i in range(n,0,-1):
#     # spaces
#     for j in range(n-i):
#         print(" ",end=" ")
#     # stars
#     for k in range(i):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the no of rows: "))
# for i in range(1,n+1):
#     # spaces
#     for j in range(n-i):
#         print(" ",end=" ")
#     # stars
#     for k in range (i):
#         print("*",end=" ")
#     print()

###  Special pattern ###

# n = int(input("Enter the no of rows: "))

# # Upper portion
# for i in range(n,0,-1):
#     # upper left corner
#     for j in range(i):
#         print("*",end=" ")
#     # middle space
#     for k in range(n-i):
#         print(" ",end=" ")
#     for l in range(n-i):
#         print(" ",end=" ")
#     # upper right corner 
#     for m in range(i):
#         print("*",end=" ")
#     print()

# # Lower portion
# for i in range(1,n+1):
#     # lower left corner
#     for j in range(i):
#         print("*",end=" ")
#     # spaces
#     for k in range(n-i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(" ",end=" ")
#     # lower right corner
#     for m in range(i):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the no of rows: "))
# for i in range (1,n+1):
#     # spaces
#     for j in range(n-i):
#         print(" ",end=" ")
#     # stars
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the no of rows: "))
# for i in range (n,0,-1):
#     # spaces
#     for j in range(n-i):
#         print(" ",end=" ")
#     # stars
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# Pascal's Triangle

# n = int(input("Enter the no of rows: "))
# for i in range(n):
#     for j in range(n-i+1):
#         print(end=" ")
#     c = 1
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c = c*(i-j)//j
#     print()

# Sets
# {}, set()

# Using curley braces
# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# print(type(my_set))

# using the set() function
# another_set = set([1, 2, 3, 4, 5])
# print(another_set)

# creating an empty set (Using empty curly braces creates an empty dictionary)
# empty_set = set()
# print(type(empty_set))

# Operations

# Adding Elements
# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)

# Removing Elements
# my_set = {1, 2, 3, 4}
# my_set.remove(4)
# print(my_set)
# # my_set.remove(5)

# my_set.discard(3)
# print(my_set)
# my_set.discard(5)

# Union
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1|set2
# print(union_set)

# Intersection
# intersection_set = set1 & set2
# print(intersection_set)

# Difference
# difference_set = set1 - set2
# print(difference_set)

# Symetric difference
# sym_diff_set = set1 ^ set2
# print(sym_diff_set)

# Membership testing
# print(1 in set1)
# print(9 in set1)

# squares = {x**2 for x in range(1,6)}
# print(squares)

# numbers = [i for i in range(1,101)]
# evens = {x for x in numbers if x%2 == 0}
# print(evens)

# Tuples
# (), ','

# Using parenthesis
# my_tuple = (1, 2, 3)
# print(my_tuple)
# print(type(my_tuple))

# # Using commas
# another_tuple = 1,2,3
# print(another_tuple)
# print(type(another_tuple))

# # Single element
# single_element = 1,
# print(single_element)
# print(type(single_element))

# Basic Operations

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# con_tuple = tuple1 + tuple2
# print(con_tuple)

# tuple1 = (1, 2, 3)
# repated_tuple = tuple1 *5
# print(repated_tuple)

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[3])
# print(my_tuple[-1])

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1:4])
# print(my_tuple[:3])
# print(my_tuple[::2])

# Built-in Function

# len()
# my_tuple = (1, 2, 3, 4, 5)
# print(len(my_tuple))

# min() & max()
# my_tuple = (1, 2, 3, 4, 5)
# print(min(my_tuple))
# print(max(my_tuple))

# sum()
# my_tuple = (1, 2, 3, 4, 5)
# print(sum(my_tuple))

# my_tuple = (0,1)
# print(any(my_tuple))
# print(all(my_tuple))

# sorted()
# my_tuple = (5,2,4,1,3,0)
# print(sorted(my_tuple))

# Nested Tuples
# nested_tuples = (1, (2, 3), (4, (5, 6)))
# print(nested_tuples[1])
# print(nested_tuples[1][1])
# print(nested_tuples[2][1][1])

# Lists

# [], list()

# Using square barckets
# my_list = [1,2,3,4,5]
# print(my_list)
# print(type(my_list))

# Using list() fun
# another_list = list([1,2,3,4,5])
# print(another_list)

# Empty list
# empty_list = []
# print(empty_list)
# print(type(empty_list))

# Basic Operations
# Adding elements

# my_list = [1,2,3,4]

# my_list.append(5)
# print(my_list)

# my_list.extend([6,7])
# print(my_list)

# my_list.insert(2,"🫠")
# print(my_list)

# Removein Elements

# my_list = [1,2,3,4,5,6,7,8]

# my_list.remove(2)
# print(my_list)

# i = my_list.pop(4)
# print(my_list)
# print(i)

# my_list.clear()
# print(my_list)

# Modifying Elements

# my_list = [1,2,3]
# my_list[0] = 5
# print(my_list)

# Indexing & Slicing

# my_list = [1,2,3,4,5]
# print(my_list[0])
# print(my_list[-1])

# my_list = [1,2,3,4,5]
# print(my_list[1:4])
# print(my_list[:3])
# print(my_list[::2])

# Nested lists

# nested_list = [[1,2],[3,4],[5,6]]
# print(nested_list)
# # Assessing elements in a nested list
# print(nested_list[0][1])
# print(nested_list[2][0])

# List comprehension

# saquare = [x**2 for x in range(1,11)]
# print(saquare)

# Dictionaries
# {}, dict()

# Using curley braces
# my_dict = {'name':'Jyoti','age':40,'city':'jamshedpur'}
# print(my_dict)

# Using the dict()
# another_dict = dict(name = 'Jyoti', age = 40, city = 'jamshedpur')
# print(another_dict)

# Empty dict
# empty_dict = {}
# print(empty_dict)
# print(type(empty_dict))

# BAsic Operations
# Accessing Value

# my_dict = {'name':'Jyoti','age':40,'city':'jamshedpur'}
# print(my_dict['name'])
# print(my_dict['age'])

# Adding and Modifying

# my_dict = {'name':'Jyoti','age':40 }

# # Adding new key pair
# my_dict['city'] = 'Jamshedpur'
# print(my_dict)

# # Modifying 
# my_dict['age'] = 80
# print(my_dict)

# REmoving items
# my_dict = {'name':'Jyoti','age':40,'city':'jamshedpur'}

# # del()
# del my_dict['city']
# print(my_dict)

# # pop()
# age = my_dict.pop('age')
# print(my_dict)
# print(age)

# popitem()
# item = my_dict.popitem()
# print(my_dict)
# print(item)



# my_dict = {'name':'Jyoti','age':40,'city':'jamshedpur'}
# iterating through keys
# for key in my_dict:
#     print(key,my_dict[key])

# # iterating through values
# for value in my_dict.values():
#     print(value)

# Iterating through key values pairs
# for key,value in my_dict.items():
#     print(key,value)

# Built - in  fun

# my_dict = {'name':'Jyoti','age':40,'city':'jamshedpur'}
# print(len(my_dict))

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# my_dict.clear()
# print(my_dict)

# Comprenension
# squares = {x: x**2 for x in range(1,11)}
# print(squares)

# Arrays

# Using the 'array' module
# import array

# int_array = array.array('i',[1, 2, 3, 4])
# print(int_array)

# float_array = array.array('f',[1, 2, 3, 4])
# print(float_array)

# Using numpy
# import numpy as np

# np_array = np.array([1, 2, 3, 4])
# print(np_array)

# Indexing and Traversal

# Accessing Elements
# print(int_array[0])
# print(int_array[2])

# Traversing an array
# for elements in int_array:
#     print(elements)

# Manupulation

# Adding elements (using array module)
# int_array.append(5)
# print(int_array)

# Removing Elements  (using array module)
# int_array.remove(2)
# print(int_array)

# Adding Elements ( using numpy )
# np_array = np.append(np_array,[5,6])
# print(np_array)

# Removing Elements (Using numpy)
# np_array = np.delete(np_array,1)
# print(np_array)

# Strings

# my_string = "Hello world!"
# print(my_string)

# another_string = 'Python is bakwas'
# print(another_string)

# Indexing & Slicing
# Accessing character
# print(my_string[0])
# print(my_string[-1])

# Slicing strings
# print(my_string[0:5])
# print(my_string[7:])
# print(my_string[::-1])

# Built - in Functions

# len()
# print(len(my_string))

# str.upper()
# print(my_string.upper())

# str.lower()
# print(my_string.lower())

# str.replace()
# print(my_string.replace('world','Python'))

# str.split()
# print(my_string.split(' '))

# str.strip()
# whitespace_string = "    Hello,Jyoti!    "
# print(whitespace_string)
# print(whitespace_string.strip())

# str.find()
# print(my_string.find('World'))

# str.join()
# list_of_strings = ['hello','Jyoti','How','are','you?']
# print(" ".join(list_of_strings))

# Functions

# def function_name(parameters):
#     ''' Docstrings(optional): Describes the function '''
#     # Function Body
#     return #Value  ( Optional )

# def greet(name):
#     ''' Greet a person by name '''
#     return f"Hello!,{name}"

# print(greet("Jyoti"))

# def example_function(a,b,c=3,*args,**kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)

# example_function(1,2)
# example_function(1, 2, 3, 4, 5, 6, d=7, e=8)

# Return
# def add(a,b):
#     return a+b

# print(add(5,6))

# Yield
# def generate_numbers():
#     for i in range(5):
#         yield i

# gen = generate_numbers()
# print(next(gen))
# print(next(gen))

# None 
# def do_nothing():
#     pass

# result = do_nothing
# print(result)

# x = "global"

# def outer():
#     x = outer

#     def inner():
#         nonlocal x
#         x = "inner"
#         print("Inner: ",x)

#     inner()
#     print("Outer: ",x)    

# outer()
# print("Global: ",x)

# Recursion

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))

# Ananonyms function

# square = lambda x: x ** 2
# print(square(5))  # Output: 25

# # Lambda function with map
# nums = [1, 2, 3, 4]
# squared_nums = list(map(lambda x: x ** 2, nums))
# print(squared_nums)  # Output: [1, 4, 9, 16]

# def describe_person(name, age, city='Unknown'):
#     return f"{name} is {age} years old and lives in {city}"

# print(describe_person("jyoti",40, "Jamshedpur"))

# def concatenate(*args, separator=" "):
#     return separator.join(args)

# print(concatenate("Hello", "world", "!"))  # Output: Hello world !
# print(concatenate("Python", "is", "awesome", separator="-"))  # Output: Python-is-awesome

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# for number in countdown(5):
#     print(number)

# modules and Packages

# mymudule.py

# def greet(name):
#   return f"Hello {name}"

# def add(a,b):
#     return a+b

# import mymodule

# print(mymodule.greet("Alice"))
# print(mymodule.add(2,3))

# MODULE NAMESPACE

# mymodule.py
# x=10
# def show():
#     print(x)

# another_module.py
# x=20
# def display():
#     print(x)

# main.py
# import mymodule
# import another_module
# mymodule.show()
# another_module.display()

# Packages

# mypackage/
#     __init__.py
#     module1.py
#     module2.py

# module1.py
# def func1():
#     return "This is function 1"

# module2.py
# def func2():
#     return "This is function 2"

# __init__.py
# from.module1 import func1
# from.module2 import func2

# import mypackage

# print(mypackage.func1())
# print(mypackage.func2())

# Math module

# import math 
# print(dir(math))

# print(math.sqrt(16))
# print(math.pi)
# print(math.sin(math.radians(90)))

# Random module

# import random

# print(dir(random))
# print(random.random())
# print(random.randint(1,10))
# print(random.choice(["apple","banana","cherry"]))

# Emoji module

# import emoji

# print(dir(emoji))
# print(emoji.emojize("Python is fun :thumbs_up:"))
# print(emoji.demojize("python is fun 👍"))


# NumPy

# import numpy as np

# # creating arrays
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])

# # Element wise addition
# print(np.add(a,b))

# # Element-wise subtraction
# print(np.subtract(a,b))

# # Element-wise multiplication
# print(np.multiply(a,b))

# # Element-wise divide
# print(np.divide(a,b))

# # Element-wise power
# print(np.power(a,2))

# NumPy Array manipulation

# # Reshape
# c = np.array([[1, 2, 3],[4, 5, 6]])
# print(c.reshape(3,2))

# # Flatten
# print(c.flatten())

# # Concatenate
# d = np.array([[7, 8, 9],[10, 11, 12]])
# print(np.concatenate((c,d),axis=0))

# # Stack
# print(np.stack((c,d),axis=1))

# NumPy Statistical Function

# Array
# e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# # mean
# print(np.mean(e))

# # Standard Deviation
# print(np.std(e))

# # Variance
# print(np.var(e))

# # Sum
# print(np.sum(e))

# # min & max
# print(np.min(e))
# print(np.max(e))

# Pandas

# import pandas as pd
# import numpy as np

# # Creating Series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# # # Creating DataFrame

# data = {
#     'A' : [1, 2, 3, 4],
#     'B' : [5, 6, 7, 8],
#     'C' : [9, 10, 11, 12]
# }
# df = pd.DataFrame(data)
# print(df)

# # From list of lists
# data = [[1, 2], [3, 4], [5, 6]]
# df1 = pd.DataFrame(data,columns=['Column1', 'Column2'])
# print(df1)

# # From Dictionary
# data = {'column1':[1, 2, 3],'column2':[4, 5, 6]}
# df2 = pd.DataFrame(data)
# print(df2)

# # From NumPy Array

# data = np.array([[1, 2, 3], [4, 5, 6]])
# df3 = pd.DataFrame(data, columns=['A', 'B', 'C'])
# print(df3)

# # Formatting Data
# # Setting an index
# df.set_index('A', inplace = True)
# print(df)

# # Renaming columns
# df.rename(columns = {'B':'Column2', 'C' : 'Column3' }, inplace = True)
# print(df)

# # Applying Functions
# df['Column3'] = df['Column3'].apply(lambda x : x * 2)
# print(df)

# # Fundamental DataFrames Operations

# # Selecting a column
# print(df['Column2'])

# # Filtering Rows
# print(df[df['Column2']>5])

# # Grouping
# grouped = df.groupby('Column2').sum()
# print(grouped)

# # Merging 
# df1 = pd.DataFrame({'key':['A', 'B', 'C'], 'Value':[1, 2, 3]})
# df2 = pd.DataFrame({'key':['A', 'B', 'C'], 'value':[4, 5, 6]})
# merged = pd.merge(df1, df2, on = 'key', how = 'inner')
# print(merged)

# # Aggregation
# print(df.agg({'Column2':['sum','mean'], 'Column3':['min','max']}))

# File 

# # Opening
# file = open("/Users/satyamkumar/Documents/code/python/lil.py", mode = 'r', encoding='utf-8')

# # Closing
# file.close()

# # Alternatively using "with" Statement
# with open ("/Users/satyamkumar/Documents/code/python/Extras/ques", mode='r', encoding='utf-8') as file:
#     content = file.read()

# # Wrighting to files
# with open("/Users/satyamkumar/Documents/code/python/Extras/Test", mode = 'w', encoding = 'utf-8') as file:
#     file.write("Hello, world!\n")

# lines = ['line 1 \n', 'line 2 \n', 'line 3 \n']
# with open("/Users/satyamkumar/Documents/code/python/Extras/Test", mode = 'a', encoding = 'utf-8') as file:
#     file.writelines(lines)

# # Reading from Files

# # Reading the Entire File
# with open("/Users/satyamkumar/Documents/code/python/Extras/Test", mode = 'r', encoding = 'utf-8') as file:
#     content = file.read()
#     print(content)

# # Reading line by line
# with open("/Users/satyamkumar/Documents/code/python/Extras/Test", mode = 'r', encoding = 'utf-8') as file:
#     line = file.readline()
#     while line :
#         print(line.strip())
#         line = file.readline()

# # Reading all lines into a list
# with open("/Users/satyamkumar/Documents/code/python/Extras/Test", mode = 'r', encoding = 'utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

# Working with files using DataFrames (Pandas)

# Reading files into DataFrames
# import pandas as pd

# # Reading a csv file
# df = pd.read_csv('/Users/satyamkumar/Documents/code/expenses.csv')
# print(df.head())

# # Reading an Excel file
# df = pd.read_excel('/Users/satyamkumar/Desktop/SUMMER INTERNSHIP Student details.xlsx', sheet_name = 'Sheet1')
# print(df.head())

# # Reading a JSON File
# df = pd.read_json('') 
# print(df.head())

# # Wrighting DataFrames to files

# # Wrighting to a csv file
# df.to_csv('', index = False)

# # Wrighting to an Excel file
# df.to_excel('', sheet_name = 'Sheet1', index = False)

# # Wrighting to a JSON File
# df.to_json('', orient = 'records')

# Error and Exception Handling

# try:
#     lst=[1,2,3]
#     print(lst[5])
# except IndexError as e:
#     print(f"Caught an IndexError: {e} ")


# a = input(" Enter the number ")
# print(f" Multiplication table of {a} is : ")
# try:
#     for i in range(1,11):
#         print(f" {int(a)} x {i} = {int(a) * i} ")
# except Exception as e :
#     print(f"Invalid Input : {e} ")


# # User-defined Exception
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# try:
#     raise CustomError(" This is a custom error ")
# except CustomError as e:
#     print(f"Caught a custom error: {e} ")

# # Catching Exceptions
# try:
#     x = int(input(" Enter a number "))
#     y = 10 / x
# except ZeroDivisionError as e :
#     print(f" Error: Division by Zero is not allowed. {e} ")
# except ValueError as e :
#     print(f" Error: Invalid Input. {e} ")
# else:
#     print(f" Result: {y} ")
# finally:
#     print(" THIS BLOCK IS ALWAYS EXECUTED")

# # Raising Exceptions
# def Check_positive(number):
#     if number <= 0:
#         raise ValueError (" Number Must be +ve ")
#     return number

# try :
#     Check_positive(-10)
# except ValueError as e :
#     print(f" Exception raised : {e} ")

# leetcode 7 No. 

# n = int (input("Enter the nuber: "))
# reverse = 0
# while n!=0:
#     digit = n%10
#     reverse = (reverse * 10) + digit
#     n = n // 10
# print (reverse)
















