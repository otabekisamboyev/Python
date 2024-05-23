################# Scope #################

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")


# Local scope
# def poison():
#     poison_strength = 5
#     print(poison_strength)
#
#
# poison()
# print(poison_strength)

player_health = 12


def game():
    def drink_potion():
        potion_strength = 41
        print(player_health)
    drink_potion()


game()
print(player_health)


# There is no block scope
game_level = 3
enemies = [""]