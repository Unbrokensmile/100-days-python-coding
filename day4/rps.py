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
yc = 0
onetwothree = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if onetwothree == 0:
    print(rock)
    yc = 1
elif onetwothree == 1:
    print(paper)
    yc = 2
elif onetwothree == 2:
    print(scissors)
    yc = 3
    
print("Computer chose:")
cc = 0
import random

rrrr = random.randint(0, 2)
if rrrr == 0:
    print(rock)
    cc = 1
elif rrrr == 1:
    cc = 2
    print(paper)
elif rrrr == 2:
    cc = 3
    print(scissors)

# judge
if cc == 1 and yc == 3 \
    or cc == 2 and yc == 1 \
    or cc == 3 and yc == 2:
    print("You lose")
elif cc == yc:
    print("Draw")
elif cc == 1 and yc == 2 \
    or cc == 2 and yc == 3 \
    or cc == 3 and yc == 1:
    print("You win")
