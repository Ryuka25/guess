import pytest
from constraint import Problem
from operations import addition, multiplication, division, zero
from problem_constraints import (
    add_constraint_for_addition,
    add_constraint_for_division,
    add_constraint_for_multiplication,
    add_constraint_for_zero,
)
from utils import get_solutions_for_one_variable, Histories


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, True),
        (100, True),
        (0, False),
        (101, False),
    ],
)
def test_no_constraint(number, expected):
    me = "K"
    hidden_numbers = {me: 20, "L": 25}
    problem = Problem()
    problem.addVariables(hidden_numbers.keys(), range(1, 100 + 1))
    solutions_for_me = get_solutions_for_one_variable(problem, me, Histories())
    assert (number in solutions_for_me) == expected


@pytest.mark.parametrize(
    "my_number, other_number, number, expected",
    [
        # The result should limit the range
        #
        # result <= 20 (inférieur à 20 donc peut etre un nombre au hasard)
        #
        # result = 2
        (1, 1, 1, True),
        (1, 1, 2, True),
        #  result = 3
        (1, 2, 1, True),
        (1, 2, 19, True),
        (
            1,
            2,
            20,
            # pas possible d'obtenir 20 si on a un 20 parmis les deux nombres
            # équivaut à dire que l'autre nombre va être 0
            False,
        ),
        (1, 2, 21, False),
        # result = 19
        (1, 18, 19, True),
        (1, 18, 19, True),
        # result = 20
        (10, 10, 19, True),
        (
            1,
            19,
            20,
            # pas possible d'obtenir 20 si on a un 20 parmis les deux nombres
            # équivaut à dire que l'autre nombre va être 0
            False,
        ),
        (1, 19, 21, False),
        (10, 10, 20, False),
        (10, 10, 21, False),
        #
        # result >= 20
        #
        # result = 21
        (1, 20, 1, True),
        (1, 20, 20, True),
        (1, 20, 21, False),
        (1, 20, 22, False),
        (2, 19, 1, True),
        (2, 19, 20, True),
        (2, 19, 21, False),
        (2, 19, 22, False),
        #
        # result <= 180
        #
        # result = 178
        (78, 100, 80, True),
        (78, 100, 79, True),
        (78, 100, 78, True),
        (78, 100, 77, False),
        (78, 100, 76, False),
        # result = 179
        (79, 100, 81, True),
        (79, 100, 80, True),
        (79, 100, 79, True),
        (79, 100, 78, False),
        (79, 100, 77, False),
        #
        # result >= 180 (supérieur à 180 donc peut etre un nombre au hasard)
        #
        # result == 180
        (80, 100, 82, True),
        (80, 100, 81, True),
        (80, 100, 80, True),
        (
            80,
            100,
            79,
            # Même si nombre au hasard, C'est n'est pas possible d'obtenir 180 à partir de 79
            # Equivaut à dire que l'autre nombre va être 101
            False,
        ),
        (80, 100, 78, False),
        # result == 181 (supérieur à 180 donc peut etre un nombre au hasard)
        (81, 100, 83, True),
        (81, 100, 82, True),
        (81, 100, 81, True),
        (81, 100, 80, True),
        (
            81,
            100,
            79,  # Même si nombre au hasard, C'est n'est pas possible d'obtenir 180 à partir de 79
            False,
        ),
        (81, 100, 78, False),
    ],
)
def test_addition_constraint(my_number, other_number, number, expected):
    me = "K"
    hidden_numbers = {me: my_number, "L": other_number}
    problem = Problem()
    problem.addVariables(hidden_numbers.keys(), range(1, 100 + 1))
    result = addition(hidden_numbers[me], hidden_numbers["L"])
    add_constraint_for_addition(problem, result, me, "L")
    histories = Histories()
    histories.add(me, "L", "ADD", result)
    solutions_for_me = get_solutions_for_one_variable(problem, me, histories)
    assert (number in solutions_for_me) == expected
