"""Program to keep track of details for a taxi"""
BASE_COST=10
MINUTE_COST=2

def yes_no_checker(answer):
    """Function to check an input is either yes or no"""
    while answer not in ["Y","Yes","N","No"]:
        answer=input("Please enter a yes/no answer: ").title()
    return answer

def num_checker(question):
    """Function to check an input is a number"""
    num=""
    while not num:
        try:
            num=float(input(question))
        except ValueError:
            print("Please enter minutes in number form")
    return num

trip_num=0
trip_total_min=0
total_cost=0
trip='Yes'
driver_name=input("What is the driver's name? ").title()
while trip not in ['No','N']:
    trip_minutes=num_checker("How many minutes did the trip take? ")
    trip_cost=BASE_COST+MINUTE_COST*trip_minutes
    print(f"This trip cost ${trip_cost:.2f}")
    trip_num+=1
    trip_total_min+=trip_minutes
    total_cost+=trip_cost
    print()
    trip=yes_no_checker(input("Do you want to enter a new trip? Yes or No: ").title())
print("="*40)
print(f"Driver {driver_name} had {trip_num} trips totalling {trip_total_min} minutes")
print(f"The average time of all trips was {trip_total_min/trip_num:.1f} minutes")
print(f"The total income for the day was ${total_cost:.2f}")
print(f"The average cost of all trips was ${total_cost/trip_num:.2f}")