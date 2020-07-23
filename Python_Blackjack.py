#1 Deck
#P2 = Dealer
#Choice hit,stand,doubledown,insurance || split

import random

#Finds the total of the cards in the player's hand
def sum(playerhand,pl):

    handsum=0

    #Finds all of the aces in a players hand and moves them to the back of the list
    for aceplace in playerhand:

        if (aceplace=='Ace'):
            
            playerhand.pop(playerhand.index(aceplace))
            playerhand.append('Ace')
            playerhand.count('Ace')
            
    #Goes through every card in the player's hand and finds the sum of all them
    for place in playerhand:

        
        #Chooses whether ace score should be 1 or 11
        if(place=='Ace'):

              if((handsum+11)<22):
                  x=11
              else:
                  x=1
                  
        elif (place=='Jack'):

            x=10

        elif (place=='Queen'):

            x=10

        elif (place=='King'):

            x=10

        else:

            x=place

        #Adds the value of the card to the total value of the hand so far
        handsum=handsum+x

    return handsum

#Assigns the playerhand two random cards from a pack of cards (See 'deck=[]')
def hand(playerhand):

    x=0

    while x!=2:

        nextcard=random.randint(0,(len(deck)-1))
        playerhand.append(deck[nextcard])
        deck.pop(nextcard)

        x=x+1

#Adds a new card into the player's hand of cards
def hit(playerhand,pl):

    nextcard=random.randint(0,(len(deck)-1))
    playerhand.append(deck[nextcard])
    deck.pop(nextcard)

    print ('Player',pl,': New Card!',playerhand[-1])

#Bank will only save you 3 times from bankrupcy
lives=3
#Player starts with £1000 to spend
moneyinbank=1000

print('You have £',moneyinbank,'to bet')

print('Would you like to play blackjack?(y/n)')
playagain=input('P.S.anything other than an input of \'y\' will constitute an \'n\' ')
print()

