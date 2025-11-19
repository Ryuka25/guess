from constraint import Problem
from problem_constraints import (
    add_constraint_for_addition,
    add_constraint_for_division,
    add_constraint_for_multiplication,
    add_constraint_for_zero,
)


OPERATION_CONSTRAINT = {
    "ADD": add_constraint_for_addition,
    "MUL": add_constraint_for_multiplication,
    "DIV": add_constraint_for_division,
    "ZER": add_constraint_for_zero,
}

MAX_NUMBER = 100
MIN_NUMBER = 1


class Histories:
    def __init__(self):
        self.content = []
        self.step = 1

    def add(self, var1, var2, operation, result):
        self.content.append(
            {"var1": var1, "var2": var2, "operation": operation, "result": result}
        )

        self.step += 1

    def has_already_used(self, var1, var2, operation):
        for history in self.content:
            operation_match = operation == history["operation"]
            vars_match = (var1 == history["var1"] and var2 == history["var2"]) or (
                var2 == history["var1"] and var1 == history["var2"]
            )

            if operation_match and vars_match:
                return True
        return False

    def compact(self):
        return list(
            map(
                lambda h: f"{h['var1']} {h['var2']} {h['operation']} {h['result']}",
                self.content,
            )
        )

    def number_of_apparition(self, var):
        apparition = 0
        for history in self.content:
            if var == history["var1"] or var == history["var2"]:
                apparition += 1

        return apparition


def get_solutions_for_one_variable(
    problem: Problem, var: str, histories: Histories, min=MIN_NUMBER, max=MAX_NUMBER
):
    if histories.number_of_apparition(var) == 0:
        return range(min, max + 1)
    solution_dicts = problem.getSolutions()
    target_solutions = list({solution_dict[var] for solution_dict in solution_dicts})
    return target_solutions


def get_other_variables(peoples, apart: str = ""):
    return list(filter(lambda people: people != apart, peoples))


def apply_constraint(
    problem: Problem, var1: str, var2: str, operation: str, result: int
):
    constraint = OPERATION_CONSTRAINT[operation]
    constraint(problem, result, var1, var2)
