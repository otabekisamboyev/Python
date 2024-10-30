import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_dict = data.letter.to_dict()
code_dict = data.code.to_dict()
name = input("Enter a name: ")
name_dict = {}
for letter in name:
    if letter.upper() in letter_dict.values():
        name_dict[letter.upper()] = list(code_dict.values())[list(letter_dict.values()).index(letter.upper())]
print(name_dict)
