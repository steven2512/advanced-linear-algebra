from linear_equations.equation import *
from linear_equations.solver.solve import solve
from matrix_operations.matrix import Matrix 

def forward_sub(system: list[Equation]) -> list[float]:
    result = [0] * len(system)
    current = solve(system[0], 'a').get_terms()[0].get_coefficient()
    result[0] = current
    for i in range(1, len(system)):
        front = system[i]
        for j in range(0, i):
            front = front.substitute('a'*(j+1), result[j])
        # pdb.set_trace()
        current = solve(front, 'a'*(i+1)).get_terms()[0].get_coefficient()
        result[i] = current
    return result


A = Matrix([2,0,0,-1,3,0,4,1,1], 3, 3)
b = Matrix([4,5,10], 3, 1)
system = build_equations(A, b)
print(*system)
print(forward_sub(system))