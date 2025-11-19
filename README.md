# ALGORITHME DEVINER NOMBRE

Voici la structure et contenu des dossiers:

```
/
|- labs/ <-- Dossier de test et benchmarks
|
|- src/
|   |- operations.py <-- Function qui simule les 4 opérations
|   |- problem_constraints.py <-- Function qui ajoute les contraintes sur un problème donnée par rapport aux résultats et les opérations
|   |- utils.py <-- Function utilitaires qui sont généralement utilisé dans l'algorithme principale
|
|- tests/
|   |- test_constraint.py <-- Test que les contrainte ajouté sont bien pris en compte dans le problème
|   |- test_operations.py <-- Test que les opérations ne sont pas éronné
|   |- test_utils.py <-- Test les différents functions utilitaires
|
|- configs.py <-- Fichier de configuration pour l'algorithme et le master
|- main.ipynb <-- Fichier jupyter notebook interactif ou il y a l'implémentation de l'algorithme principale
|- master.py <-- Script python utilisé pour simuler un master
|- requirements.txt <-- Liste des modules/bibliothèques à installer pour intéragir avec le programme
```

# Installation (Dans un environment virtuelle de préférence)

```
> pip install -r requirements.txt
```

# Intéragir avec l'algorithme

Lancer le script `main.ipynb` via jupyter notebook

```
> jupyterlab
```

Ou installer l'extention `Jupyter` dans VSCode et utiliser VSCode comme éditeur intéractif

# Intéragir en tant que master

Lancer le script `master.py` depuis la ligne des commandes

```
> python master.py
```
