# que 1 check the number sign 
# def check_number_sign(num):
#     if num > 0:
#         return "positive"
#     elif num < 0:
#         return "negative"
#     else:
#         return "zero"
    
# num = int(input("enter your number - "))
# print(check_number_sign(num))

#  que 2 even number checker 
# def check_even_number(num):
#     if num % 2 == 0:
#         return "This is  even number"
#     else:
#         return " This is odd number"
# n = int(input("enter your number - "))
# print(check_even_number(n))

# que 3 add and display sum
# def add_number(a,b):
#     return(a+b)
# a = int(input("enter your number - "))
# b = int(input("enter your number - "))
# print(add_number(a,b))

#  que 4 multiplication table function 
# def print_table(n):
#     for i in range (1,11,1):
#         print(f"{n} x {i} = {n*i}")
# n = int(input("enter your number - "))
# print(print_table(n))


# que 5 count digits number 
# def count_digits_number(n):
#     if n == 0:
#         print(1)
#     n = abs(n)
#     count = 0
#     while n > 0:
#         count += 1
#         n //= 10
#     print(count)
# n = int(input("enter your number - "))
# print(count_digits_number(n))

#  que 6 sum of first n naturals 
# def natural_number(n):
#     if n <= 0:
#         return 0 
#     s = 0 
#     for i in range(1,n+1):
#         s = s + i 
#     return s 
# n = int(input("enter your number - "))
# print(natural_number(n))

# que 7 Reverse number function
# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         rev = rev *10 + n % 10
#         n = n // 10
#     return rev
# n = int(input("enter your number - "))
# print(reverse_number(n))


#  que 8 inner function multiply & square 
# def multiply_and_square(a, b):
#     def multiply(x,y):
#         return x * y
    
#     product = multiply(a,b)
#     return product * product 
# a = int(input("enter your number - "))
# b = int(input("enter the number - "))
# print(multiply_and_square(a,b))

#  que 9 Armstrong number function 
# def armstrong_number(n):
#     original = n 
#     digits = len(str(n))
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total += digit ** digits 
#         n //= 10
#         if total == original:
#             return " Armstrong number "   
#     else:
#         return " Not an Armstrong Number"
# n = int(input("enter the number - "))
# print(armstrong_number(n))

# que 10 recrusive number function 
# def recursive_number(n):
#     if n == 0:
#         return 0 
#     return n + recursive_number(n-1)
# n = int(input("enter your number - "))
# print(recursive_number(n))

# que 11 inverted triangle pattern 
# n = int(input("enter your number - "))
# for i in range(n , 0,-1):
#     print("*" * i)



    