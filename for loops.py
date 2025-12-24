# for i in range(10,41,1):
#     print(i)

# for i in range(-10,21,1):
#     print(i)

# for i in range(34,4,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)

# questions of for loops 
# que 1

# n = int(input("please tell me how many times you want to print:"))

# for i in range(n):
#     print("have dinner??")

# que 2 
# n = int(input("tell me the number"))

# for i in range(1,n+1):
#     print(i)

# que 3 
# n = int(input("tell me the number"))

# for i in range(n,0,-1):
#      print(i)

# que 4
# n = int(input("till me the number for sum"))

# s = 0 

# for i in range(1,n+1):
#     s = s+i
# print(f"your sum is {s}") 

# que 5 
# n = int(input("tell me your number:-"))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact*i
# print(f"your factorial is {fact}")

# que 6

# n = int(input("tell me your range :-"))

# even_sum = 0
# odd_sum = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print(f"the even number is {even_sum} the odd number is {odd_sum}")

#que 7

# n = int(input("tell me your number to check the factors:-"))

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

# que 8

# n = int(input("tell me your number to sum of all factors:-"))
# s = 0

# for i in range(1,n+1):
#     if n % i == 0:
#          s = s + i
# print(f"this is your sum {s}")

# que 9

# a = int(input("tell me your value:-"))
# b = int(input("tell me your exponent:-"))
# power = a

# for i in range(b-1):
#     power = power * a
# print(f"this is your answer{power} ")

# que 10
# n = int(input("tell me your number:-"))
# count = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         count = count + 1
# if count == 1:
#     print("your number is unity number")
# elif count == 2:
#     print("your number is prime number")
# else:
#     print("your number is not prime number")



# more que for better understand 
# que1

# for num  in range(1,11):
#     print(num)

# que 2
# for i in range(0, 21):
#     if i % 2 == 0:
#         print(i)

# que 3 
# for ch in "PYTHON":
#     print(ch)

# que 4
# colors = ["red", "green", "blue", "yellow"]

# for c in colors:
#     print(c)
 
# que 5
# for i in range(5,51):
#     if i % 5 == 0:
#         print(i)

# medium one's

# que1 

# n = 0
# for i in range(1,51):
#     n += i
# print(n)

# que 2 

# nums = [3, 7, 9, 2, 5]

# largest = nums[0]

# for n in nums:
#     if n>largest:
#         largest = n
# print(largest)

# que3

# text = "beautiful day"
# vowels = "aeiou"
# count = 0 

# for ch in text:
#     if ch in vowels:
#         count += 1
# print(count)


# que 4 

# for i in range(10 ,0,-1):
#     print(i)

# que 5 

# for i in range(1,11):
#     print(i*i)

# again for loop que 

# que 1 

# n = int(input("how many times oyu want to print - "))

# for i in range(n):
#     print(f" {i}hello world")

# code 1
# n = (input("enter the number - "))
# s = 0

# for ch in n:
#     if ch != '-':
#      s = s + int(ch)
# print(s)

# easy level que 1 

# que 1 
# for i in range(1,11,1):
#     print(i)

# que 2
# for i in range (10 ,0 ,-1):
#     print (i)

# que 3 

# for i in range(1,51,1):
#     if  i % 2 == 0:
#         print(i)

# que 4 

# for i in range(1,51,1):
#     if i % 2 != 0:
#         print(i)

# que 5 

# for i in range(1,11,1):
#     print(i * i)

# level 2 
# que 6
# n = int(input("tell me your number - "))
# s = 0 

# for i in range (1, n+1):
#     s = s + i 
# print(s)

# que 7
# n = int(input("tell me your number - "))
# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# que 8
# n = int(input("tell me your number - "))
# count = 0
# for i in range(1,n+1):
#     if i % 3 == 0:
#         count = count + 1

# print(count)

# que 9 
# n = int(input("give me the table of - "))

# for i in range(1,11):
#     print(n, "x", i, "=", n * i)


# que 10

# a = [3,73,8,47,178,276,34]
# lar = a[0]
# for i in range(len(a)):
#     if a[i]>lar:
#         lar = a[i]

# print(f"this is the largest value{lar}")

# level 3 

# que 11 Calculate the sum of digits of a number

