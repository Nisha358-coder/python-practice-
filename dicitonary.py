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