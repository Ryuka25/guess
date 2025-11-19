from constraint import Problem
from src.utils import get_solutions_for_one_variable, Histories


def test_get_solutions_for_one_variable():
    problem = Problem()
    problem.addVariables(["K", "L"], [1, 2, 3])
    solutions_for_k = get_solutions_for_one_variable(problem, "K", Histories(), 1, 3)
    assert set([1, 2, 3]) - set(solutions_for_k) == set({})
    assert 4 not in solutions_for_k
