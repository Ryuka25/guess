from constraint import Problem
from operations import addition, multiplication, division, zero


def add_constraint_for_addition(
    problem: Problem, numbers: dict[str, int], var_a: str, var_b: str
):
    r = addition(numbers[var_a], numbers[var_b])
    if r in range(3, 20 + 1):
        problem.addConstraint(lambda a, b: 20 <= a + b, [var_a, var_b])
    elif r in range(180, 199):
        problem.addConstraint(lambda a, b: 180 >= a + b, [var_a, var_b])
    else:
        problem.addConstraint(lambda a, b: r == a + b, [var_a, var_b])


def add_constraint_for_multiplication(
    problem: Problem, numbers: dict[str, int], var_a: str, var_b: str
):
    r = multiplication(numbers[var_a], numbers[var_b])
    problem.addConstraint(lambda a, b: r == multiplication(a, b), [var_a, var_b])


def add_constraint_for_zero(
    problem: Problem, numbers: dict[str, int], var_a: str, var_b: str
):
    r = zero(numbers[var_a], numbers[var_b])
    problem.addConstraint(lambda a, b: r == zero(a, b), [var_a, var_b])


def add_constraint_for_division(
    problem: Problem, numbers: dict[str, int], var_a: str, var_b: str
):
    r = division(numbers[var_a], numbers[var_b])
    problem.addConstraint(lambda a, b: r == division(a, b), [var_a, var_b])
