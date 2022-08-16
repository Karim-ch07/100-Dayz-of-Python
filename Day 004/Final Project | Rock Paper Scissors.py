rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(choices[choice])

print("Computer chose:\n")
Comp_choice = random.randint(0,2)
print(choices[Comp_choice])

if choice == 0 and Comp_choice == 2:
  state = 'Win'
elif choice == 1 and Comp_choice == 0:
  state = 'Win'
elif choice == 2 and Comp_choice == 1:
  state = 'Win'
elif choice == Comp_choice:
  state = 'Draw'
else:
  state = 'Lose'

print(f"You {state}")
