import random

# Read and understand the docstrings of all of the functions in detail.


def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
    deck= []
    for i in range(1,num+1):
        deck.append(100+i)
        deck.append(200+i)
        deck.append(300+i)
        deck.append(400+i)
    return deck
    

def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    random.shuffle(deck)
    return deck

def deal_cards_start(deck):
     '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
     '''
     i = 1
     player= []
     while i < 8:
         player.append(deck[-i])
         i = i+1
     i=1
     while i<8:
         deck.pop(-1)
         i=i+1
         
     return player
               
     


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    
    i = 1
    while i < num+1:
        player.append(deck[-i])
        
        i = i+1
    x = 1

    while x < num+1:
         deck.pop(-1)
        
         x = x+1


def takeRank(elem):
    return elem%100


def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    emp=[]
    for i in hand:
            emp.append(i)
    emp2=[]
    for i in hand:
            emp2.append(i)
            
    emp.sort()
    
    emp2.sort(key=takeRank)
    for i in range(len(emp)-1):
        if emp2[i]%100 == emp2[i+1]%100 and emp2[i]//100 > emp2[i+1]//100:
            x=emp2[i]
            emp2.pop(i)
            emp2.insert(i+1,x)
    
    
    print (emp)
    print(emp2)
    

            



def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    
    for i in cards:
        if i in player:
            player=player
        else:
            excluded= i
    for i in cards:
        if i in player:
           player=player 
        else:
            print(str(excluded)+ " is not in hand, Invalid input")
            return False
    return True       
        


def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    if len(cards)< 2:
        print("Invalid input. Discardable set needs to have at least 2 cards.")
        return False
    else:
        for i in range(0,len(cards)-1):
            if(str(cards[i])[1:])== (str(cards[i+1])[1:]):
                checker = True
            else:
                checker = False
                return False
        if checker == True:
            return True
    


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([311,312,313,316])
    Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    x= cards[0]//100
    emp=[]
    if len(cards)< 3:
        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
        return False
    else:
        for i in cards:
                emp.append(i)
                
        for i in cards:
            
            if i//100 == x:
                checker = True
            else:
                checker = False
                return False
        if checker == True:
            emp.sort()
            for i in range(0,len(emp)-1):
                
                if emp[i]%100 == emp[i+1]%100 -1:
                    checker == True
                else:
                    checker == False
                    return False
        return True

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in your hand. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    
    x = 0
    while x == 0:
        emp=[]
        cards= str(input("Which card would you like to discard? "))
        cards = cards.strip().split()
        for i in cards:
            emp.append(int(i))
        cards= emp
        if is_valid(cards,player) == True:
            for i in cards:
                player.remove(i)
            x = 1
        else:
            print("No such card in your hand. Try again.")
    print("here is your new hand printed in two ways\n")
    print_deck_twice(player)


def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401

    401 102 104
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211

    103 211
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
    
    z = 0
    
    while z== 0:
        question = input("Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind?")
        if question.strip().lower() == "yes":
            z= 0
            emp=[]
            cards = str(input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space:"))
            cards = cards.strip().split()
            
            for i in cards:
                emp.append(int(i))
            cards = emp
            x= cards[0]//100
            checker = True
            if is_valid(cards,player) == True:
                if is_discardable_kind(cards) == True :
                    for i in cards:
                        player.remove(i)
                    print("here is your new hand printed in two ways\n")
                    print_deck_twice(player)
                    
                   
                elif is_discardable_seq(cards) == True :
                    for i in cards:
                        player.remove(i)
                    print("here is your new hand printed in two ways\n")
                    print_deck_twice(player)
                else:
                    for i in cards:
                        if i//100 == x:
                            cards = cards
                        else:
                            checker = False
                    if checker != False:
                        print("Invalid sequence. While Cards are all of the same suit, they are not consecutive integers")
                    else:
                        print("Invalid sequence. Cards are not of same suit")
            else:
                
                z = 0
                
                       
           
            
                
        
        
        elif question.strip().lower() == "no":
            z= 1
            player = player
           
         


# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()

    
# YOUR CODE GOES HERE and in all of the above functions instead of keyword pass

if size_change.strip().lower() == "yes":
    rank_change = int(input("Enter a number between 3 and 99, for the number of ranks:"))
elif size_change.strip().lower() == "no":
    rank_change = 13

x = rank_change * 4
print("You are playing with a deck of " + str(x) + " cards")

make_deck(rank_change)
shuffle_deck(make_deck(rank_change))                
deck = shuffle_deck(make_deck(rank_change)) # deck is made and shuffled


player = (deal_cards_start(deck))


print("Here is your starting hand printed in two ways\n")
print_deck_twice(player) #players hand is delt and printed in useful ways
round = 1
while len(player) > 1:
    
    print ("Welcome to round " + str(round))
    dice = random.randint(1,6)     
    print("You rolled " + str(dice))
    if dice == 1:
        rolled_one_round(player)
        print("Round " + str(round) +" completed")
        round= round +1
    else:
        if len(deck) < dice:
            num =len(deck)
        else:
            num = dice
        
        print(f'since you rolled {dice},the following {dice} or {len(deck)}will be added to will be added to your hand from the deck')
        deal_new_cards(deck, player, num)
        print("Here is your new hand printed in two ways\n")
        print_deck_twice(player)
        
        rolled_nonone_round(player)
        
        
        while(is_discardable_seq== False and is_discardable_kind == False):
            rolled_nonone_round(player)

        print("Round" + str(round) +"completed")
        round= round +1
     
while len(player) == 1:
     print ("Welcome to round" + str(round))
     print ("The game is in empty deck phase")
     rolled_one_round(player)
     
     
if len(player) == 0:
    print("CONGRATULATIONS YOU COMPLETED THE GAME IN " + str(round) +" rounds" + ",HURRAY!")
     
    
    
    
  
