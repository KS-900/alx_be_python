income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
savings = income - expenses
monthlySavings = savings * 12 + (savings * 12 * 0.05)
print("Your monthly savings are $"+ str(income))
print("Projected savings after one year, with interest, is: $" + str(monthlySavings))