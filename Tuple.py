#  que 1 sum and average of tuple 

# def sum_and_average_tuple(n, elements):
#     total = sum(elements)
#     Average = total /n
#     return total , Average

# n = 5 
# elements = (10,20,30,40,50)
# result = sum_and_average_tuple(n, elements)
# print("sum:",result[0])
# print("Average:",result[1])


#  que 2 remove element in tuple 

# def remove_element_from_tuple(n, elements, to_remove):
#     lst = list(elements)
#     if to_remove in lst:
#         lst.remove(to_remove)
#     return tuple(lst)

# n = 5 
# elements = (10,20,30,40,50)
# to_remove = 30
# result = remove_element_from_tuple(n, elements, to_remove)
# print(result)


#  que 3 check element existence 

# def check_element_existence(n, elements, search_element):
#     if search_element in elements:
#         print("Found")
#     else:
#         print("Not Found")

# n = 5
# elements = (10,20,30,40,50)
# search_elemnt = 30 

# check_element_existence(n,elements,search_elemnt)


#  que 4 maximum and minimum values 

# def max_min_tuple_elements(n, elements):
#     return max(elements), min(elements)
# n = 5 
# elements = (10,20,30,40,50)
# maximum , minimum = max_min_tuple_elements(n,elements)
# print("Maximum:" , maximum)
# print("Minimum:",minimum)


#  que 5 frequency count of tuple emenets 

# def frequency_count_tuple(n,elements):
#     freq = {}
#     for item in elements:
#         freq[item] = freq.get(item , 0) + 1 
#     for key , value in freq.items():
#         print(f"{key} : {value}")
# n = 6 
# elements = (10,20,10,30,20,10)
# frequency_count_tuple(n,elements)