#  que 1 symetric difference finder 

# def symmetric_difference_finder(n, set1, m, set2):
#     return  set(set1).symmetric_difference(set(set2))
# n = 4 
# set1 = [1,2,3,4]

# m= 4
# set2 = [3,4,5,6]
# result = symmetric_difference_finder(n, set1, m, set2)
# print(result) 


# que 2 remove duplicates using set

# def remove_duplicates_using_set(n, elements):
#     seen = set()
#     result = []
#     for item in elements:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# n = 8
# elements = [1,2,3,2,4,3,5,1]
# output = remove_duplicates_using_set(n,elements)
# print(output)

#  que 3 union , intersection , difference 
# def set_operations(n1, set1, n2, set2):
#     s1 = set(set1)
#     s2 = set(set2)
    
#     print(f"Union:",list(s1|s2))
#     print(f"Intersection:",list(s1&s2))
#     print(f"Difference:",list(s1 - s2))
    
# n1 = 5
# set1 = [10,20,30,40,50]

# n2 = 4
# set2 = [30,40,50,60]
# set_operations(n1, set1, n2, set2)


#  que 4 subset and superset check

# def check_subset_superset(n1,set1,n2,set2):
#     s1 = set(set1)
#     s2 = set(set2)

#     if s1 == s2:
#         print("set1 and set2 are equal")
#     elif s1.issubset(s2):
#         print("set1 is a subset of set2")
#     elif s1.issuperset(s2):
#         print("set1 is a superset of set2")
#     else:
#         print("No subset or superset relation")

# n1 = 3
# set1 = [1,2,3]
# n2 = 5
# set2 = [1,2,3,4,5]

# check_subset_superset(n1,set1,n2,set2)

#  que 5 check unique element

# def check_unique_elements(numbers):
#     if len(numbers) == len(set(numbers)):
#         return "Unique"
#     else:
#         return "Not Unique"
# n = int(input())
# numbers = list(map(int,input().split()))
# print(check_unique_elements(numbers))

