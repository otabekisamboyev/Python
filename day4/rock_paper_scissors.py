import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissors]
index = random.randint(0, 2)
choice = int(input("Choose: 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if choice == 0:
    if index == 0:
        print(f"You pick: {choice}\n{rock}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nTie!")
    elif index == 1:
        print(f"You pick: {choice}\n{rock}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nYou Lose!")
    else:
        print(f"You pick: {choice}\n{rock}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nYou Win!")
elif choice == 1:
    if index == 0:
        print(f"You pick: {choice}\n{paper}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nYou Win!")
    elif index == 1:
        print(f"You pick: {choice}\n{paper}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nTie!")
    else:
        print(f"You pick: {choice}\n{paper}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nYou Lose!")
elif choice == 2:
    if index == 0:
        print(f"You pick: {choice}\n{scissors}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nYou Lose!")
    elif index == 1:
        print(f"You pick: {choice}\n{scissors}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nYou Win!")
    else:
        print(f"You pick: {choice}\n{scissors}\n"
              f"Computer pick: {index}\n{rock_paper_scissors[index]}\nTie!")
else:
    print("Wrong Insert!")
