from data import expenses
 
total = sum(expenses.values())

for i in expenses:
    if  i == "Food":
        print(f"you spend {expenses[i]} on food")
    elif i == "Travel":
        print(f"you spend {expenses[i]} on Traveling")
    elif i == "Shopping":
        print(f"you spend {expenses[i]} on shopping")
    elif i == "Entertainment":
        print(f"you spend {expenses[i]} on entertainment")