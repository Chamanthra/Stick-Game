#defining the print_move function.
 def print_move(current_player, row, stick_quantity):
    if stick_quantity == 1:                     #if the stick_quantity=1 the sticks
 should be stick.           
        print(current_player, 'takes', stick_quantity, 'stick from row', row)
    else:
        print(current_player, 'takes', stick_quantity, 'sticks from row', row)
 #importing module random to radomly choose the current_player and rows and 
stick_quantity for 'CPU' turn.
 import random
 import time   # additional task .  
print('Welcome to Nim!')                            #print intoductory for the 
start of the game. 
user = input('Enter name: ')                      #prompt the user to enter their 
name.              
wins = 0         
losses = 0       
#Using a endless while loop to play the game again and again if the user wants.
 running_game =True
 while running_game:
    decision =input('Do you want the player that picked the last stick to be 
winner(w) or loser(l) ?enter w or l : ').lower() # additional task.
    sticks = [1, 3, 5, 7]
    player = [user, 'CPU']
    current_player = random.choice(player)               #choosing a random player 
to go first.
    print(f"Game is starting {current_player} will be going first!")
    #run the game until sum of sticks become zero.
    while sum(sticks) > 0:
        #To display the sticks as triangle in the screen before and after taking 
out sticks taking turns.
        for row, stick in enumerate(sticks, start=1):
            width = len(sticks) - row
            space = ''
            print(str(row) + '.' + space.center(width) + '|' * stick)
        if current_player == user:
            #Reprompt the user until the user enter valid syck and row number.
            while True:
                try:
                    row = int(input('Which row would you like to take sticks from? 
'))
 take? '))
                    stick_quantity = int(input('How many sticks would you like to 
                    if  row in range(1,len(sticks)+1) and  stick_quantity in 
range(1,sticks[row - 1]+1):
                        break
                    else:
                        print('Invalid row or stick number.')
                except ValueError:
                    print('Invalid input.')
            print_move(current_player, row, stick_quantity)
            #The selected amount of sticks taken out by user is subtracted from the
 sticks list.
            sticks[row - 1] -= stick_quantity
            current_player = 'CPU'          #set the current_player to CPU.
        #if the current_player is cpu the row and amount of sticks to be taken out 
will be picked randomly.
        #The game will reprompt the cpu to enter valid entries and deductions from 
already empty rows.
        else:
            while True :
                try:
                    row = random.randint(1, len(sticks))
                    stick_quantity = random.randint(1, sticks[row - 1])
                    if row in range(1,len(sticks )+1) and stick_quantity in 
range(1,sticks[row-1]+1) :
                        break
                except ValueError:
                    print('invalid input')
            sticks[row - 1] -= stick_quantity  #The amount of sticks cpu want to 
deduct from the stick list is subtracted.
            time.sleep(2)                       # rest for two seconds before 
executing print_move function.
            print_move(current_player, row, stick_quantity)
            current_player = user          #set current_player to user.
    #if sum of sticks is zero end the game.
    print('Game Over!')
    #The last player to take out the last stick can be winner or loser according to
 the decision variable value.
    #additional task .
    if decision == 'w':                  # The last current player to take out the 
last stick  is the winner.
        if current_player =='CPU':          
            print(f"Winner is {user} ")
            wins += 1
        else:
            print(f"Winner is CPU")
            losses += 1
    else :                           # The last current player to take out the last
 stick  is the loser.
        if current_player == 'CPU':
            print(f"Winner is CPU")
            losses +=1
        else:
            print(f"Winner is {user}")
            wins +=1
    #Asking the user if they want to playe the game again or not.
    response = input('Would you like to play again? Enter y or n: ').lower()
    print (f"You have won {wins} time(s) and lost {losses} time(s).")       #keep 
track of all the wins and losses of the user.
    #if the response is no then the game will end .
    if response != 'y':
        running_game =False     
