#Exercise 11) Exercise 1: Movie Ticket Price CalculatorWrite a Python program that asks the user for their age and 
# determines the price of a movie ticket based on the following rules:
# If the user is , the ticket costs .
# If the user is , the ticket costs .
#- If the user is , the ticket costs .

age = int(input("How old are you?"))

if age >= 18:
    price = 5 
elif age >=25:
    price = 10
elif age >= 60:
    price = 50
elif age >= 35: 
    price = 25
else:
    price = 0
    print("You are not eligible for a ticket")

print(f"The ticket price is $ {price}")

#Exercise 2
#Write a Python program that asks the user to enter a number and checks whether it is even or odd.
i = int(input("Please add your desired number: "))
if i%2 == 0:
    print ("Your number is even")
elif i%2 != 0:
    print("Your number is odd")

#Exercise 3
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Access Granted")
else:
    print("Access Denied")


