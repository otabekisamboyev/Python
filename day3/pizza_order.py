# small 15
# medium 20
# large 25
# pepperoni small +2
# pepperoni medium or large +3
# extra cheese any +1
print("Welcome to our Pizza center!")
bill = 0
size = input("Which size of pizza do you wanna buy? S. or M. or L. ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Something went wrong")
    exit()

pepperoni = input("Do you wanna add pepperoni? Y. or N. ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

cheese = input("Do you want extra cheese? Y. or N. ")
if cheese == "Y":
    bill += 1

print(f"\nYou chose {size} size of pizza")
print("Pepperoni: Yes") if pepperoni == "Y" else print("Pepperoni: No")
print("Cheese: Yes") if cheese == "Y" else print("Cheese: No")
print(f"Final bill: ${bill}")
