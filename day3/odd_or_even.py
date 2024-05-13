print("Program that find the number is odd or even!")
number = int(input("Enter the number: "))
if number < 0:
    print("You entered minus sign number!")
elif number == 0:
    print("You entered 0!")
else:
    if number % 2 == 0:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")
