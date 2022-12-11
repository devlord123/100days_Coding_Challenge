# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
resF = name1.lower()
resM = name2.lower()

T = resF.count('t') + resM.count('t')
R = resF.count('r') + resM.count('r')
U = resF.count('u') + resM.count('u')
E = resF.count('e') + resM.count('e')
first = T + R + U + E

L = resF.count('l') + resM.count('l')
O = resF.count('o') + resM.count('o')
V = resF.count('v') + resM.count('v')
E = resF.count('e') + resM.count('e')
second = L + O + V + E
result = str(first) + str(second)
if result < "10":
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result > "90":
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result < "40" or result <= "50":
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
