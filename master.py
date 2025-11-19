from random import randint
from configs import (
    MAX_NUMBER,
    MIN_NUMBER,
    PEOPLES,
    HIDDEN_NUMBERS,
    MANUAL_HIDDEN_NUMBERS,
    OPERATION_MAP,
)


class GuessTheNumberMaster:
    def __init__(self):
        if MANUAL_HIDDEN_NUMBERS:
            self.hidden_numbers = HIDDEN_NUMBERS
        else:
            self.hidden_numbers = {}
            random_numbers = []
            for people in PEOPLES:
                random_number = 0
                while True:
                    random_number = randint(MIN_NUMBER, MAX_NUMBER)
                    if random_number in random_numbers:
                        continue
                    else:
                        random_numbers.append(random_number)
                        break
                self.hidden_numbers[people] = random_number

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

            except Exception:
                print("erreur (vérifier vos inputs)")
                continue

        print("Programme terminé normalement")


if __name__ == "__main__":
    master = GuessTheNumberMaster()
    master.start()
