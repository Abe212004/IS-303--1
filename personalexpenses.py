#Variables
lExpenses = []
iSmall = 0
iModerate = 0
iLarge = 0

#Prompt user to enter their expenses (Make sure that expenses are valid numbers and not negative)
fExpense = float(input("Enter an expense (or enter 0 to finish):"))
while fExpense !=0:
    if fExpense < 0:
        print("Expenses can't be negative. Please try again.")
    else:
        lExpenses.append(fExpense)
    fExpense = float(input("Enter an expense (or enter 0 to finish):"))


#Ensures that at least one expense was entered.
if len(lExpenses) == 0:
    print("No expenses were entered.")
else:

#Classify the expenses.
    for fItem in lExpenses:
        if fItem < 25:
            iSmall += 1
        elif fItem >= 25 and fItem <= 100:
            iModerate += 1
        else:
            iLarge += 1

#Calculate totals
iCount = len(lExpenses)
fTotal = sum(lExpenses)
fAverage = fTotal/iCount

#Print the results
print(f"Total number of expenses: {iCount}")
print(f"Total expenses: ${fTotal:.2f}")
print(f"Average expense: ${fAverage:.2f}")
print(f"Smallest expense: ${min(lExpenses):.2f}")
print(f"Largest expense: ${max(lExpenses):.2f}")
print(f"Number of small expenses: {iSmall}")
print(f"Number of moderate expenses: {iModerate}")
print(f"Number of large expenses: {iLarge}")
