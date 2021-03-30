import random


def coinToss():
    """Function to flip the coin and decide which user/AI goes first"""
    if random.randint(0, 1) == 0:
        #print ('AI') test
        return 'PC'
    else:
        return 'Player'
        #print ('Player') test

#Test
#for x in range(0, 10):
#    coinToss()
