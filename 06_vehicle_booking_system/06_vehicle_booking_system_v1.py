"""Program to keep track of vehicles for booking
Version 1 - basic working program"""

available_vehicles=[[1,"Suzuki Van", 2],[2,"Toyota Corolla",4],[3, "Honda CRV", 4],
                [4, "Suzuki Swift", 4],[5, "Mitsibishi Airtrek", 4],
                [6, "Nissan DC Ute", 4],[7, "Toyota Previa", 7],
                [8, "Toyota Hi Ace", 12],[9 ,"Toyota Hi Ace", 12]]
booked_vehicles=[]

seat_num = int(input("Enter number of seats required (Type -1 to quit: "))
while seat_num!=-1:
    print("VEHICLE NUMBER - TYPE - NO. SEATS")
    for car in available_vehicles:
        note = ""
        if car[2] < seat_num:
            note=" - NOTE: Not enough seats"
        print(f"No. {car[0]} - {car[1]} - {car[2]} seats{note}")

    booking_num=int(input("Enter a number to book: "))
    for vehicle in available_vehicles:
        if vehicle[0]==booking_num:
            booked_vehicle=vehicle
            available_vehicles.remove(vehicle)
    name=input("Enter your name: ").title()
    booked_vehicles.append([booked_vehicle, name])
    print(f"{booked_vehicle[1]} booked by {name}")
    print()
    seat_num=int(input("Enter number of seats required (Type -1 to quit: "))
print("VEHICLES BOOKED TODAY")
for car in booked_vehicles:
    print(f"No. {car[0][0]} - {car[0][1]} - Booked by: {car[1]}")
