from replit import clear
from art import logo
print(logo)

bid = {}
bid_more = True

def high_bid(h_bid):
  h = 0
  winner = ""
  for i in h_bid:
    score = h_bid[i]
    if score > h:
      h = score
      winner = i
  print(f"The winner is {winner} with ${h} total bids.")
      


while bid_more:
  name = input("What is your name: ")
  price = int(input("How many bid? $"))
  bid[name] = price
  print("Do you want to bid again")
  bg = input("yes or no ")
  if bg == "no":
    bid_more = False
    high_bid(h_bid = bid)
    print("Congrats.")
  else:
    clear()