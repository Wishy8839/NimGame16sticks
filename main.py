import random
import time

sticks = 16
compwin = False
Wins = 0
Losts = 0
print("you start with 16 sticks")
print("you can remove 1, 2, or 3 sticks each round")
print("The person to pick the last stick loses")
print("----------------------------------------")


while sticks != 1 or -1 or -2 or -3 or 0 :
  Ans = int(input("how many sticks do you wanna use (1, 2, or 3): "))
  if sticks == 3:
      while Ans > 2:
        print("You can't take all of the sticks")
        Ans = int(input("Pick a number (1 or 2)"))
        if Ans == 2:
          compwin = True
      while sticks == 32:
       while Ans > 1:
        print("You can't take all the sticks")
        Ans == int(input("Pick a number (1)"))
        if Ans == 1:
          compwin = True
  while Ans <= -1:
    print("You can't take away a negative!")
    Ans = int(input("How many sticks do you wanna use (1, 2, or 3:  )"))
  while Ans == 0:
    print("you can't skip your turn!")
    Ans = int(input("how many sticks do you wanna use (1, 2, or 3:  )"))
  while Ans > 3:
    print("thats more than 3, try again")
    Ans = int(input("how many sticks do you wanna use (1, 2, or 3):  "))
  if Ans <=-1:
    Ans*-1
  sticks = sticks - Ans
  print(f"sticks left: {sticks}")
  
  CompAns = random.randint(1,3)
  if sticks == 12:
    if CompAns == 1 or 2:
      CompAns = 3
  if sticks == 10:
    if CompAns ==  2 or 3:
      CompAns = 1
  if sticks == 8:
    if CompAns == 1 or 2:
      CompAns == 3
  if sticks == 7:
    if CompAns == 1 or 3:
      CompAns = 2
  if sticks == 6:
    if CompAns == 2 or 3:
      CompAns = 1
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
  if Ans <= -1:
    print("Stop trying to cheat")
    sticks = random.randint(2,4)
    compwin = True
  if CompAns >= 16:
    CompAns = 15
    time.sleep(1)
    print("So you tried to cheat, YOU WILL LOSE!")
  if sticks > 1:
    sticks = sticks - CompAns
    print(f"computer answer: {CompAns}")
    print(f"sticks left: {sticks}")
  if compwin == True:
    print("The computer has won!")
    sticks = 16
    compwin = False
    Losts += 1
    print(f"Number of times lost: {Losts}")
    print(f"Number of times won: {Wins}")
    time.sleep(1.5)
    print("you'll play again now")
    time.sleep(1.5)
    print(f"Number of sticks: {sticks}")
  elif sticks == 1:
    print("The computer has lost")
    sticks = 16
    Wins += 1
    print(f"Number of times lost: {Losts}")
    print(f"Number of times won: {Wins}")
    time.sleep(1.5)
    print("you'll play again now")
    time.sleep(0.5)
    print(f"Number of sticks: {sticks}")
