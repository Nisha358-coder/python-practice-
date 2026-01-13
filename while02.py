# level - 1 
# que 1  count digits
# a = int(input("enter the number - "))
# count = 0

# while a > 0:
#     count = count + 1
#     a = a // 10
# print(count)

# que 2 sum of digits 
# a = int(input("enter the number - "))
# s = 0 

# while a > 0:
#     s = s + a % 10
#     a = a // 10
# print(s)

#  que 3 product of digits 

# a = int(input("enter the number - "))
# product = 1 

# while a > 0:
#     product = product * (a % 10)
#     a = a // 10
# print(product)

#  que 4 reverse a number 
# a = int(input("enter the number - "))
# rev = 0 
# while a > 0:
#     rev = rev * 10 + a %10
#     a = a // 10
# print(rev)

#  que 5 palindrome check
# a = int(input("enter the number -"))
# copy = a 
# rev = 0 

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# if rev == copy:
#     print("your number is palindrome")
# else:
#     print("your number is not palindrome")

#  que 6 harshad number 
# a = int(input("enter the number- "))
# temp = a 
# digit_sum = 0

# while temp > 0:
#     digit_sum = digit_sum + (temp % 10)
#     temp = temp // 10
# if a % digit_sum == 0:
#     print("this is harshed number")
# else:
#     print("this is not a harshed number")

# que 7 strong number 
# n = int(input("enter the number - "))
# temp = n 
# strong_num = 0

# while temp > 0:
#     digit = temp % 10

#     fact = 1 
#     i = 1 

#     while i <= digit:
#              fact *= i

#              i += 1
    
#     strong_sum += fact
#     temp //= 10
# if strong_sum == n:
#    print("Strong Number")
# else:
#     print("Not Strong Number")

#  que 8 average until negative 
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