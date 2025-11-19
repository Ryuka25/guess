from random import randint
from src.operations import addition, multiplication, division, zero

MAX_NUMBER = 100
MIN_NUMBER = 1

PEOPLES = [
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

OPERATION_MAP = {"ADD": addition, "MUL": multiplication, "DIV": division, "ZER": zero}

#################################################
# MASTER CONFIGS
#################################################

# Hidden numbers are generated automatically
# Turn to True and set the hidden numbers manually
MANUAL_HIDDEN_NUMBERS = False
HIDDEN_NUMBERS = {
    "K": 43,
    "L": 38,
    "P": 81,
    "O": 5,
    "A": randint(MIN_NUMBER, MAX_NUMBER + 1),
    "B": randint(MIN_NUMBER, MAX_NUMBER + 1),
    "C": randint(MIN_NUMBER, MAX_NUMBER + 1),
    "D": randint(MIN_NUMBER, MAX_NUMBER + 1),
    "E": randint(MIN_NUMBER, MAX_NUMBER + 1),
    "F": randint(MIN_NUMBER, MAX_NUMBER + 1),
    "G": randint(MIN_NUMBER, MAX_NUMBER + 1),
}
