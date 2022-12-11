# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y" or extra_cheese == "Y":
        bill += 4
        print(f"Your final bill is: {bill}")
    elif add_pepperoni == "N" or extra_cheese == "N":
        print(f"Your final bill is: {bill}")
    print(f"Your final bill is: {bill}")
    



elif size == "M":
    print("Medium")
elif size == "L":
    print("Large")
