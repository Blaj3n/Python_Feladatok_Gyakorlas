# 2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy
# három különböző értéket kapott-e!

szamok = []

szam_1 = int(input("Kérek egy számot: "))
szam_2 = int(input("Kérek egy számot: "))
szam_3 = int(input("Kérek egy számot: "))

szamok.append(szam_1)
szamok.append(szam_2)
szamok.append(szam_3)

for szam in szamok:
    if szam != szamok[szam]:
        print("Három különböző érték van a tömbben")
        break
    else:
        print("Van azonos érték a tömbben")
        break
