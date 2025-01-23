from linear_equations.equation import Equation
from linear_equations.solver.solve import solve
import pdb
def back_sub(system: list[Equation]) -> list[float]:
    result = [0] * len(system)
    current = solve(system[-1], f'a{len(system)}').get_terms()[0].get_coefficient()
    result[-1] = current
    for i in range(len(system)-2, -1, -1):
        back = system[i]
        for j in range(len(result)-1, i, -1):
            back = back.substitute(f'a{j+1}', result[j])
        current = solve(back, f'a{i+1}').get_terms()[0].get_coefficient()
        result[i] = current
    # pdb.set_trace()
    return result