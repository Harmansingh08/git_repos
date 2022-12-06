import random
chances = 3
gameover = 1
totalscore = 0
print("----------------- GUESS THE NUMBER GAME -------------------")
print("########################## Rules ##########################")
print("-> You will decide the upper and lower bound for the game.")
print("-> You will get only 3 chances to guess the correct answer.")
print("-> You will be awarded 10 Points for each correct answer.")
print("\n")
print("__________________LET'S START THE GAME__________________")
print("\n")
while(gameover):
  lowerBound = int(input("Enter Lower Bound : "))
  upperBound = int(input("Enter Upper Bound : "))
  print("------------------------")
  print("      GAME STARTED      ")
  print("------------------------")
  randomVal = random.randint(lowerBound,upperBound)
  while chances>0 :
    guess = int(input("Take a guess : "))
    print("------------------------")
    if(guess>randomVal):
      print("Your guess was high.")
      chances-=1
      print(chances, "chances left.")
      print("------------------------")
    elif(guess<randomVal):
      print("Your guess was low.")
      chances-=1
      print(chances, "chances left.")
      print("------------------------")
    elif(guess==randomVal):
      print("Correct Guess, Congrats ")
      chances=3
      totalscore+=10
      print("------------------------")
      break
  print("Total Score is", totalscore)
  if(chances==0):
      gaveover=0
      print("Correct Number was", randomVal)
      print("------------------------")
      print("       GAME OVER       ")
      if(totalscore==0):
        print("Better Luck Next Time!")
      print("------------------------")
      break