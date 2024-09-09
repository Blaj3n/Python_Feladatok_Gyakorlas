# 1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legkisebb értéket ezek közül!

minimum = int(input("Kérem az első számot: "))
for i in range(1, 5, 2): # 2-ig fg futni, azaz lesz egy 0. köre, és egy 1. köre.
    szam = int(input("Kérek még egy számot: "))
    if minimum > szam:
        minimum = szam
print(f"A legkisebb érték a 3 szám közül: {minimum} ")

# [1, 101[, 2
# 1. range(meddig menjen 0-tól i - 1) range(5) = [0, 1, 2, 3, 4],
# 2. range(mettől, meddig - 1), range(2, 7) = [2, 3, 4, 5, 6]
# 3. range([kezdő, meddig menjen -1[, hányasával), range(1, 5, 2) = [1, 3]
# FONTOS, hogy a harmadikat, tehát, hogy hányasával lépkedjen csak harmdikként adhatod meg.