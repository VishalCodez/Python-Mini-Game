#Game title: Land of the Lost

#----All functions go here-----
def gameIntro():    #Displays the introductory message for the game
    print('Welcome to Land of the Lost')
    print('This game was creator for pure amusement')
    print('If you like it or not, the created had a blast making the game\n')
    print('You are Warrick, a soldier who has strayed from his platoon and when trying to make')
    print('Way back to his platoon, Warrick stepped on what appeared to be a trap set up by a ravanous fellow')
    print('It appears it was set up by a vicious evil-dark sorcerer, Xzyphix who had a foul feeling for humans')
    print('Warrick is falling down to what appears to be several hundreds of feet down in pitch black')
    print('Worrying for his life, Warrick feels he will fall straight to his death to some evil trap set up below.')
    print('After Warrick sees a faint light at the bottom of the pit, Warrick reluctantly lands on a soft pile of what')
    print('he thought as pillows, but really it was the decaying bodies of past travelers befallen to the same trap.')
    print('Warrick picks up a small bag of tokens. The pouch reads "Door Tokens", wonder whats the use?')
    print('Welcome to Hell, a faint voice said. Warricks eyes grew big and he knew at this moment sword in hand')
    print('Buckler in the other and along with a crossbow with limited to 5 shots of righteous Silver arrows')
    print('Warrick would not be another statistic to this miniscule unholy dungeon.')
    print('So Warrick sets off... Into the darkness of Land of the Lost.\n')

def warrickUI():    #References Global variables that were pre-defined for use in the Warrick UI function
    global warrickHP    
    global warrickDEF 
    global warrickXbow 
    global warrickPots 
    global warrickEnergy 
    global warrickTokens
    
    print('-----------------------------------')
    print('\nWarrick')
    print('    HP:    ' + str(warrickHP) +' / 100'+'    Defense: '+str(warrickDEF)+'%') #Controls Warricks HP & Defense
    print('    Crossbow: ' +str(warrickXbow) + ' of 5 Arrows Left. Use Wisely!')    #Controls Warricks Arrows counter
    print('    Potions: ' +str(warrickPots) + ' of 3 Potions Left. Maximum 3!')     #Controls Warricks potions
    print('    Fatigue: ' +str(warrickEnergy) + ' %. Dont Run out or you DIE!')     #Controls Warricks Fatigue stat
    print('    Door Tokens: ' +str(warrickTokens) + ' of 50. Dont spend all in one Door!')  #Controls Warricks tokens
    print('\n-----------------------------------\n')

def doorRules():    #Presents the game rules when called
    print('Warrick starts of with 4 doors in front of him. Each door has a number 1 - 4.')
    print('Warrick must decide which door to travel through. Keep in mind these rules')
    print('\nRULES')
    print('    1.Every Main Door has a series of doors inside which requires a token cost to pass through. The token ranges are 1-10 tokens')
    print('    2.In the event you spend your tokens unwisely and simply you run out, Warricks fate will already be sealed')
    print('    3.Expect that the higher the door cost the riskier but more rewarding it is, even so maybe thats a Lie!')
    print('Let the Games Begin.\n')
    print('Which door will you choose you peasant!, says the Goblin atop a pedastall.')

def doorMapping():  #When called, this prompts the user for a Main door choice which will be compared with a nested If/Else condition
    import sys
    doorchoice = input('Please type a door number 1-4:')
    if str(doorchoice) == str(1):
        print('\nYou chose MAIN Door #: '+ str(doorchoice) + '\n')
    elif str(doorchoice) == str(2):
        print('\nYou chose MAIN Door #: '+ str(doorchoice)+ '\n')
    elif str(doorchoice) == str(3):
        print('\nYou chose MAIN Door #: '+ str(doorchoice)+ '\n')       
    elif str(doorchoice) == str(4):
        print('\nYou chose MAIN Door #: '+ str(doorchoice)+ '\n')        
    else:
        print('\nYou choose no Door, enemies quickly surround you and you DIE!')
        print('Warrick lets out a blood curdling yell.')
        print('You hear the gobling cackling in the background, why didnt you choose?...HeeeHeeHeHeHYaaah\n')
        sys.exit()  #System terminates the program

def mainDoor(howManyDoors, doorCounter):
    #Passes value by referance in order to keep track of How many total doors lye in the dungeon and current door progress
    print('This dungeon has ' + str(howManyDoors) +' Total Doors. Choose your Doors carefully') 
    print('Warrick passes through door '+str(doorCounter)+' of Total '+str(howManyDoors)+ '. Total Doors Remaining: '+str(howManyDoors))
    doorCounter += 1
    howManyDoors -=  1

def warrickLowHP(): #Function to automatically heal Warrick if he runs low on HP
    global warrickHP
    global warrickPots
    
    if int(warrickHP) <= 40: #When Warricks HP goes below 40 this function will heal warrick and subtract 1 from his total potions
        print('\nWarrick was low on HP, automatic potion if available used')
        print(' +   30 HP \n')
        warrickPots -=  1
        warrickHP +=  30
        return warrickPots, warrickHP
        if int(warrickPots) == 0:
            print('\nWarrick can no longer Heal, Please get more potions\n')
    
