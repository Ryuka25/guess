# definit la prochaine meilleure question à poser
# supprimer les redondances de reponses pour supprimer les questions inutiles qui n'apportent rien

def evaluer(intervalle, variable_interessant="K"):
    #si on veut savoir le chiffre des unites, si les chiffres des unites sont differents dans l'intervalle
    unites = []
    for i in intervalle:
        unites.append(i%10)

    possibilites_unite = len(sorted(unites))
    ecart = max(intervalle) - min(intervalle)
    nombre_possibilites = len(intervalle)

    if(question_produit(possibilites_unite)): 
        return "prochaine question : produit"

    
    return "produit ou division avec quelqu'un d'autre"

def question_produit(possibilites_unite):
    # si on veut savoir le chiffre des unites
    if possibilites_unite == 1 : return False # si on connait deja l'unité, cette question est inutile

    if possibilites_unite < 5: # ou proche, plus c'est proche de 2, plus la question doit etre posee, est pertinante
        return True
    return False

def question_division(ecart):
    # division : utilse qd il y a pas mal d'ecart entre les possibilites (pour voir quel possibilite est la plus proche de la solution)
    if ecart > 40:
        return True
    return False

def question_addition(ecart):
    # on utilise addition pour obtenir intervalle globale (reduire les intervalles de possibilites)
    if ecart > 60:
        return True
    return False

def question_zero(ecart):
    # on utilise zero pour avoir un intervalle de 10
    if ecart > 20:
        return True
    return False


question = evaluer(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
    )

print(question)
    