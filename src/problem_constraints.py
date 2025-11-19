# Realistic constraints

from constraint import Problem
from operations import multiplication, division, zero


def add_constraint_for_addition(
    problem: Problem,
    r: int,
    var_a: str,
    var_b: str,
):
    if r <= 20:
        problem.addConstraint(lambda a, b: a + b <= 20, [var_a, var_b])
        return
    if r >= 180:
        problem.addConstraint(lambda a, b: a + b >= 180, [var_a, var_b])
        return
    problem.addConstraint(lambda a, b: a + b == r, [var_a, var_b])


def add_constraint_for_multiplication(problem: Problem, r: int, var_a: str, var_b: str):
    problem.addConstraint(lambda a, b: r == multiplication(a, b), [var_a, var_b])


def add_constraint_for_zero(problem: Problem, r: int, var_a: str, var_b: str):
    problem.addConstraint(lambda a, b: r == zero(a, b), [var_a, var_b])


def add_constraint_for_division(problem: Problem, r: int, var_a: str, var_b: str):
    problem.addConstraint(lambda a, b: r == division(a, b), [var_a, var_b])
