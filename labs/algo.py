from constraint import Problem, AllDifferentConstraint
from sujet import contrainte_addition, produit, division, contrainte_zero

xi = [43, 38, 81, 5, 46, 39, 68]  # liste aleatoire

responses = {
    "M": {"a": 81, "p": 4, "d": 1, "z": 1},
    "A": {"a": 124, "p": 3, "d": 1, "z": 4},
    "L": {"a": 48, "p": 5, "d": 8, "z": 4},
    "V": {"a": 89, "p": 8, "d": 1, "z": 0},
    "S": {"a": 82, "p": 7, "d": 1, "z": 1},
    "F": {"a": 111, "p": 4, "d": 1, "z": 2},
}

# supprimer les redondances de reponses pour supprimer les questions inutiles qui n'apportent rien
# on utilise addition pour obtenir intervalle globale (reduire les intervalles de possibilites)
# pour savoir chiffre des unites on utilise produit
# on utilise zero pour avoir un intervalle de 10
# division : utilse qd il y a pas mal d'ecart entre les possibilites (pour voir quel possibilite est la plus proche de la solution)
# responses = {
#     "M": {"a": None, "p": None, "d": None, "z": None},
#     "A": {"a": None, "p": 3, "d": None, "z": None},
#     "L": {"a": 48, "p": None, "d": 8, "z": None},
#     "V": {"a": None, "p": None, "d": None, "z": 0},
#     "S": {"a": None, "p": None, "d": None, "z": None},
#     "F": {"a": None, "p": None, "d": None, "z": None},
# }


personnes = ["K"]
for key, value in responses.items():
    # vérifier si AU MOINS une des valeurs n'est pas None
    if any(v is not None for v in value.values()):
        personnes.append((key))

p = Problem()

p.addVariables(personnes, range(1, 101))
p.addConstraint(AllDifferentConstraint(), personnes)


for key, value in responses.items():
    if value["a"] != None:
        p.addConstraint(
            lambda a, b, r=value["a"]: contrainte_addition(a, b, r), ["K", key]
        )
    if value["p"] != None:
        p.addConstraint(lambda a, b, r=value["p"]: produit(a, b) == r, ["K", key])
        pass
    if value["d"] != None:
        p.addConstraint(lambda a, b, r=value["d"]: division(a, b) == r, ["K", key])
        pass
    if value["z"] != None:
        # p.addConstraint(lambda a, b, r=value["z"]: contrainte_zero(a, b, r), ["K", key])
        pass

s = p.getSolutions()
print()
print("Il y a", len(s), "solutions\n")
# print(s)

variable_a_afficher = "K"
valeurs = sorted({solution[variable_a_afficher] for solution in s})
print(f"il y a {len(valeurs)} valeurs possibles de {variable_a_afficher} : {valeurs}")
