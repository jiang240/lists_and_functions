"""Program to keep track of speeding tickets"""

def speed_check(question):
    """Function to check an inputted speed is in int form"""
    speed_=""
    while not speed_:
        try:
            speed_=int(input(question))
        except ValueError:
            print("Enter speed in numbers, please.")
    return speed_

SPEEDS_FINES=[[1, 30], [10, 80], [15, 120], [20, 170], [25, 230], [30, 300],
              [35, 400], [40, 510], [45, 630]]
TO_ARREST=["James Wilson", "Helga Norman", 'Zachary Conroy']
fine_num=0
total_fines=0
all_speeders=[]
print("###########")
speeder_name = input("Enter name of speeder: ").title()
while speeder_name != "X":
    if speeder_name in TO_ARREST:
        print(f"{speeder_name.upper()} - WARRANT TO ARREST")
    over_speed=speed_check("Enter the km/h over speed limit: ")
    for speeds in SPEEDS_FINES:
        if over_speed >= speeds[0]:
            fine=speeds[1]
    print(f"{speeder_name} to be fined ${fine}")
    fine_num+=1
    all_speeders.append([speeder_name, over_speed])
    total_fines+=fine
    print("###########")
    print()
    print("############")
    speeder_name=input("Enter name of speeder: ").title()
print(f"Total fines: {fine_num}")
for speeder in all_speeders:
    print(f"{all_speeders.index(speeder)+1}) Name: {speeder[0]}   "
          f"  Amount over speed limit: {speeder[1]}km/h")
print(f"Total amount of fines: ${total_fines}")
