from abc import ABC, abstractmethod

class Constraint(ABC):
    def __init__(self, variables):
        self.variables = variables

        @abstractmethod
        def satisfied(self, assignment):
            pass

class CSP():
    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError(
                    'Every variable should have domain assigned to it.')

    def add_constraints(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)
    def consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment)==len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None

class MapColoringConstraint(Constraint):
    def __init__(self, place1, place2):
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2

    def satisfied(self, assignment):
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]

if __name__ == "__main__":
    variables = [
        'Yukon', 'British Columbia', 'Northwest Territories', 'Alberta', 'Saskatchewan', 'Manitoba', 'Nunavut', 'Ontario', 'Quebec'
    ]
    domains = {}

    for variable in variables:
        domains[variable] = ['red', 'green', 'blue', 'yellow', 'orange', 'Pink', 'Brown', 'Purple', 'Cyan']

    csp = CSP(variables, domains)
    csp.add_constraints(MapColoringConstraint('Yukon', "British Columbia"))
    csp.add_constraints(MapColoringConstraint('Yukon', "Northwest Territories"))
    csp.add_constraints(MapColoringConstraint('British Columbia', "Northwest Territories"))
    csp.add_constraints(MapColoringConstraint('Manitoba', "Ontario"))
    csp.add_constraints(MapColoringConstraint('Ontario', "Quebec"))


    solution = csp.backtracking_search()

    if solution is None:
        print("No Solution has been found")
    else:
        print(solution)