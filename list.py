#  que 1 sum & average of list 

# a = [10,20,30,40,50]
# sum = 0 
# for i in a:
#     sum = sum + i
# print(f"the sum of total number is {sum}")
# print(f"the average of total number is {sum/len(a)}")

# que 2 maximum element with index 

# a = [1,74,4,83,2,5,25,87,73,94,26]
# max = a[0]
# index = 0 
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i 
# print(f"your maximum element is {max} and index is {index}")

#  que 3 2nd maximum element 

# a = [1,74,4,83,2,5,25,99,73,94,26]
# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0 
# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = a[i]
#         index2 = i
#         index = i 
#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i 
# print(f"max is  {max} at index {index} and 2nd max  is {max2} at index {index2}")

#  que 4 check if list is sorted or not 
# a = [12,13,14,27,84,34,93]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#        continue
#     else:
#      print("your list is not sorted")
#      break

# else:
#     print("your list is sorted")

# que 5 left rotation by 1

# a = [10,20,30,40,50]

# for i in range(len(a)-1):
#     a[i],a[i+1] = a[i+1],a[i]
# print(a)
 
# que 6 right rotation by 1

# a = [10,20,30,40,50]

# for i in range(len(a)-1,0,-1):
#     a[i],a[i-1] = a[i-1],a[i]
# print(a)

# que 7 left rotation by k

# k = int(input("how many time you want to rotate"))
# a = [10,20,30,40,50]

# for i in range(k):
#     for i in range(len(a)-1):
#      a[i],a[i+1] = a[i+1],a[i]
# print(a)

# que 8 reverse list(In place)

# a = [10,20,30,40,50]
# b = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[b] = a[b],a[i]
#     b = b -1 
# print(a)

# que 9 linear search

# a = [12,63,84,83,9,2,46,16,2,82,92,27]
# search = 92

# for i in range(len(a)):
#     if a[i] == search:
#         print(f"element found at index {i}")
#         break

# else:
#        print("not such element exist")

#  que 10 binary sort 
# a= [25,834,827,3,9,3,9,2,947,933,84,29]
# search = 933

# start = 0 
# end = len(a)-1
# mid = (start + end)//2

# while start <= end:
#     if a[mid] == search:
#         print(f"element fount at index { mid}")
#         break 

#     elif a[mid]< search:
#         start = mid + 1
#         mid = (start + end)//2

#     elif a[mid]> search:
#         start = mid - 1
#         mid = (start + end)//2
# else:
#     print("sorry no such element exist")


 # que 11 bubble sort 

# a = [26,84,943,94,8,25,73,9,2,6828,93,8,78,89,6,5,6448,]

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#      if a[i]>a[i+1]:
#         a[i],a[i+1]=a[i+1],a[i]

# print(a)

# que 12 selection sort 

# a = [25,74,937,943,9,56,4,7,34,8,7,498]

# for i in range(len(a)-1):
#     j = i +1 
#     min = i
#     for k in range(j, len(a)):
#         if a[k] < a[min]:
#             min = k

#     a[i],a[min]=a[min],a[i]
# print(a)
