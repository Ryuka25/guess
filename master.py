from constraint import Problem, AllDifferentConstraint
from random import randint
from operations import addition, multiplication, division, zero

MAX_NUMBER = 100
MIN_NUMBER = 1


OPERATION_MAP = {"ADD": addition, "MUL": multiplication, "DIV": division, "ZER": zero}


class GuessTheNumberMaster:
    def __init__(self):
        ###############################
        # Setting up the hidden numbers
        ###############################
        peoples = [
            "K",
            "L",
            "P",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
        ]
        self.hidden_numbers = {}
        random_numbers = []
        for people in peoples:
            random_number = 0
            while True:
                random_number = randint(MIN_NUMBER, MAX_NUMBER)
                if random_number in random_numbers:
                    continue
                else:
                    random_numbers.append(random_number)
                    break
            self.hidden_numbers[people] = random_number

        # self.hidden_numbers = {
        #     "K": 43,
        #     "L": 38,
        #     "P": 81,
        #     "O": 5,
        #     "A": randint(MIN_NUMBER, MAX_NUMBER + 1),
        #     "B": randint(MIN_NUMBER, MAX_NUMBER + 1),
        #     "C": randint(MIN_NUMBER, MAX_NUMBER + 1),
        #     "D": randint(MIN_NUMBER, MAX_NUMBER + 1),
        #     "E": randint(MIN_NUMBER, MAX_NUMBER + 1),
        #     "F": randint(MIN_NUMBER, MAX_NUMBER + 1),
        #     "G": randint(MIN_NUMBER, MAX_NUMBER + 1),
        # }

        pass

    def start(self):
        print("hidden_numbers = ", self.hidden_numbers)
        print("")
        print("==============================================")
        print("============[POSEZ VOTRE QUESTION]============")
        print("==============================================")
        print("")
        print("Remarques:")
        print("- tapez 'exit' pour quitter")
        print("- les cases doivent être respecté")
        print("- des nouveaux nombres sont générer à chaque partie")
        print("")
        print("Chaque question posé sera sous la forme : ")
        print(">>>")
        print(">>> INITIAL_PERSONNE_1 INITIAL_PERSONNE_2 OPERATION")
        print(">>>")
        print("Operations : ADD MUL DIV ZER")
        print("")

        while True:
            raw_response = input(">>> ")

            try:
                questions = raw_response.upper().split()
                if questions[0] == "exit":
                    break

                personne_1 = questions[0]
                personne_2 = questions[1]
                operation = questions[2]

                operation_func = OPERATION_MAP[operation]

                result = operation_func(
                    self.hidden_numbers[personne_1], self.hidden_numbers[personne_2]
                )

                print(f"{personne_1} {personne_2} {operation} == {result}")

            except:
                print("erreur (vérifier vos inputs)")
                continue

        print("Programme terminé normalement")


if __name__ == "__main__":
    master = GuessTheNumberMaster()
    master.start()
