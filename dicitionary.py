#  que 1 print unique element in array
# a = [1,1,1,1,2,2,6,6,8,8,8,8,8,8,9,9,9,9,5,5,5,5,3]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d.keys())


#  que 2 cont the frequency of array element 

# a = [1,1,1,3,3,3,6,6,7,8,9,9,9,4,4]
# d= {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


#  que 3 jewels and stone (leetcode que)

# jewels = "aA"
# stones = "aAAbbbb"

# d = {}

# for i in stones:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i] = 1
    
#     count = 0 

#     for i in d.keys():
#         if i in jewels:
#             count += d[i]
    
# print(count)


#  que 3 Pangram check (leetcode que)

# a = "thequickbrownfoxjumpsoverthelazydog"

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i] = 1 

# if len(d) == 26:
#             print("True")
# else:
#             print(False)
        

#  que 4 first letter appear twice (leetcode que)

# a = "abccdaaz"

# d = {}

# for i in a:
#     if i in d:
#         d[i]+= 1
#         if d[i] == 2:
#            print(i)
#            break
#     else:
#         d[i] = 1 

#  que 5 sum of unique element (leetcode que)

# a = [1,2,3,2]
# d = {}


# for i in a:
#     if i in d:
#         d[i]+= 1
#     else:
#         d[i] = 1
# sum = 0 

# for i in d:
#     if d[i] == 1:
#         sum = sum + i

# print(sum)

#  que 6 sort the people (leetcode que)

# names = ["Marry", "John", "Emma"]
# heights = [180,165,170]

# d = {}
# for i in range(len(names)):
#     d[names[i]] = heights[i]

# d = ((sorted(d.items(), key=lambda x: x[1] , reverse= reversed)))
# for i in range(len(d)):
#     names[i]=d[i][0]
# print(names)

#  que 7 checking two strings have same frequency map

# s1 = "aabbcc"
# s2 = "baccab"

# if len(s1) == len(s1):
#     d = {}

#     for i in s1:
#         if i in d.keys():
#             d[i] +=1
#         else:
#             d[i] = 1
    
#     for i in s2:
#         if i in d.keys():
#             d[i] -= 1
#         else:
#             print("there is extra element")
        
#     for i in d:
#         if d[i] != 0:
#             print("your elements are not same")
#             break
#     else:
#         print("strings are same")

# else:
#     print("not same")


#  que 8 find duplicate in array hashset

# a = [1,1,1,2,2,4,4,7,6,5,6,5,4,7,3,7,4,4,8,9,4,4,4]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1 
#     else:
#         d[i] = 1
# for i in d:
#     if d[i] > 1:
#         print(i)


#  que 9 most frequency even element (leetcode que)

# nums = [0,1,2,2,4,4,1]

# d= {}

# for i in nums:
#     if i % 2 == 0:
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1
# if not d:
#         print (-1)
# else:

#     max_f = max(d.values())
#     cand = [num for num , freq in d.items() 
# if freq == max_f]
#     print (min(cand))


#  que 10 intersection of two arrays 

# a = [1,2,2,1]
# b = [2,2]
# d = {}

# j = []
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# for i in d.keys():
#     if i in b:
#         j.append(i)
# print(j)