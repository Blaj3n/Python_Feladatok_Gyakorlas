# 1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legkisebb értéket ezek közül!

szamok = []

szam_1 = int(input("Kérek egy számot: "))
szam_2 = int(input("Kérek egy számot: "))
szam_3 = int(input("Kérek egy számot: "))

szamok.append(szam_1)
szamok.append(szam_2)
szamok.append(szam_3)

print(f"A legkisebb érték a 3 szám közül: {min(szamok)}")
