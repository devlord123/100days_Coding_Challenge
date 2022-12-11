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
storage = [rock, paper, scissors]
pick = int(input("What do you want to chose? Type 0 for Rock, 1 for paper, 2 for Scissors "))
A = storage[0]
B = storage[1]
C = storage[2]
computer = random.choice(storage)
print(computer)
if pick == 0:
    print(A)
    if A == computer:
        print("You won")
    else:
        print("You lost")
elif pick == 1:
    print(B)
    if B == computer:
        print("You won")
    else:
        print("You lost")
    
elif pick == 2:
    print(C)
    if C == computer:
        print("You won")
    else:
        print("You lost")
    
