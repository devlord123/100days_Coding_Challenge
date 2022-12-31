#Sorting a list

item = [60, 20, 70, 40, 50]

def sort_list(item,order):
    count = 0
    new = []
    if order == "asc":
        for i in item:
            if count > i:
                count = i
                print(count)
                new.append(count)
        print(new)
    if order == "dsc":
        for i in item:
            if count < i:
                count = i
                new.append(count)
        print(new)



sort_list(item, "dsc")
import pprint


#Hide a credit card
num = "578376527889764"
def card(num):
    if len(num) >= 15:
        print("Credit Card detected")
        ok = num[4:15]
        ok = "**********"
        print(f"{num[0:4]}{ok}")
    else:
        print("This is not a credit card")


card(num)

#Give Me Discount
def discount(price, percentage):
    per = price * percentage / 100
    disc_per = price - per
    print(f"Your discount price is {disc_per}. Enjoy!.")


discount(100, 20)

#Just The Number
word = ["Hello", "911", "im calling", "1234", "okay", "788"]

print(len(word))
def num(str):

    new = []
    for i in word:
        if i.isdigit():
            new.append(i)
    return new

print(num(word))

#Repeat Characters

def repeat(str):
    ran = []
    for i in str:
        for j in i:
            #print(i,j)
            ran.append(i)
            ran.append(j)
    print(f"{ran}")



repeat("wow")


#CHECKING IF ITS A NIGERIAN NUMBER
def checkNigerianNum(num):
    if len(num) != 13:
        return False
    for i in range(0, 4):
        if not num[i].isdecimal():
            return False
    if num[4] != "-":
        return False
    for i in range(5, 8):
        if not num[i].isdecimal():
            return False
    if num[8] != "-":
        return False
    for i in range(9, 13):
        if not num[i].isdigit():
            return False
    return True
# 555-444-7898
ngn = "0817-058-5143"
print(checkNigerianNum(ngn))