def doorRandomizer():
    import random   #imports the random library to use in the randomized door generation
    import sys
    D1=random.randrange(1,3)        #These ranges are tied into a absolute encounters list that will dish out
    D1cost=random.randrange(5,15)   #the event tied to that door range number when choosen by the player
    D2=random.randrange(4,7)
    D2cost=random.randrange(5,15)
    D3=random.randrange(8,10)
    D3cost=random.randrange(5,15)
    print('Door choices are as followed. Please enter the door number.' )
    print('\nDoor ' + str(D1)+' ['+str(D1cost)+' token cost]'+'    Door ' + str(D2)+' ['+str(D2cost)+' token cost]'+'    Door ' + str(D3)+' ['+str(D3cost)+' token cost]')
    userChoice = input('\nEnter Door Here : ')

    global warrickTokens    #Global variable to keep track of Warricks Tokens
    
    if warrickTokens < D1cost or warrickTokens < D2cost or warrickTokens < D3cost:
        print('\nA mysterious figure appears from out the shadows, says "Warrick You Do No Have Enough Tokens To Proceed"')
        print('May this dungeon and the vile creatures have mercy on your soul')
        print('Warrick becomes trapped and is consumed by the darkness. Game Over...\n')
        sys.exit()
    elif str(userChoice) == str(D1) :
        warrickTokens -=  D1cost
        absoluteDoorOccurences(userChoice)
        print('\nGreat Job, Warrick continues.')
        print('Warrick has ' + str((warrickTokens)) + ' Tokens remaining\n')
        return warrickTokens
    elif str(userChoice) == str(D2):
        warrickTokens -= D2cost
        absoluteDoorOccurences(userChoice)
        print('\nGreat Job, Warrick continues.')
        print('Warrick has ' + str((warrickTokens)) + ' Tokens remaining\n')
        return warrickTokens
    elif str(userChoice) == str(D3):   
        warrickTokens -=  D3cost
        absoluteDoorOccurences(userChoice)
        print('\nGreat Job, Warrick continues.')
        print('Warrick has ' + str((warrickTokens)) + ' Tokens remaining\n')
        return warrickTokens
    else:
        while str(userChoice) != str(D1) or str(userChoice) != str(D2) or str(userChoice) != str(D3):
            print('\nHEEY! Enter the correct Door number.')
            print('Try Again')
            print('\nDoor ' + str(D1)+' ['+str(D1cost)+' token cost]'+'    Door ' + str(D2)+' ['+str(D2cost)+' token cost]'+'    Door ' + str(D3)+' ['+str(D3cost)+' token cost]')
            userChoice=userChoice = input('\nEnter Door Here : ')
            
            if str(userChoice) == str(D1) :
                warrickTokens -=  D1cost
                absoluteDoorOccurences(userChoice)
                print('\nGreat Job, Warrick continues.')
                print('Warrick has ' + str((warrickTokens)) + ' Tokens remaining\n')
                return warrickTokens
            elif str(userChoice) == str(D2):
                warrickTokens -=  D2cost
                absoluteDoorOccurences(userChoice)
                print('\nGreat Job, Warrick continues.')
                print('Warrick has ' + str((warrickTokens)) + ' Tokens remaining\n')
                return warrickTokens
            elif str(userChoice) == str(D3):   
                warrickTokens -= D3cost
                absoluteDoorOccurences(userChoice)
                print('\nGreat Job, Warrick continues.')
                print('Warrick has ' + str((warrickTokens)) + ' Tokens remaining\n')
                return warrickTokens              
    
