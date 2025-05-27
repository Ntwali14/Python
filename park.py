#car parking and ticketing system

import random

ticket_ID = random.randint(1, 1000)

car_number = input("Enter your car number: ")
car_type = input("Enter your car type (small, medium, large): ").lower()

#function to calculate the parking fees
def calculate_parking_fee(car_type):
    if car_type == "small":
        return 100
    elif car_type == "medium":
        return 200
    elif car_type == "large":
        return 300
    else:
        return 0
    
#function to print the ticket
def print_ticket(ticket_ID, car_type, car_number, parking_fee):
    print("********** Parking Ticket **********")
    print("************************************")
    print("Ticket_ID: ", ticket_ID)
    print("Car_number: ", car_number)
    print("Car_type: ", car_type)
    print("Parking_fee: ", parking_fee)
    print("Thank you for parking with us!")

if car_type in ["small", "medium", "large"]:
    print("Your ticket number is: ", ticket_ID)
    parking_fee = calculate_parking_fee(car_type)
    print("Your parking fee is: ", parking_fee)
    print_ticket(ticket_ID, car_type, car_number, parking_fee)
    
else:
    print("Invalid car type. Please enter small, medium, or large.")
