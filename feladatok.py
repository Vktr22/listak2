def elsofeladat(szam_lista):
    for i in range(0,len(szam_lista),1):
        print(f"A lista {i}. eleme: {szam_lista[i]}")


def masodikfeladat(szam_lista):
    print()
    i=0
    osszeg = 0
    while i < len(szam_lista):
        if szam_lista[i] > 0:
            osszeg += szam_lista[i]
        i += 1

    return osszeg

def harmadikfeladat(szam_lista):
    print()
    negativak = 0
    i = 0
    while i < len(szam_lista):
        if szam_lista[i] < 0:
            negativak += 1
        i += 1

    return negativak

def negyedikfeladat(szam_lista):
    print()
    i = 0
    nemegesz = 0
    while i < len(szam_lista):
        if type(szam_lista[i]) == float:
            nemegesz += 1
        i += 1

    return nemegesz

def otodikfeladat(szam_lista):
    print()
    i = 0
    osszeg = 0
    darab = 0
    atlag = 0
    while i < len(szam_lista):
        if szam_lista[i] % 3 == 0:
            osszeg += szam_lista[i]
            darab += 1
        i += 1
    atlag = osszeg / darab

    return atlag

def hatodikfeladat(szam_lista):
    print()
    legnagyobb = 0
    i = 0
    while i < len(szam_lista):
        if szam_lista[i] > legnagyobb:
            legnagyobb = szam_lista[i]
        i += 1
    print(f"A legnagyobb szám: {legnagyobb}")
    return legnagyobb

def hetedikfeladat(szam_lista):
    print()
    legkisebb = 0
    i = 0
    while i < len(szam_lista):
        if szam_lista[i] < legkisebb:
            legkisebb = szam_lista[i]
        i += 1

    return legkisebb

def nyolcadikfeladat(szam_lista):
    legkisebb = hetedikfeladat(szam_lista)
    legnagyobb = hatodikfeladat(szam_lista)
    print()
    kulonbseg = legnagyobb - legkisebb

    return kulonbseg