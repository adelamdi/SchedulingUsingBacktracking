from Phase1 import *
from Phase2 import *



# left and right are variables 
def Arc_Reduction(left:Variable,right:Variable):
    Is_Changed = False
    for left_value in left.domain:
        Found = False
        for right_value in right.domain:
            if right_value != left_value: # If they're not equal then they're a possible solution
                Found = True
                break
        
        # There's no right value such that left value can be satisfied 
        # So it should be removed from the domain of the left variable 
        if not Found:
            left.domain.remove(left_value)
            Is_Changed = True
    
    return Is_Changed