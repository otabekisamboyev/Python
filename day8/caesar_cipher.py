from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''My solution'''


def caesar(word, move, direction):
    chars = []
    if direction == 'decode':
        move *= -1
    elif direction == 'encode':
        pass
    else:
        return 'Wrong insert'
    for i in word:
        chars.append(i)
    for n in range(0, len(chars)):
        if chars[n] in alphabet:
            char = chars[n]
            index_alphabet = alphabet.index(char)
            move_char = index_alphabet + move
            chars[n] = alphabet[move_char]
        else:
            continue
    word = "".join(chars)
    return word


stop = True
while stop:
    direct = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    print(f"The {direct}d text is : {caesar(text, shift, direct)}")

    stop_loop = input("Type 'yes if you want to go. Otherwise type 'no: ")
    if stop_loop.lower() == 'no':
        stop = False
    elif stop_loop.lower() == 'yes':
        pass
    else:
        print("Wrong insert!")
        exit()

'''Teacher's solution
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)'''