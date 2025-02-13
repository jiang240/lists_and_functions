"""Program to keep track of children in a childcare"""

HOUR_COST=12
choice=6
all_children=[]
def drop_off():
    name=input("What is the name of the child you want to drop off? ").title()
    all_children.append(name)
    print(f"{name} has been added to the roll.")

def pick_up():
    pass

def calc_cost():
    pass

def print_roll():
    print(f"Here are all the children currently on the roll: {all_children}")

while choice!=5:
    print("*"*60)
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("*"*60)
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit system")
    print()
    choice=int(input("What would you like to do? (Number between 1 and 5): "))
    if choice==1:
        drop_off()
    elif choice==2:
        pick_up()
    elif choice==3:
        calc_cost()
    elif choice==4:
        print_roll()
    else:
        print("Goodbye")