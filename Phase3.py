from Phase1 import *
from Phase2 import *
from copy import copy



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

def AC3(csp:CSP): # returns false on failure and true on success
    # create a worklist and fill it with all of the arcs
    Worklist = []
    for left in csp.variables[1:]:
        for right in left.conflicts:
            Worklist.append((left,csp.variables[right]))

    while len(Worklist) != 0:
        arc = Worklist[0]
        Worklist.remove(Worklist[0])
        left = arc[0]
        right = arc[1]
        if Arc_Reduction(left,right):
            if len(left.domain) == 0:
                return False #
            else:
                for Candidate_Arc in left.conflicts:
                    Worklist.append((csp.variables[Candidate_Arc],left))
                    