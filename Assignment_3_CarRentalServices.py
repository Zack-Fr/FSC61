class User:
    def __init__(self,name,password,user):
        self.name = name
        self.password = password
        self.user = user

class RequestOrder(User):
    def __init__(self, name, password, user, date, orderNumber):
        
        self.currentDate = date
        self.orderNumber = orderNumber
        super().__init__(name,password,user)       

class Vehicle:        
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rentalPrice = 0
        
    def getRental(self):
        return self.__rentalPrice
    def setRental(self , newRental):
        self.__rentalPrice = newRental

    def totalRentalCost(self, rentalDays):
        return self.__rentalPrice * rentalDays
    def display_info(self):
        print (f"Car Brand:{self.brand}")  
        print (f"Car Model:{self.model}")
        print (f"Car Year:{self.year}")
        # print (f"Car Seats:{veh1.seats}")
        # print (f"car Rental Price:{veh1.getRental}")

class Car(Vehicle):
    def __init__(self, brand, model, year, seatCapacity):
        self.seatCapacity = seatCapacity
        super().__init__(brand, model, year)
    def display_info(self):
        print (f"Car seats capacity:{self.seatCapacity}")
        #print (f"car Rental Price:{veh1.getRental}")
class Bike(Vehicle):
    def __init__(self, brand, model, year, engineCapacity):
        self.engineCapacity = engineCapacity
        super().__init__(brand, model, year)
    def display_info(self):
        print (f"Bike seats capacity:{self.engineCapacity}")
        #print (f"car Rental Price:{veh1.getRental}")
def createAccount():
    name = input("Enter your name that will be used in your account: ")
    password = input("Enter your password: ")
    user = name
    
    account = User(name,password,user)
    
    print(f"Created an account = {user}")
    
    return account
def createOrder():
    date = input("Add the current date: ")
    
    orderNumber = date
    print(f"Created an order number {orderNumber}" )
    
    rentalDays = input("how many days would you like to rent our services for? ")
    
    order = date, orderNumber, rentalDays, account
    orderList.append(order)
    
    return order

def prompt():
    print("======================")
    print("Welcome to SPEED rental services!")
    print("======================")
    print("Enter 0 to create an account")
    print("Enter 1 to create a new request order using a guest account")
    print("Enter 2 to view available vehicles")
    print("Enter 5 to exit")
    action = int(input("Choice: "))
    
    return action

veh1 = Car("Toyota", "Corolla", 2020, 5)
veh2 = Bike("Toyota", "Yamaha", 2025, 1200)

orderList = []    
action = ""
account = "guest"

while action != 5:
    action = prompt()
    
    if action == 0:
        account = createAccount()
    elif action == 1:
        orderNumber = createOrder()
        print(orderList)
    elif action == 2:
        veh1.display_info()
        veh2.display_info()