from Phase1 import *
#from Phase2 import Back_tracking

def status(variables):
    for v in variables[1:]:
        print(v.domain)
        print(v.conflicts)
        print()

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
    
    status(variables)
    
    csp = CSP(variables, N)

    assigments : dict = Back_tracking({}, csp)

    for item in assigments.items():
        print(' '.join(item))

main()