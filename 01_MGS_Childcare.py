"""Program to keep track of children in a childcare"""

HOUR_COST=12
choice=0
all_children=[]

def int_check(question):
    """Function to check for valid integer"""
    number_ = ""
    while not number_:
        try:
            number_ = int(input(question))
        except ValueError:
            print("You must enter an integer")
    return number_

def drop_off():
    """Function to process the dropping off of a child"""
    name=input("What is the name of the child you want to drop off? ").title()
    all_children.append(name)
    return f"{name} has been added to the roll."

def pick_up():
    """Function to process the picking up of a child"""
    child=input("Input name of child: ").title()
    while child not in all_children or child != "X":
        print(f"We don't seem to have {child} in our roll.")
        child=input(f"Check that the name is spelled correctly or press X to"
                    f" quit: ").title()
        if child=="X":
            return "You have not picked up any children."
    all_children.remove(child)
    return f"{child} has been removed from the roll."

def calc_cost():
    """Function to calculate the cost of a child staying"""
    hours=int_check("For how many hours will your child be with us? ")
    cost=hours*HOUR_COST
    return f"The cost for a child staying with us for {hours} hours is ${cost}."

def print_roll():
    """Function to print all children in roll"""
    print(f"Here are all the children currently on the roll: {all_children}")

print("*"*60)
print("Welcome to MGS Childcare")
print("What would you like to do? Please choose one of the items below")
print("*"*60)
while choice !=5:
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit system")
    print()
    choice=int_check("What would you like to do? (Number between 1 and 5): ")
    if choice==1:
        print(drop_off())
    elif choice==2:
        print(pick_up())
    elif choice==3:
        print(calc_cost())
    elif choice==4:
        print_roll()
    else:
        print("Goodbye")
