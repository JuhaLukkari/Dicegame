import random
import time
class Player:
  def __init__(self, name, money, points, tries, guesses):
     self.name = name
     self.money = money
     self.points = points
     self.tries = tries
     self.guesses = guesses
  def showStats(self):
     print "## You have", self.money,  "coins left and", self.points, "points. ##"
     if (self.tries != 0):
       successrate = float(self.points)/float(self.tries)
       print "## Success rate is", successrate*100, "%. ##"
     
def throw(guess_value, gamer):
  dice_value = random.randint(2,12) 
  print "*** The dices show........ %d! ***" %dice_value
  if (guess_value == dice_value):
     print "*** And we have a winner! You received 5 coins ***"
     gamer.points = gamer.points +1
     gamer.money = gamer.money + 5
     gamer.tries = gamer.tries +1
  elif (guess_value < dice_value):
     print "*** Your guess is too small! ***"
     gamer.money = gamer.money -1
     gamer.tries = gamer.tries +1
  elif (guess_value > dice_value):
     print "*** Your guess is too big! ***" 
     gamer.money = gamer.money -1
     gamer.tries = gamer.tries +1     
  gamer.guesses.append(guess_value)
  gamer.guesses.append(dice_value)
  time.sleep(2)

def gameGenie(gamer):
  gamer.money = gamer.money - 1
  offvalues = 0
  i = 0
  while(i < len(gamer.guesses) - 1):
     offvalues = offvalues + abs(gamer.guesses[i] - gamer.guesses[i+1])
     i = i + 1
  offavg = float(offvalues)/float(i)
  print "Your guesses are on average off by %d" %(int(offavg)) 

def highScores(gamer):
#stuff here
#open and print contents of a file
#append gamer
  scores = open("scores.txt", "r")
   

def main():
  name = raw_input("What is your name? ")
  gamer = Player(name, 20, 0, 0,[])
  inp = "0"
  while(1):
     print "Options:\n2-12  Guess the value of the dice (costs one coin)"
     print "s  Shows your status\ng  GameGenie gambling advisor (costs one coin)" 
     print "q  Quits the game"
     inp = raw_input("Insert command:")
     if(gamer.money <= 0):
       print "*** You ran out of coins! You got", gamer.points, "right! ***"
       break
     if (inp == 's'):
       gamer.showStats()
     elif (inp == 'g'):
       gameGenie(gamer)
     elif (inp == 'q'):
       break 
     else:
       try:
         int(inp)
       except ValueError:
         print "*** Invalid command! ***"
       else:
         if(int(inp) > 1 and int(inp) < 13):
           throw(int(inp), gamer)
         else:
           print "*** Guess again, the value is between 2 and 12 ***"
     

main()
