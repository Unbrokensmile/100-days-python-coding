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
# your_choice:
yc = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if yc == 0:
    print(rock)
elif yc == 1:
    print(paper)
elif yc == 2:
    print(scissors)
    
print("Computer chose:")
cc = 0
import random

cc = random.randint(0, 2)
if cc == 0:
    print(rock)
elif cc == 1:
    print(paper)
elif cc == 2:
    print(scissors)

# judge
if cc == yc:
    print("Draw")
elif cc%3 == (yc+1)%3:
    print("You lose")
elif cc%3 == (yc+2)%3:
    print("You win")
