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

    # def totalRentalCost(self, rentalDays):
    #     return self.__rentalPrice * rentalDays
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
        super().display_info()
        print (f"Car seats capacity:{self.seatCapacity}")
        #print (f"car Rental Price:{veh1.getRental}")
class Bike(Vehicle):
    def __init__(self, brand, model, year, engineCapacity):
        self.engineCapacity = engineCapacity
        super().__init__(brand, model, year)
    def display_info(self):
        super().display_info()
        print (f"Bike engine capacity:{self.engineCapacity}cc")

def show_vehicle_info(vehicle):
    vehicle.display_info()
def createAccount():
    name = input("Enter your name that will be used in your account: ")
    password = input("Enter your password: ")
    user = name
    
    account = User(name,password,user)
    
    print(f"Created an account = {user}")
    
    return account
def createOrder():
    date = input("Add the current date: ")
    
    print("Choose a vehicle:")
    print("1. Car - Toyota Corolla")
    print("2. Bike - Yamaha")
    
    vehicle_choice = int(input("Enter your choice (1 or 2): "))
    
    rentalDays = input("how many days would you like to rent our services for? ")
    
    if vehicle_choice == 1:
        selected_vehicle = car1
    elif vehicle_choice == 2:
        selected_vehicle = bike1
    else:
        print("Invalid choice. Defaulting to Car.")
        selected_vehicle = car1
        
    totalRental = selected_vehicle.getRental() * int(rentalDays)
    orderNumber = date
    print(f"Created an order number {orderNumber}" )
    print(f"Total Rental Cost for {selected_vehicle.brand} {selected_vehicle.model}: ${totalRental}")
    
    
    order = (date, orderNumber, rentalDays, account , totalRental)
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

car1 = Car("Toyota", "Corolla", 2020, 5)
car1.setRental(50)

bike1 = Bike("Toyota", "Yamaha", 2025, 1200)
bike1.setRental(50)

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
        car1.display_info()
        bike1.display_info()
        