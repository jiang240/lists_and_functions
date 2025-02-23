"""Program to keep track of vehicles for booking
Version 2 - error check and prevention"""

def int_check(question):
    """Function to check for valid integer"""
    number_ = ""
    while not number_:
        try:
            number_ = int(input(question))
        except ValueError:
            print("You must enter an integer")
    return number_

def available_check(num):
    """Function to check if a vehicle is available"""
    while True:
        for vehicle in available_vehicles:
            if vehicle[0]==num:
                available_vehicles.remove(vehicle)
                return vehicle
        num=int_check("That vehicle is not available. Please choose a different one: ")

available_vehicles=[[1,"Suzuki Van", 2],[2,"Toyota Corolla",4],[3, "Honda CRV", 4],
                [4, "Suzuki Swift", 4],[5, "Mitsibishi Airtrek", 4],
                [6, "Nissan DC Ute", 4],[7, "Toyota Previa", 7],
                [8, "Toyota Hi Ace", 12],[9 ,"Toyota Hi Ace", 12]]
booked_vehicles=[]

seat_num = int_check("Enter number of seats required (Type -1 to quit): ")
while seat_num!=-1 and available_vehicles!=[]:
    print("VEHICLE NUMBER - TYPE - NO. SEATS")
    for car in available_vehicles:
        note = ""
        if car[2] < seat_num:
            note=" - NOTE: Not enough seats"
        print(f"No. {car[0]} - {car[1]} - {car[2]} seats{note}")
    print()
    booked_vehicle=available_check(int_check("Enter a number to book: "))
    name=input("Enter your name: ").title()
    booked_vehicles.append([booked_vehicle, name])
    print(f"{booked_vehicle[1]} booked by {name}")
    print()
    seat_num=int_check("Enter number of seats required (Type -1 to quit): ")
print()
print("VEHICLES BOOKED TODAY")
for car in booked_vehicles:
    print(f"No. {car[0][0]} - {car[0][1]} - Booked by: {car[1]}")
