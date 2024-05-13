year = int(input("Which year do you wanna check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}-year is a leap year!")
        else:
            print(f"{year}-year is not a leap year!")
    else:
        print(f"{year}-year is leap year!")
else:
    print(f"{year}-year is not a leap year!")