def absoluteDoorOccurences(doorChoice):
    global warrickHP 
    global warrickDEF 
    global warrickXbow 
    global warrickPots 
    global warrickEnergy 
    global warrickTokens
    import time     #Used to add time pauses to execute an action or project a game feeling
   #These conditions are used to set what is behind each door when the door is chosen
    if str(doorChoice) == str(1):
        print('\nDesolate, nothing inside beside a long hallway, \n')
        time.sleep(.8)
        print('Warrick sees something moving on the ground...It is nothing, Warrick continues...')
        time.sleep(.8)
        warrickEnergy -=  17.5
        return warrickEnergy
    elif str(doorChoice) == str(2):
        print('Warrick finds 1 coin and as Warrick looks up he pauses,..')
        time.sleep(1)
        print('to see a decaying skeloton in the corner looks grim, Warrick continues...\n')
        warrickTokens += 1
        warrickEnergy -= 4.35
        return warrickEnergy, warrickTokens
    elif str(doorChoice) == str(3):
        print('Warrick finds 1 Silver Arrow and 1 Potion, Warrick grins')
        time.sleep(.8)
        print('As Warrick is walking, trips and falls over...Ooof')
        time.sleep(.8)
        print('Gets up, Warrick continues...\n')
        warrickXbow += 1
        warrickPots +=  1
        warrickEnergy -= 4.5
        return warrickEnergy, warrickPots, warrickXbow
    elif str(doorChoice) == str(4):
        print('Goblin encounter. Warrick defeats the enemy looses 4 HP')
        print('Warrick exclaims! ')
        time.sleep(1.3)
        print('I took a HIT!, Warrick continues...\n')
        warrickHP -=   4
        warrickEnergy -=  6.5
        warrickDEF -=  8.0
        return warrickEnergy, warrickHP, warrickDEF
    elif str(doorChoice) == str(5):
        print('Reluctantly nothing suspicious inside.')
        print('Warrick decides to take a quick break since its clear')  
        time.sleep(.8)
        print('Warrick gets up, Warrick continues...\n')
        warrickEnergy -= 4.5
        return warrickEnergy
    elif str(doorChoice) == str(6):
        print('Warrick finds a chest. Its a TRAP!')
        print('Warrick takes the first strike!')
        time.sleep(1.2)
        print('.... SWooOOSh! Beheaded')
        time.sleep(.8)
        print('Warrick suffers 15 hp, Looses 1 Arrow, Warrick continues...\n')
        warrickHP -=   15
        warrickEnergy -= 7.5
        warrickDEF -=  5.0
        warrickXbow -= 1
        return warrickEnergy, warrickHP, warrickDEF, warrickXbow 
    elif str(doorChoice) == str(7):
        print('Warrick finds 2 Silver Arrows, Warrick continues through a puzzle of stairs, Will he ever get out?...\n')
        time.sleep(.8)
        print('I think its this way, mmmm')
        time.sleep(.8)
        print('Get a map Pal!')
        time.sleep(.8)
        print('Warrick succesfully navigates through the web of stairs')
        warrickXbow += 2
        warrickEnergy -= 3.5
        return warrickEnergy, warrickXbow
    elif str(doorChoice) == str(8):
        print('Warrick encounters a Centaur, the Centaur pauses as if he recognizes Warrick')
        time.sleep(.8)
        print('Nope, he quiclkly rushes Warrick, blows exchange, Centaur falls Warrick suffers 35 HP loss, Looses 2 arrows,')
        time.sleep(.5)
        print('finds 5 coins, Warrick continues...\n')
        warrickHP -= 35
        warrickTokens += 5
        warrickEnergy -= 10.5
        warrickDEF -= 13.0
        warrickXbow -= 2
        return warrickEnergy, warrickTokens, warrickHP, warrickDEF, warrickXbow
    elif str(doorChoice) == str(9):
        print('Warrick finds 7 Door Tokens. "Hey turn around..."')
        time.sleep(1.5)
        print('"HAAAH! Made you LOOK!", Warrick continues...\n')
        warrickTokens += 7
        warrickEnergy -= 3.5
        return warrickEnergy, warrickTokens
    elif str(doorChoice) == str(10):
        print('Warrick is ambushed. Its a TRAP!.')
        time.sleep(1.8) + ('After some intense battling, que the music....Ring a ding ding....')
        print('Warrick suffers 50 hp, looses 1 arrow, Warrick continues...\n')
        warrickHP -= 50
        warrickEnergy -= 14.5
        warrickDEF -= 17.0
        warrickXbow -= 1
        return warrickEnergy, warrickHP, warrickDEF, warrickXbow
#----Functions List ends here---------
#---Global Values
warrickHP = 100
warrickDEF = 100
warrickXbow = 5
warrickPots = 1
warrickEnergy = 100
warrickTokens = 50
import random
import sys
totalDoors = doorsGen = random.randrange(5,10)
doorEnterCounter = 0
#----Global values end-------------------
#Game Execution Below
gameIntro() #game introduction
warrickUI() #controls Warrick Interface
doorRules() #introduces player to game rules
doorMapping() #Door sequence and Rules
mainDoor(doorsGen, doorEnterCounter) #initializes 1st game sequence

while warrickTokens > 0:    #Loops the game as long as player stays above 0 tokens or clears the game and does not die
    doorRandomizer()
    warrickLowHP()
    warrickUI()
    doorsGen -= 1
    doorEnterCounter +=  1
    print('Warrick passes through door '+str(doorEnterCounter)+' of Total '+str(totalDoors)+ '. Total Doors Remaining: '+str(doorsGen))
    if int(warrickTokens) < 0 or int(warrickHP) <= 0: 
        print('\nWAAAAAAARICK, you insolent FOOL!!, How could you run out of Tokens or Let Yourself DIE! says Warricks Inner Mind')
        print('The enemies draw near and Warrick stands no chance')
        print('Thanks for playing!! Now exiting..')
        sys.exit()
    #------------------------------
    if str(doorEnterCounter) == str(totalDoors) and int(warrickHP) > 0 and int(warrickTokens) > 0:
        print('You Made It Out, Congratulatioooooonsssss!!!')
        sys.exit()
