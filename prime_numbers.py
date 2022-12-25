print ("The Prime Numbers in the range are: ")  
for num in range(1, 55):
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
          break
    else:
      print(num)
