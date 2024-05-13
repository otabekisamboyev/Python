print("Welcome to BMI calculator 2.0!")
height = float(input("Please, enter your height in meters: "))
weight = float(input("Please, enter your wight in kilograms: "))
bmi = round(weight / (height ** 2), 1)
if bmi < 18.5:
    print(f"Your BMI is {bmi},and you are underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi}, and you are normal weight!")
elif bmi < 30:
    print(f"Your BMI is {bmi}, and you are overweight!")
elif bmi < 35:
    print(f"Your BMI is {bmi}, and you are obese!")
else:
    print("You need clinical medicine")
