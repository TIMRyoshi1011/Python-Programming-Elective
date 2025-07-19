import random

x = random.randint (1, 10)
y = 0
z = 0
print ('Enter a random number between 1 and 10')

while z != x:
  y += 1
  z = input (f'Random number # {y}: ')

  if z.isnumeric(): 
    z = int (z)

  else: 
    print ('That is not a number, only enter numbers!')
    continue

  if z > x:
    print ("That number is too high, try again!") 

  elif z < x: 
    print("That number is too low, try again!")

else:
  print (f'It took you {y} tries to get the correct answer, congratulations!')
  input ("Press enter to exit")
  