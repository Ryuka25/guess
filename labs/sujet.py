from random import randint
# les nombres secrets :
xi = []
nombre_participants = 11
for i in range(nombre_participants):
    xi.append(randint(1, 100)) 

# xi = [36, 95, 90, 43, 62, 36, 72, 19, 37, 71, 68]
# i = participants
# 1 = Khanie 2 = Lova 3 = M 4 = patric
xi= [43, 38, 81, 5, 46, 39, 68, 66, 62, 79, 95]

# print(f"\nnombre secrets : {xi}")
# print(f"\nmon nombre : {xi[0]}")

# operations :
def addition(i1, i2):
    if(i1 + i2 >= 180): return randint(180, 199)
    if(i1 + i2 <= 20): return randint(3, 20)
    return i1 + i2

def produit(i1, i2):
    return (i1 * i2) % 10


def division(i1, i2):
    if i1 > i2: return i1 // i2
    return i2 // i1

def zero(i1, i2):
    if(i1 % 10 == 0 and i2 %10 == 0): return abs(i1 // 10 - i2 // 10) + 1
    return abs(i1 // 10 - i2 // 10)

def contrainte_addition(a, b, r):
    if(r >= 180 and r<= 199):
        return a + b >=180
    if(r >= 3 and r <= 20):
        return a+b <= 20
    return r == a + b

def contrainte_produit():
    pass

def contrainte_division():
    pass

def contrainte_zero(a, b, r):
    return abs(a - b) <= (r*10) + 8
