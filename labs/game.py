import random
import traceback
from constraint import Problem
from operations import addition, multiplication, division, zero
from problem_constraints import (
    add_constraint_for_addition,
    add_constraint_for_division,
    add_constraint_for_multiplication,
    add_constraint_for_zero,
)
from utils import get_solutions_for_one_variable

MAX_NUMBER = 100
MIN_NUMBER = 1

OPERATION_CONSTRAINT = {
    "ADD": add_constraint_for_addition,
    "MUL": add_constraint_for_multiplication,
    "DIV": add_constraint_for_division,
    "ZER": add_constraint_for_zero,
}

DEBUG = False

# tester si l'operation est compatible avec l'autre
# mul permet de reduire les nombres en arrière elimine une grande partie, add est efficace seulement si on débute, il permet de limiter les ranges entre deux chiffres

# tester les operations que je peut faire, la meuilleurs à effectuer selon les possibilités
# rechercher si l'opération a été déjà effectuer avec la personne à qui j'voullais le faire,
# si oui, chercher qqn d'autres

# Faire addition si capabalities entre 1 - 100
# Faire multiplication si les chifres des unités sont très différentes

# Best operation between two variables

# ADD if one of variable already known to test the addition


class GuessTheNumber:
    def __init__(self):
        # Setting up game data
        self.histories = []
        self.step = 1
        self.me = "K"

        # Create a problem
        self.problem = Problem()

        # Setting up the hidden numbers
        self.hidden_numbers = {
            self.me: None,
            "L": None,
            "P": None,
            "O": None,
        }
        self.problem.addVariables(
            self.hidden_numbers.keys(), range(MIN_NUMBER, MAX_NUMBER + 1)
        )

    def get_other_peoples(self):
        list_of_peoples = list(self.hidden_numbers.keys())
        return list(filter(lambda people: people != self.me, list_of_peoples))

    def store_step(self, personne1, personne2, operation, result):
        self.histories.append((personne1, personne2, operation, result))

    def show_candidates(self, personne):
        print(get_solutions_for_one_variable(self.problem, personne))

    def show_histories(self):
        print(self.histories)

    def show_next_move(self, personne, operation):
        print("Personne: ", personne, "— Opération: ", operation)

    def start(self):
        print("hidden_numbers = ", self.hidden_numbers)
        print("")
        print("==============================================")
        print("=============[ECRIVER LA REPONSE]=============")
        print("==============================================")
        print("")
        print("Remarques:")
        print("- tapez 'exit' pour quitter")
        print("- tapez 'next' pour afficher la suggestion")
        print(
            "- tapez 'candidates PERSONNE_INITIAL' pour vérifier les candidats restant pour une personne"
        )
        print("- tapez 'history' pour afficher les historiques")
        print("- les cases doivent être respecté")
        print("- les nombres trouvés disparaissent à chaque partie")
        print("")
        print("Chaque réponse attendu sera sous la forme : ")
        print(">>>")
        print(">>> exit")
        print(">>> next")
        print(">>> history")
        print(">>> candidates PERSONNE_INITIAL")
        print(">>> INITIAL_PERSONNE_1 INITIAL_PERSONNE_2 OPERATION")
        print(">>>")
        print("")

        while True:
            personne, operation = self.which_personne_operation()
            raw_response = input(f"Pas de jeux : {self.step} >>> ")

            try:
                response = raw_response.split()
                if response[0] == "exit":
                    break

                if response[0] == "candidates":
                    self.show_candidates(response[1])
                    continue

                if response[0] == "history":
                    self.show_histories()
                    continue

                if response[0] == "next":
                    self.show_next_move(personne, operation)
                    continue

                personne1 = response[0]
                personne2 = response[1]
                operation = response[2]
                result = int(response[3])
                self.store_step(personne1, personne2, operation, result)
                self.apply_constraint(personne1, personne2, operation, result)

            except Exception as e:
                print("erreur (vérifier vos inputs)", e)
                if DEBUG:
                    traceback.print_exc()
                continue

            self.step += 1

        print("Programme terminé normalement")

    def apply_constraint(self, personne1, personne2, operation, result):
        constraint = OPERATION_CONSTRAINT[operation]
        constraint(self.problem, result, personne1, personne2)

    def get_prev_history(self, stepBack=1):
        """Return tuple of other_person, operation, result"""
        try:
            prev_history = self.histories[-stepBack]
        except:
            prev_history = None

        if not prev_history:
            return None, None, None

        other_person = (
            prev_history[0] if prev_history[0] != self.me else prev_history[1]
        )
        return other_person, prev_history[2], prev_history[3]

    def get_random_personne(self):
        choices_left = []

        personnes_in_history = []

        for history in self.histories:
            personnes_in_history.append(history[0])
            personnes_in_history.append(history[1])

        for people in self.get_other_peoples():
            if people not in personnes_in_history:
                choices_left.append(people)

        if choices_left:
            return random.choice(choices_left)

        # Anyway get a random people if no choices left
        return random.choice(self.get_other_peoples())

    def get_random_personne_from_history_without_type_of_operation(
        self, operations, other_than
    ):
        personnes_histories = []
        blacklisted_personnes = []

        for history in self.histories:
            other_personne = history[0] if history[0] != self.me else history[1]
            if history[2] in operations:
                blacklisted_personnes.append(other_personne)
            personnes_histories.append(other_personne)

        for personne in blacklisted_personnes:
            personnes_histories.remove(personne)

        personnes_histories.remove(other_than)

        try:
            personne = random.choice(personnes_histories)
        except:
            # Just pick a one personne
            personne = random.choice(self.get_other_peoples())

        return personne

    def which_personne_operation(self):
        # Implementation here

        if self.step == 1:
            # Addition operation give a precise range so do it first
            # Also it won't change so this is no longer necessary after first step
            personne = self.get_random_personne()
            return (personne, "ADD")

        prev_personne, prev_operation, prev_result = self.get_prev_history()

        if self.step == 2:
            return (prev_personne, "MUL")

        prev_prev_personne, prev_prev_operation, prev_prev_result = (
            self.get_prev_history(2)
        )

        if prev_prev_personne == prev_personne:
            # On essaie d'éviter d'utiliser la même personne
            # plus de deux fois de suite
            personne = self.get_random_personne()

            if prev_operation != "DIV":
                return personne, "MUL"

            personne = self.get_random_personne_from_history_without_type_of_operation(
                ["DIV"], prev_personne
            )

        personne = prev_personne
        return personne, "DIV"


if __name__ == "__main__":
    game = GuessTheNumber()
    game.start()
