szam_lista = [12, 23, -56, 82, 12.23, 69, -100]
import feladatok
import szoveglistak
print("1. feladat:")
feladatok.elsofeladat(szam_lista)

print("2. feladat:")
osszeg = feladatok.masodikfeladat(szam_lista)
print(f"A pozitív számok összege: {osszeg}")

print("3. feladat:")
negativak = feladatok.harmadikfeladat(szam_lista)
print(f"A negatív számok darabszáma: {negativak}")

print("4. feladat:")
nemegesz = feladatok.negyedikfeladat(szam_lista)
print(f"A nem egész számok száma: {nemegesz}")

print("5. feladat:")
atlag = feladatok.otodikfeladat(szam_lista)
print(f"A 3-al osztható számok átlaga: {atlag}")

print("6. feladat:")
legnagyobb = feladatok.hatodikfeladat(szam_lista)
print(f"A legnagyobb szám: {legnagyobb}")

print("7. feladat:")
legkisebb = feladatok.hetedikfeladat(szam_lista)
print(f"A legkisebb szám: {legkisebb}")

print("8. feladat:")
kulonbseg = feladatok.nyolcadikfeladat(szam_lista)
print(f"A legnagyobb és a legkisebb számok különbsége: {kulonbseg}")
