class Term:
    "Represnts a mathematical term (inclusive or exclusive of variables)"
    def __init__(self, coefficient: int, variables: list):
        self.coefficient = coefficient
        self.variables = variables
    