# n = (input("enter the number - "))
# s = 0

# for ch in n:
#     if ch != '-':
#         s = s + int(ch)
# print(s)

# que 12  Count even and odd digits in a number
# n = int(input("tell me your number - "))


# for i in range(1,n+1):
#     if i % 2 == 0:
#         print (i,"is even number")
#     else:
#         print(i,"is odd number")

# que 13 Find the product of digits of a number

# n = (input("tell me your number - "))
# product= 1 

# for ch in n:
#     if ch != '-':
#         product = product * int(ch)
        
# print(product)

#  que 14  Check whether a number is an Armstrong number

# n = input("Enter a number: ")
# length = len(n)

# sum_val = 0

# for ch in n:
#     sum_val = sum_val + int(ch) ** length

# if sum_val == int(n):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# que 15  Print all prime numbers in a given range

# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))

# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(num)


#  level 3 
#  que 12 Reverse a string using a for loop.
# s = (input ("enter the string - "))
# rev = " "
# for ch in s:
#     rev = ch + rev 
# print(rev)


# level 5 
# que 21 Find the sum of elements in a list

# a = [3, 73, 8, 47, 178, 276, 34]
# total = 0 

# for x in a:
#     total = total + x
# print(total)

#  que 22 Count how many elements are greater than a given number

# a = [10, 20, 5, 30, 15]
# num = 50 

# count = 0 

# for x in a:
#     if x> num:
#         count = count + 1
# print(count)

#  que 23 Remove all negative numbers from a list
# a = [2, -3, 4, -1, 5]
# new_list = []

# for x in a:
#     if x >= 0:
#         new_list.append(x)

# print(new_list)

# que 24 Find the second largest element in a list
# a = [3, 7, 2, 9, 5]

# largest = a[0]
# second_largest = a[0]

# for x in a:
#     if x > largest:
#         second_largest = largest
#         largest = x
#     elif x > second_largest and x != largest:
#         second_largest = x

# print(second_largest)


#  que 25 Count how many times an element appears in a list

# a = [1, 2, 3, 2, 4, 2]
# element = 2

# count = 0

# for x in a:
#     if x == element:
#         count = count + 1

# print(count)


# revise 5 que 
# que 1 print number 1 to 50 
# for i in range(1,51,1):
#     print(i)

# que 2 Find the factorial of a given number
# n = int(input("enter the number - "))
# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i 
# print(fact)

# que 3 Reverse a string using a for loop
# s = input("enter the string - ")
# rev = " "

# for ch in s:
#     rev = ch + rev 
# print(rev)

# que 4 Calculate the sum of digits of a number
# n = (input("enter the number - "))
# sum = 0 

# for ch in n:
#     sum = sum + int(ch)
# print(sum)

# que 5 Find the sum of elements in a list

# a = [1,6,8,3,9]
# sum = 0 

# for ch in a:
#     sum = sum + int(ch)
# print(sum)

# n = (input("enter your string"))
# rev = " "

# for ch in n:
#     rev = ch + rev
# print(rev)

# more questions 
# que 1
# n = str(input())
# vowels = "aeiou"
# count = 0 

# for ch in n :
#     if ch in vowels:
#         count = count + 1 
# print(count)

# que 2 
# n = str(input("enter the number - "))
# count = 0

# for ch in n:
#     if int(ch) % 2 == 0:
#         count = count + 1

# print(count)

# que 5 Find the largest digit in a number

# n = str(input("enter the number - "))
# largest = 0

# for ch in n:
#     if int(ch) > largest:
#         largest = int(ch)
# print(largest)

# que Count how many digits are greater than 5 in a number

# n = str(input("enter the number - "))
# count = 0 
# largest = 5 

# for ch in n:
#     if int(ch)>5:
#         count = count + 1
# print(count)


#  que Find the sum of odd digits in a number

# n = str(input("enter the number -"))
# sum = 0

# for ch in n:
#     if int(ch) % 2 != 0:
#         sum = int(ch) + sum
     
# print(sum)

#  que Count how many words are in a sentence

# Remove all vowels from a string

# Check whether a string has any digit in it


n = str(input("enter the sentence - "))
count  = 0

for ch in n:
    if ch == ' ' :
        count = count + 1 

print(count)
