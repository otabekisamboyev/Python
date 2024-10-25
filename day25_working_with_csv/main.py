# with open("weather-data.csv") as file:
#     content = file.readlines()
#     print(content)


# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         else:
#             continue
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather-data.csv')
# print(type(data))
# print(type(data["temp"]))


# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data['temp'].max())

# Get condition in columns
# print(data['condition'])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# temp_mon = int(monday.temp.iloc[0]) * 1.8 + 32
# print(temp_mon)

# Create dataframe from scratch
# dict_data = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(dict_data)
# # print(data)
# data.to_csv("new_data.csv")


data = pandas.read_csv('004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
dict_squirrels = {
    "fur color": ["Gray", "Black", "Red"],
    "count": [gray_squirrels_count, black_squirrels_count, red_squirrels_count]
}
data = pandas.DataFrame(dict_squirrels)
data.to_csv("squirrels.csv")
