programming_dictionary = {
    "Bug": "An error...",
    "Function": "A peace of code..."
}
# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new item to dictionary
programming_dictionary["Loop"] = "The action..."
# print(programming_dictionary)

# Creating new empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a dictionary in a dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 25}
# }

# Nesting dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 25
    }
]
