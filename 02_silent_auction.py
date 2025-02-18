"""Program to run a silent auction"""
def price_check(price_):
    """Function to check that a price is valid"""
    price=""
    while not price:
        try:
            price=float(input(price_))
        except ValueError:
            print(f"Please enter a valid price.")
    return price

bid=0
highest_bid=0
item=input("What is the auction for? ")
reserve=price_check("What is the reserve price? ")
print()
print(f"The auction for the {item} has started!")
print()
while bid!=-1:
    print(f"Highest bid so far is ${highest_bid:.2f}")
    bid = price_check("What is your bid? ")
    if bid ==-1:
        if highest_bid >= reserve:
            print(f"The auction for the {item} finished with a price of ${highest_bid:.2f}.")
        else:
            print(f"The highest bid of ${highest_bid:.2f} did not meet the reserve price, "
                  f"and the {item} was not sold.")
    elif bid <= highest_bid:
        print("Please place a higher bid.")
    else:
        highest_bid = bid
