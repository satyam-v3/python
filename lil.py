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