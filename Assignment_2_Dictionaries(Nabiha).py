def InitCredentials():


    NewUser = {
        "salary" : MonthlySalary,
        "month" :CurrentMonth,
    }
    
    return NewUser

def SalarySplit():
    #action = "Below add the percentage of how you would split your salary "
    newExpense = ""
    Expenses = []

    while newExpense != "exit" or "":
        newExpense = input("Start adding your expenses or type exit and press Enter to finish the list of expenses : ")

        if newExpense != "exit" or "":
            percentage = int(input(f"Percentage of {newExpense} off your salary: "))
        
            expense = {
                "expenseType" : newExpense,
                "expensePercentage": percentage
                }
            
            Expenses.append(expense)
    
    return Expenses
def findTotal(Expenses):
    sum = 0

    for expense in Expenses:
        sum = sum + float(expense["expensePercentage"])/100
        #sum2 = finances["Total monthly expenses"] - sum
    return (sum)

List = []
action= None
MonthlySalary = float(input("Hi Nabiha!, Please add your monthly salary: "))
CurrentMonth = input("Enter the month that corresponds to the current salary: ")
AdditionalIncome = float(input("Beside your salary, add any additional income to your account or add 0 if not: "))
AdditionalSavedIncome = float(input("How much would you like to save in $ out of your additional income this month?"))
TotalIncome = (MonthlySalary + AdditionalIncome)
print("Total income for this month is ",TotalIncome )

while action != "no":
    
    finances = InitCredentials()
    finances["Expenses"] = SalarySplit()
    finances["Total monthly expenses"] = findTotal(finances["Expenses"])*float(MonthlySalary) +float(AdditionalSavedIncome)
    #finances["Expenses in $ for "] = findTotal(finances["Expenses"])
    finances["Total remainder of your salary"] = float(TotalIncome) - finances["Total monthly expenses"]
    finances["yearly expenses"] = finances["Total monthly expenses"] * 12
    finances["Additional Income you saved this month"] = AdditionalSavedIncome 
    finances["If your salary was doubled next year:P"] = float(MonthlySalary) * 2
    print(finances)
    List.append(finances)
    action = input("Would you like to create another sheet for another month?: ")

print(List)