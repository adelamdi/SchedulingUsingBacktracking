from Phase1 import *
from queue import PriorityQueue
from copy import copy

def Back_tracking(assignment:dict, csp:CSP) -> dict:
    """returns an assigment dictionary or None"""

    var_index = MRV(assignment, csp)
    var = csp.variables[var_index]
    
    for value in var.domain:
        csp0 = copy(csp)

        assignment[var_index] = value
        if is_complete(assignment, csp):
            return assignment

        if not forward_checking(var_index, value, csp0):
            return None
        
        result = Back_tracking(assignment, csp0)
        if result != None:
            return result
        del assignment[var_index]
    
    return None

def is_complete(assignment:dict, csp:CSP) -> bool:
    if len(assignment) == (len(csp.variables) - 1):
        return True
    return False

def forward_checking(var_index:int, value:int, csp:CSP):
    """"updates csp variables domain, and sees if any domain became empty then returns false, else returns true"""
    
    var = csp.variables[var_index]
    var.domain = [value]
    for c in var.conflicts:
        if value in csp.variables[c].domain:
            csp.variables[c].domain.remove(value)
        if len(csp.variables[c].domain) == 0:
            return False
    return True

def MRV(assignment:dict, csp:CSP) -> int:
    """returns index of a variable with minimum remaning values"""
    pq = PriorityQueue()
    
    for i in range(1, len(csp.variables)):
        if i not in assignment.keys():
          pq.put((len(csp.variables[i].domain), i))
    
    return pq.get(0)[1]

def LCV(var:Variable, csp:CSP) -> PriorityQueue:
    queue = {}

    for value in var.domain:
        # Choose that one who eliminate fewest values in other variables
        sum = 0
        for vari in var.conflicts:
            if value in csp.variables[vari].domain :
                sum += 1
        queue.update({value:sum})
    #Sort Queue Dictionary to find minimum
    sortedqueue = sorted(queue.items(), key=lambda x:x[1])
    return(list(sortedqueue)[0]) 
