# number of arguments for sides of dice 
# table of probability for each possible outcome for each number

import random
from collections import Counter

def prob_dice(dices, sim_count ):
    table=dict()
    simulation_count=sim_count
    roll_log =Counter()
    
    for i in range(simulation_count):
        roll_log[sum((random.randint(1,dice) for dice in dices))]+=1

        
        
    for record in range(len(dices),sum(dices)+1):
        rolling_prob=round((float(roll_log[record])/simulation_count)*100,2)
        table[record]=f"{rolling_prob}%"
        print(f"{record} {rolling_prob}%")
    return table    
        
        
    
    
    

prob_dice([4,6,6,5,7],10**5)

