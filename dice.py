import random
import time
class Player:
  #Player class
  def __init__(self, name, money, points, tries, guesses):
     self.name = name		#Inputted name
     self.money = money		#Available coins
     self.points = points	#Number of correct guesses
     self.tries = tries		#Number of all guesses
     self.guesses = guesses	#List containing the guessed numbers and values of the dices
  def showStats(self):
     print "## You have", self.money,  "coins left and", self.points, "points. ##"
     if (self.tries != 0):
       successrate = (float(self.points)/float(self.tries))*100.0	#How many correct guesses from all guesses
       print "## Success rate is %.3f percent. ##" %successrate
     
def throw(guess_value, gamer):
  dice_value = random.randint(2,12) 				#Get a random integer between 2 and 12
  print "*** The dices show........ %d! ***" %dice_value
  if (guess_value == dice_value):				#Guess was correct
     print "*** And we have a winner! You received 5 coins ***"
     gamer.points = gamer.points +1
     gamer.money = gamer.money + 5
     gamer.tries = gamer.tries +1
  elif (guess_value < dice_value):		#Guessed value was too small
     print "*** Your guess is too small! ***"
     gamer.money = gamer.money -1
     gamer.tries = gamer.tries +1
  elif (guess_value > dice_value):		#Guessed value was too big
     print "*** Your guess is too big! ***" 
     gamer.money = gamer.money -1
     gamer.tries = gamer.tries +1     
  gamer.guesses.append(guess_value)		#Append dice and guess values for gameGenie
  gamer.guesses.append(dice_value)		#First value is player guess, second is the dice value
  time.sleep(2)					#Wait 2 seconds for more dramatic effect

def gameGenie(gamer):
  gamer.money = gamer.money - 1
  offvalues = 0				#How much off the guesses were
  i = 0
  if (len(gamer.guesses) > 0):
     #Calculate how much the guesses miss on average the dice values
     while(i < len(gamer.guesses) - 1):
       offvalues = offvalues + abs(gamer.guesses[i] - gamer.guesses[i+1])
       i = i + 1
  
     offavg = float(offvalues)/float(i)		#Average value for "missed" values
     print "*** Your guesses are on average off by %d ***" %(int(offavg)) 
     #Take the negative and positive values separately
     j = 0
     toosmall = 0	#All guesses that were too small 
     toobig   = 0	#All guesses that were too big 
     value    = 0	#Ansatz
  
     while(j < len(gamer.guesses)):
       value = gamer.guesses[j] - gamer.guesses[j+1]	#Sum guessed value and dice value
       if(value < 0):
         toosmall = toosmall + 1	#Increase number of too small guesses
       if(value > 0):
         toobig = toobig + 1		#Increase number of too large guesses
       j = j + 2       			#Iterate through player guesses
     if(toosmall > toobig):
       print "*** And your guesses are mostly too small! There are two dices you know... ***"	#Be a smart ass
     elif(toosmall < toobig):
       print "*** And your guesses are mostly too big! You sure you are only seeing two dices? ***"	#Be a smart ass
     elif(toosmall == toobig):
       print "*** And you keep changing your mind on the number you guess! Having a little split personality maybe? ***" #...

  else:
     print "*** The sum of two dices might be less than 12... ***"	#No guesses, but be a smart ass anyway
  
  time.sleep(2)		#Wait two seconds for more dramatic effect

def highScores(gamer):
#Show high scores and add players score if it is high enough
  print "You ran out of coins!!"
  time.sleep(2)
  print "You are cast out from the gambling tent. Hopefully you survive the night alone in the wilderness..."
  time.sleep(4)
  try:
     scoresfile = open("scores.txt", "r+")	#Attempt opening the high scores file
  except IOError:
     print "Couldn't open high scores file!"
  else:
     scores = scoresfile.read()
     scores = scores.split()		#Make a list from the scores file
     i = 1
     pos = 0		#Location in the list
     high = 0		#Highest score
     if(gamer.points <= int(scores[len(scores)-1])):	#Not enough points 
       print "You got %d points! Sorry, you didn't make it to the high scores list. \n" %gamer.points
       j = 0
       print "HIGHSCORES"
       while(j < len(scores)):
           print '{:10s} {:2d}'.format(scores[j], int(scores[j+1]))	#Print the high scores anyway
           j = j + 2							#Iterate through names in the list
     else:
       while(i < len(scores)):	
         if(gamer.points > int(scores[i])):
           if(int(scores[i]) > high):
             pos = i				#Location in the list for the new highest score
             high = int(scores[i])			#New highest score
         i = i + 2				#Iterate through names in the list
     #With the obtained location, the file is rewritten
       oldname = scores[pos-1]		#Store the high score that needs to be replaced
       oldpoints = scores[pos]
       newscores = []			#List containing the old scores and the new high score
       i = 0
       while(i < len(scores)):
         if(i != pos-1):
           newscores.append(scores[i])		#Append old scores
         else:
           newscores.append(gamer.name) 	#append new high score
           newscores.append(gamer.points)
           newscores.append(oldname)		#move the old score further
           newscores.append(oldpoints)
           i = i + 1
         i = i + 1

       print "You made it to the high scores list!! \n"
       i = 0
       print "HIGH SCORES"
       while(i < len(newscores)):	
           print '{:10s} {:2d}'.format(newscores[i], int(newscores[i+1])) #Print high scores in formatted manner
           i = i + 2
       scoresfile.seek(0, 0)		#set pointer to the beginning of the file
       for s in newscores:
           scoresfile.write("%s \n" %s) #Write to file, newline separating values 

     scoresfile.close()			#close the high scores file

def main():
  print "Game of Two Dices ver. 0.1"
  name = raw_input("What is your name? ")	#Name for the player instance
  name = name.replace(" ", "")			#Remove whitespace, for ver 0.1 high score handling 
  gamer = Player(name, 10, 5, 0,[])		#Create an instance for the player
  print "You find 10 coins from your pocket..."
  time.sleep(1)
  print "You approach a tent looking for shelter..."
  time.sleep(2)
  print "And in this tent, gambling is held. As long as you can play you are safe from the night.\n"
  time.sleep(3)
  inp = "0"
  #####Main loop
  while(1):
     print "An ominous character is rolling two dices in his hands...."
     print "Options:\n2-12  Guess the value of the two dices (costs one coin)"
     print "s  Shows your status\ng  GameGenie gambling advisor (costs one coin)" 
     print "q  Quits the game"
     inp = raw_input("Insert command:")		
     if(gamer.money <= 0):		#If all coins are used
       highScores(gamer)		#Show high scores and rewrite scores file upon need
       break				#Exit the main loop
     if (inp == 's'):		
       gamer.showStats()		#Show player coins, points and success rate
     elif (inp == 'g'):
       gameGenie(gamer)			#Give statistical advices to the player		
     elif (inp == 'q'):
       break 				#Quit pressed. Exit the main loop
     else:				#Anything else read from input
       try:
         int(inp)			#Try to typecast inp to integer
       except ValueError:
         print "*** Invalid command! ***"	#Not a number, nor any of the designated characters 
       else:
         if(int(inp) > 1 and int(inp) < 13):	#Inp is an integer in the correct range
           throw(int(inp), gamer)		#Go to dice throwing
         else:
           print "*** Guess again, the value is between 2 and 12 ***"	#Not a valid integer
     

main()
