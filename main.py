import random

sticks = 16
compwin = False
print("you start with 16 sticks")
print("you can remove 1, 2, or 3 sticks each round")
print("The person to pick the last stick loses")
print("----------------------------------------")


while sticks != 1:
  Ans = int(input("how many sticks do you wanna use (1, 2, or 3): "))
  while sticks == 3:
    while Ans > 2:
      print("You can't take all the sticks")
      Ans = int(input("how many sticks do you wanna use (1 or 2): "))
  while sticks == 2:
    while Ans > 1:
      print("You can't take all of the sticks")
      Ans = int(input("how many sticks do you wanna use (1):  "))
  while Ans > 3:
    print("thats more than 3, try again")
    Ans = int(input("how many sticks do you wanna use (1, 2, or 3):  "))
    if sticks == 3:
      while Ans > 2:
        print("You can't take all of the sticks")
        Ans = int(input("Pick a number (1 or 2)"))
    while sticks == 2:
      while Ans > 1:
        print("You can't take all the sticks")
        Ans == int(input("Pick a number (1)"))
  sticks = sticks - Ans
  print(f"sticks left: {sticks}")
  
  CompAns = random.randint(1,3)
  if sticks == 4:
    if CompAns == 1 or 2 or 3:
      CompAns = 3
      compwin = True
  if sticks == 3:
    if CompAns == 1 or 2 or 3:
      CompAns = 2
      compwin = True
  if sticks == 2:
    if CompAns == 2 or 3:
      CompAns = 1
      compwin = True
  if sticks > 1:
    sticks = sticks - CompAns
    print(f"computer answer: {CompAns}")
    print(f"sticks left: {sticks}")
  if compwin == True:
    print("The computer has won!")
    sticks = 16
    compwin = False
    print("you'll play again now")
  elif sticks == 1:
    print("The computer has lost")
    sticks = 16
    print("you'll play again now")
