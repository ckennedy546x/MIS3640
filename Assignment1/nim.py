#
# You need to replace 'pass' with your code
#


from random import randint
from math import log


def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    # Define constant variables.
    HUMAN = 0
    COMPUTER = 1
    SMART = 0
    DUMB = 1

    # Create the initial pile, determine the starting player and the computer's
    # strategy.
    pile = randint(10, 100)
    turn = randint(0, 1)
    strategy = randint(0, 1)

    # While the game is still being played.
    while pile > 0:
        if turn == COMPUTER:
            
            if pile == 1:
                # Take the last marble.
                return False
            elif strategy == DUMB:
                # Take a random, legal number of marbles from the pile.
                take = randint(1, pile/2)
                return take
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
                take = randint(1, pile/2)
                return take
            else:
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus
                # 1.
                if pile > 63:
                    take = pile - 63
                    return take
                elif pile > 31:
                    take = pile - 31
                    return take
                elif pile > 15:
                    take = pile - 15
                    return take
                elif pile > 7:
                    take = pile - 7
                    return take
                else:
                    take = pile - 3
                    return take    
                
            # Update pile
            pile = pile - take

            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            
            turn = HUMAN

        elif turn == HUMAN:
            if pile == 1:
                return True
            else:
                print("Your turn.   The pile currently has", pile, "marbles in it.")

                take = int(input("How many marbles will you take? Make sure you take at least 1 marble but no more than half the current pile! "))
                if take > 0 and take <= pile/2:   
                # Update pile
                    pile = pile - take
        
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER

    return turn == COMPUTER

print(nim())