names = []
invite_letter = ''

with open("./input/Names/invited_names.txt", mode="r") as file:
    for line in file:
        name = line.strip()
        names.append(name)

print(names)
with open("./input/Letters/starting_letter.txt", mode="r") as file:
    invite_letter = file.read()
for name in names:
    personalized_letter = invite_letter.replace("[name]", name)
    with open(f"./output/ReadyToSend/starting_letter_{name}.txt", mode="w") as letter_file:
        letter_file.write(personalized_letter)
