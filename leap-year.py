# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

    
    ###############################################
    """Leap year calculations with functions"""
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(y, m):
  if m > 12 or m < 1:
      return "Invalid inputs"  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if is_leap(y) == False:
    new = month_days[m - 1]
    return new
  elif is_leap(y) == True:
    month_days[2] = 29
    new = month_days[m - 1]
    return new 



year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
