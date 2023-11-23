szoveg_lista = ["Alma", "Körte", "Szilva", "Szőlő", "alma"]

"""
1. Hány alma/Alma van a listában?
2. Hány Sz betűvel kezdődő szöveg van a listában?
3. Melyik a leghosszabb szó? Mekkora a szossza? Hányadik helíen áll a listában?
"""
def hanyalma (szoveg_lista):
    i = 0
    darab = 0
    while i < len(szoveg_lista):
        if szoveg_lista[i] == "alma" or szoveg_lista == "Alma":
            darab += 1
        i += 1
    print(f"{darab} alma van a listában.")