while(playagain=='y'):

    if(moneyinbank==0):
        #Gives £1000 if player is bankrupt
        print('You take a £1000 loan from the bank')
        moneyinbank=1000

    #Will ask player to bet an amount of money (Has to be affordable)
    while(1!=2):
        bet=int(input('How much money do you bet on this game? £'))

        if(bet<=moneyinbank):
            if(bet>=0):
                break
        #If the bet is not affordable, keep asking until it is
        print('Offer a proper bet')
    


    #Finite number of cards & values in ONE deck
    deck=['Ace', 'Ace', 'Ace', 'Ace', 2, 2, 2, 2, 3, 3, 3, 3,4, 4,
          4, 4,5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,9, 9,
          9, 9,10, 10, 10, 10,'Jack', 'Jack', 'Jack', 'Jack', 'Queen',
          'Queen', 'Queen', 'Queen', 'King', 'King', 'King', 'King']



    
    p1hand=[]
    p2hand=[]

    #Gives the player & dealer their cards
    hand(p1hand)
    hand(p2hand)

    


    
    #Makes it ( | ) easier to read code  
    #         ( v )
    p2card1=p2hand[0]
    p2card2=p2hand[1]


    #Finds the sum of the player & dealer's cards respectively
    p1sum=sum(p1hand,1)
    p2sum=sum(p2hand,2)


    

    
    turn=0
    first=0
    split=0
    splfirst=0
    
    #This loop will go on forever until a 'break' clause appears
    while (1!=2):

        print()
        
        if(p1sum==21):
            if(split==0):break
            else:turn=2
            
            
        #So that the player can use insurance in case of the dealer having Blackjack  
        if(p2card1!='Ace'):
            if(p2sum==21):
                if(split==0):break
                else:turn=2
        
        #Player's turn
        if(turn==0):

            print ()
            print ()

            print ('Your Cards:',p1hand)

            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print ('Dealer\'s first Card:',p2card1)
            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print()
            
            print()

            print ('Your Total:',p1sum)
    
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            
            print('Possible choices: 1.hit 2.stand 3.double 4.split 5.insurance')
            print()
            if (p1sum>=21):
                if(split==0):
                    break
                else:
                    turn=2
                
                
            #What action does the player want to take?
            choice=input('Player 1 ')
            print()


            if (choice=='hit'):

                hit(p1hand,1)
                
                p1sum=sum(p1hand,1)

                #print ('P1 Total:',p1sum)
                #print ('Your Cards:',p1hand)

            if (choice=='stand'):
                
                if(p2sum>p1sum):
                    if(split==0):break
                    else:turn=2

                else:
                    if(split==0):
                        turn=1
                        print('Dealer\'s turn')
                    else:
                        turn=2
                        

                    #print ('Your Cards:',p1hand)
                    
                    print()

            if (choice=='double'):
                #'first' makes sure the player doesn't try to double after their 1st action
                if(first==0):

                    print('Double your bet')
  
                    if((bet*2)<=moneyinbank):

                        bet=bet*2

                        hit(p1hand,1)

                        p1sum=sum(p1hand,1)

                        print ('P1 Total:',p1sum)
                        print ('Your Cards:',p1hand)

                    else:

                        print('You don\'t have enough money to double your bet')

                    


                else:

                    print('You can only double the first time')

            if (p1sum>=21):
                if(split==0):
                    break
                else:
                    turn=2

            #'first' makes sure the player doesn't try to insurance after their 1st action
            if(first==0):
                if(p2card1=='Ace'):
                    
                    if(choice=='insurance'):
                        #Winning the insurance bet & losing the original bet always cancel eachother out
                        if(p2card2=='Jack'):

                            print('Win the insurance bet & lose original bet | Net loss: £0')
                            bet=0
                            if(split==0):break
                            else:turn=2

                        elif(p2card2=='Queen'):

                            print('Win the insurance bet & lose original bet | Net loss: £0')
                            bet=0
                            if(split==0):break
                            else:turn=2

                        elif(p2card2=='King'):
                            
                            print('Win the insurance bet & lose original bet | Net loss: £0')
                            bet=0
                            if(split==0):break
                            else:turn=2

                        elif(p2card2==10):
                            
                            print('Win the insurance bet & lose original bet | Net loss: £0')
                            bet=0
                            if(split==0):break
                            else:turn=2
                        
                        else:
                            #If insurance bet is lost(Insurance bet always = half of original bet 
                            moneyinbank-=(bet/2)
                            print('You have £',moneyinbank,'to bet')
                elif(p2card1!='Ace'):
                    if(choice=='insurance'):
                        print('You cannot use that option at this time')

            else:
                if(choice=='insurance'):
                    print('You cannot use that option at this time')
            
            if(first==0):
                if(p1hand[0]==p1hand[1]):
                    splithand=[]
                    if(choice=='split'):
                        splithand.append(p1hand[0])
                        print('Split! Splithand: ',splithand)
                        p1hand.remove(p1hand[0])
                        hit(p1hand,1)
                        print()
                        print('Play hand: ',p1hand)
                        p1sum=sum(p1hand,1)
                        print ('P1 Total:',p1sum)
                        split=1
                if(p1hand[0]!=p1hand[1]):
                    if(choice=='split'):
                        print('You cannot use that option at this time')
            else:
                if(choice=='split'):
                    print('You cannot use that option at this time')
            first+=1
            
        #Dealer's turn
        if(turn==1):

            toobig=0
            wouldwork=0

            #Finds the card value which is the highest possible value card to be drawn without going bust
            hitorpush=21-p2sum
        
            for card in deck:

                if (card=='Ace'):card=1

                if(card=='King'):card=10

                if(card=='Queen'):card=10

                if(card=='Jack'):card=10

                #If the selected card in the deck is:

                #Too big & would therefore cause the dealer to bust add 1 to this tally
                if (card>hitorpush):

                    toobig+=1

                #small enough not to cause a bust if selected add 1 to this tally
                if(card<=hitorpush):

                    wouldwork+=1
            
            #Bust or Dealer's won
            if (p2sum>=21):
                break
            #Stand : Dealer's won
            if(p2sum>p1sum):
                break

            #If both players have the same card value:
            if(p2sum==p1sum):

                #If more cards in the deck will bust the dealer than make the dealer win, stand & settle for a draw
                if(toobig>wouldwork):

                    break

                #If more cards in deck will make the dealer win that make the dealer bust, hit
                else:

                    hit(p2hand,2)

                    p2sum=sum(p2hand,2)

            #If the dealer's score is less than the player's the dealer's only hope of winning is the hit
            if(p2sum<p1sum):

                hit(p2hand,2)

                p2sum=sum(p2hand,2)


