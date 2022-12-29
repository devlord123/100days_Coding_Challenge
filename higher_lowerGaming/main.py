from game_data import data
import art
import random
from replit import clear



score = 0
print(art.logo)

game = True
question_b = random.choice(data)

while game:
  question_a = question_b 
  question_b = random.choice(data)
  
  while question_a == question_b:
    question_b = random.choice(data)
  
  a_name = question_a["name"]
  a_desc = question_a["description"]
  a_country = question_a["country"]
  a_count = question_a["follower_count"]
  
  b_name = question_b["name"]
  b_desc = question_b["description"]
  b_country = question_b["country"]
  b_count = question_b["follower_count"]
  
  print(f"Compare A: {a_name}, a {a_desc}, from {a_country}")
  print(art.vs)
  print(f"Against B: {b_name}, a {b_desc}, from {b_country}")
  
  guess = input("Make a guess 'A' or 'B'? ")
  
  if guess == "A" and a_count > b_count:
    score += 1
    clear()
    print(f"You won and your score is {score}")
  elif guess == "B" and b_count > a_count:
    score += 1
    clear()
    print(f"You won and your score is {score}")
  else:
    game = False
    clear()
    print(art.logo)
    print(f"You score {score}, Try again")


