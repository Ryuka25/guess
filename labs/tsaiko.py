from sujet import addition, produit, division, zero

personnes = ["K", "M", "A", "L", "V", "S", "F"]
xi = [43, 38, 81, 5, 46, 39, 68] # liste aleatoire

def addition_with(i2, i1 = 0):
    r = addition(xi[i1], xi[i2])
    print(f"\naddition de {personnes[i1]} et {personnes[i2]} : {r}")
    return r

def produit_with(i2, i1 = 0):
    r = produit(xi[i1], xi[i2])
    print(f"\nproduit de {personnes[i1]} et {personnes[i2]} : {r}")
    return r

def division_with(i2, i1 = 0):
    r = division(xi[i1], xi[i2])
    print(f"\ndivision de {personnes[i1]} et {personnes[i2]} : {r}")
    return r

def zero_with(i2, i1 = 0):
    r = zero(xi[i1], xi[i2])
    print(f"\nzeros entre {personnes[i1]} et {personnes[i2]} : {r}")
    return r

def onePersonAllOperations(i2, i1=0):
    print(f"\n ====== Opérations entre {personnes[i1]} et {personnes[i2]} =========")
    addition_with(i2, i1)
    produit_with(i2, i1)
    division_with(i2, i1)
    zero_with(i2, i1)
    print("\n================== fin ==================")

def launchAll():
    for i in range(1, len(xi)):
       onePersonAllOperations(i)


launchAll()