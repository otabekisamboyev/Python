row1 = ["🔳", "🔳", "🔳"]
row2 = ["🔳", "🔳", "🔳"]
row3 = ["🔳", "🔳", "🔳"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to treasure (column-row): ")
if int(position[0]) > len(treasure_map) or int(position[1]) > len(treasure_map):
    print("Position id out of range of map")
else:
    treasure_map[int(position[0]) - 1][int(position[1]) - 1] = "🪙"
    print(f"{row1}\n{row2}\n{row3}")