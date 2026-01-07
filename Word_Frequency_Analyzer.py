user = "I love python and I love coding"
user = user.lower()

d = {}
words = user.split()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)