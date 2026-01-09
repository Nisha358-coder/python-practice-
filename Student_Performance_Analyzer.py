students_marks = [23,56,96,87,46,46,75,46,97,58,64,88,98,95,32,11,77,89,75,99]

result = {}
total = 0

for marks in students_marks:
    total += marks

    if marks  >= 75:
        category = "doing very well"
    elif marks >= 45:
       category = " doing okay"
    else:
        category = " struggling"
result[category] = result.get(category , 0) + 1
average = total /len(students_marks)
print("class average:", average)
print("class performance summary :")
print(result)