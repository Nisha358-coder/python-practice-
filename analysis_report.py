from students_marks import students_marks

result = {}
total = 0

for marks in students_marks:
    total += marks 

    if marks >= 75:
        category = "doing very well"
    elif marks >= 45 :
        category = "doing okay"
    else:
        category = "struggling"
result[category] = result.get(category , 0) + 1
average = total /len(students_marks)
print("class average:", average)
print("class performance summary :")
print(result)