#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§





        #If player has split
        if(turn==2):
            
            if(splfirst==0):
                print()
                print('Playhand is done')
                
                hit(splithand,1)
                splfirst=1
            
            print(splithand)
            splitsum=sum(splithand,'Split')
            print()
        
            if(splitsum==21):
                break
            
            
            
        
        #Split Player's turn
        

            if (splitsum>=21):
                break
                
            print()
            print('Possible choices: 1.hit 2.stand 3.double 4.split 5.insurance')
            print()    
                
            #What action does the player want to take?
            choice=input('Split hand: ')
            print()


            if (choice=='hit'):

                hit(splithand,'Split')
                
                splitsum=sum(splithand,'Split')

                print ('Split Total:',splitsum)
                print ('Split Cards:',splithand)

            if (choice=='stand'):
                if(p2sum>splitsum):
                    break
                else:
                    turn=1

                    print ('Split Cards:',splithand)
                    print('Dealer\'s turn')
                    print()

            if (choice=='double'):
                #'first' makes sure the player doesn't try to double after their 1st action
                if(first==0):

                    print('Double your bet')
  
                    if((bet*2)<=moneyinbank):

                        bet=bet*2

                        hit(p1hand,1)

                        splitsum=sum(splithand,'Split')

                        print ('Split Total:',splitsum)
                        print ('Split Cards:',splithand)

                    else:

                        print('You don\'t have enough money to double your bet')

                    


                else:

                    print('You can only double the first time')



#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§



                    
            
    #Out of playing loop
    print()
    p1sum=sum(p1hand,1)
    print ('Your Cards:',p1hand)
    print ('Your Total:',p1sum)

    print()
    if(split!=0):
        splitsum=sum(splithand,1)
        print('Split cards:',splithand)
        print('Split total:',splitsum)

    print()

    p2sum=sum(p2hand,2)

    print ('Dealer\'s Cards:',p2hand)
    print ('Dealer\'s Total:',p2sum)        

    print()

    #Calculates who has the highest score <=21
    if(p1sum>p2sum):

        if(p1sum<=21):

            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print ('Player 1 beats Dealer')
            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

            moneyinbank+=bet

        else:

            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print ('Dealer beats Player 1')
            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

            moneyinbank-=bet

    elif(p2sum>p1sum):

        if(p2sum<=21):

            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print ('Dealer beats Player 1')
            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

            moneyinbank-=bet

        else:

            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print ('Player 1 beats Dealer')
            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

            moneyinbank+=bet

    elif(p2sum==p1sum):

        print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
        print('Player & Dealer: Push')
        print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

    print()
    print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
    print()

    if(split!=0):
        if(splitsum>p2sum):

            if(splitsum<=21):

                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
                print ('Player split beats Dealer')
                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

                moneyinbank+=bet

            else:

                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
                print ('Dealer beats Split')
                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

                moneyinbank-=bet

        elif(p2sum>splitsum):

            if(p2sum<=21):

                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
                print ('Dealer beats Split')
                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

                moneyinbank-=bet

            else:

                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
                print ('Player split beats Dealer')
                print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

                moneyinbank+=bet

        elif(p2sum==splitsum):

            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')
            print('Player split & Dealer: Push')
            print('±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

    #Game over
    print()
    print()
    print('Play Over')
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print('You have £',moneyinbank,'to bet')
    print()

    if(moneyinbank==0):

        print('You are broke! The bank will only save you',(lives-1),'more times')
        lives-=1

    #If broke more than 3 times play ends immediately
    if(lives==0):

        print('The bank refuses to lend you an more money | You lose')
        break


    #Asks player whether they want to bet again
    playagain=input('Would you like to play blackjack?(y/n)')
    print()           
    print() 


#Leaving message
if(lives>0):

    print('You leave the Casino with £',moneyinbank)

    if(moneyinbank>=1000):

        print('You have gained £',(moneyinbank-1000))

    else:

        print('You have lost £',(1000-moneyinbank))
