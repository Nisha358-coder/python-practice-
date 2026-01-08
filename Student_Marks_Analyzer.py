marks = [23,64,97,37,27,58,97,57,86,35,45,97,88,68,90]
total = sum(marks)
average = total / len(marks)

for i in marks:
    if i >= 85:
        print(i,"-Topper")
    elif i>= 60:
        print(i,"-Pass")
    elif i>= 40:
        print(i, "-Good")
    else:
        print(i,"-Fail")
print ("class Average", average)