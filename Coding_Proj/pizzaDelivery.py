
print("Welcome to Python Pizza Deliveries")
size = input("What size do you want? (S|M|L)").upper()
add_pepperoni = input("Do you want to add pepperoni? (Y|N)").upper()
add_cheese = input("Do you want to add cheese? (Y|N)").upper()


PRICE_S = 15
PRICE_M = 20
PRICE_L = 25

final_bill = 0

if size == "S":
    final_bill = PRICE_S
elif size == "M":
    final_bill = PRICE_M
else:
    final_bill = PRICE_L


if add_pepperoni == "Y":
    if size == "S":
        final_bill += 2
    elif size == "M" or size == "L":
        final_bill += 3

if add_cheese == "Y":
    final_bill += 1

print(f'Your final bill is: {final_bill}')

        



