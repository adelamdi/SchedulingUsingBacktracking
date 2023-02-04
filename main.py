from Phase1 import *
from Phase2 import Back_tracking


def main():

    input = open("./inputs/input-1.txt", 'r')

    M,N = [int(i) for i in input.readline().split()] # M=number of salons, N=number of Groups

    variables = [None, *[Variable([], []) for _ in range(M)]]   # variables start from index 1

    for i in range(1, N+1):
        temp = [int(j) for j in input.readline().split()]
        for j in temp:
            variables[j].domain.append(i)

    E = int(input.readline())
    for i in range(E):
        conflicts = [int(j) for j in input.readline().split()]
        variables[conflicts[0]].conflicts.append(conflicts[1])
        variables[conflicts[1]].conflicts.append(conflicts[0])
    
    csp = CSP(variables, N)

    # status(csp.variables)

    assigments : dict = Back_tracking({}, csp)

    if assigments == None:
        print("No")
        return

    res = list(assigments.items())
    res.sort(key=lambda x: x[0])
    res = [str(i[1]) for i in res]
    
    print(' '.join(res))

main()