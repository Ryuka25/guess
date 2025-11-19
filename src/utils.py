import copy
from constraint import Problem
from configs import MIN_NUMBER, MAX_NUMBER, OPERATION_CONSTRAINT


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


def check_constraint_validity(
    new_problem, peoples, var1, var2, operation, result, histories
):
    apply_constraint(new_problem, var1, var2, operation, result)

    for people in get_other_variables(peoples):
        candidates = get_solutions_for_one_variable(new_problem, people, histories)
        if len(candidates) == 0:
            yes_no = input(
                f"No candidates found for {people} if using this cmd, continue with this ? y/N"
            )
            if yes_no == "y":
                continue
            else:
                raise Exception(f"No candidates found for {people} if using this cmd")
        if len(candidates) == 1:
            print(f"One candidate left for {people} == {candidates}")


def add_command(problem: Problem, cmd: str, histories, peoples):
    # cmd sous la forme "VAR1 VAR2 OPERATION RESULT"
    parsed_cmd = cmd.upper().split()

    var1 = parsed_cmd[0]
    var2 = parsed_cmd[1]
    operation = parsed_cmd[2]
    result = int(parsed_cmd[3])

    new_variables = []
    current_variables = list(problem._variables.keys())
    if var1 not in current_variables:
        new_variables.append(var1)
    if var2 not in current_variables:
        new_variables.append(var2)

    new_problem = copy.deepcopy(problem)
    new_problem.addVariables(new_variables, range(MIN_NUMBER, MAX_NUMBER + 1))
    check_constraint_validity(
        new_problem, peoples, var1, var2, operation, result, histories
    )

    problem.addVariables(new_variables, range(MIN_NUMBER, MAX_NUMBER + 1))
    apply_constraint(problem, var1, var2, operation, result)

    return var1, var2, operation, result


def get_operation_already_used_in_list_of_ordered_operation(
    list_of_ordered_operation, people
):
    already_used_operations = []
    for ordered_operation in list_of_ordered_operation:
        for operation in ordered_operation:
            if operation["var"] == people:
                already_used_operations.append(operation["operation"])
    return already_used_operations
