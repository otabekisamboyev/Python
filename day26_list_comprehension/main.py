# Task 1

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [number ** 2 for number in numbers]

# print(squared_numbers)


# Task 2
# result = [number for number in numbers if number % 2 == 0]

# print(result)


# Task 3
# with open("file1.txt") as file:
#     list1 = [int(line.rstrip()) for line in file]
#
# with open("file2.txt") as file:
#     list2 = [int(line.strip()) for line in file]
#
# result = [int(i) for i in list1 if i in list2]
# print(result)


# Task 4
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split()}
#
# print(result)


# Task 5
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 22,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 1.8) + 32 for day, temp_c in weather_c.items()}
print(weather_f)
