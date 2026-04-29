print("3. feladat")

class Diafilm():
    def __init__(self, cim_, megjelenesi_ev_, filmkocokak_szama_, szines_e_):
        self.cim = cim_
        self.megjelenesi_ev = megjelenesi_ev_
        self.filmkockak_szama = filmkocokak_szama_
        self.szines_e = szines_e_

diafilmek = []
with open('02_feladat/filmek.txt', 'r', encoding='utf-8') as forrasfajl:
    #next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        diafilm = Diafilm(adatok[0], int(adatok[1]), int(adatok[2]), int(adatok[3]))
        diafilmek.append(diafilm)

# print(f'{diafilmek=}')
for diafilm in diafilmek: 
    print(diafilm.cim)
