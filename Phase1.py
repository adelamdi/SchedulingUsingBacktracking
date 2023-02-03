
#Modeling CSP Problem
class Variable:
    def __init__(self, domain, conflicts) -> None:
        self.domain = domain
        self.conflicts = conflicts


class CSP:
    def __init__(self, variables, N) -> None:
        self.variables : list[Variable] = variables   # we're modeling salons as variables
        self.values = [i for i in range(1, N+1)] # and groups as values