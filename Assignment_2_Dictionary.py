def InitCredentials():
    MonthlySalary = input("Hi Nabiha!, Please add your monthly salary: ")
    CurrentMonth = input("Enter the month that corresponds to the current salary: ")

    NewUser = {
        "salary" : MonthlySalary,
        "month" :CurrentMonth,
    }
    
    return NewUser

def SalarySplit():
    #action = "Below add the percentage of how you would split your salary "
    newExpense = ""
    Expenses = []

    while newExpense != "exit":
        newExpense = input("Expense type: ")

        if newExpense != "exit":
            percentage = int(input(f"Percentage of {newExpense}: "))

            expense = {
                "expenseType" : newExpense,
                "expensePercentage": percentage
                }
            
            Expenses.append(expense)
    
    return Expenses
def findTotal(Expenses):
    sum = 0

    for expense in Expenses:
        sum = sum + expense["expensePercentage"]/100

        return  sum

List = []
action= None

while action != "no":
    finances = InitCredentials()
    finances["Expenses"] = SalarySplit()
    finances["total"] = findTotal(finances["Expenses"])

    List.append(finances)
    action = input("Would you like to create another sheet: ")

print(List)