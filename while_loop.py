# while loop 

# que 1 print each digit 
# a = int(input("enter your number - "))

# while a > 0:
#     print(a % 10)
#     a = a // 10 

# que 2 sum of digits
# a = int(input("enter your number - "))
# s = 0

# while a > 0:
#      s = s + a % 10
#      a = a // 10 

# print(f"your digits sum is {s}")


# que 3 reverse a digits number 
# a = int(input(" enter your number - "))
# rev = 0 

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(f"your reverse digit is {rev} ")

# que 4 palindrome number check

# a = int(input("enter your number - "))
# rev = 0 
# copy = a

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if rev == copy:
#     print("yes your number is palindrome")
# else:
#     print("sorry your number is not palindrome")

#  que 5 automorphic number 

# a = 9
# copy = a

# square = a ** 2 
# count = 0 

# while a > 0:
#     count = count + 1
#     a = a // 10
# extract = square % (10**count)

# if extract == copy:
#     print("your number is automophic")
# else:
#     print("sorry your number is not automorphic")

# questions practice 
# que 1 continuous number input and sum
# total = 0

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     total += n

# print(total)

# que 2 product of digits 

# a = int(input())
# product = 1 

# while a > 0:
#     product = product * (a % 10)
#     a = a // 10
# print(product)

# que 3 harshad number check 

# a = int(input())
# temp = a 
# digit_sum = 0

# while temp > 0:
#     digit_sum = digit_sum + (temp % 10)
#     temp = temp // 10
# if a % digit_sum == 0:
#     print("Harshad number")
# else:
#     print("not Harshad number")

#  que 4 average until negative input  
# total = 0
# count = 0

# while True:
#     n = int(input())
    
#     if n < 0:
#         break
    
#     total += n
#     count += 1

# if count == 0:
#     print(0)
# else:
#     print(total / count)

# que 4 strong number check
# n = int(input())
# temp = n
# strong_sum = 0

# while temp > 0:
#     digit = temp % 10
    
#     fact = 1
#     i = 1
#     while i <= digit:
#         fact *= i
#         i += 1
    
#     strong_sum += fact
#     temp //= 10

# if strong_sum == n:
#     print("Strong Number")
# else:
#     print("Not Strong Number")
