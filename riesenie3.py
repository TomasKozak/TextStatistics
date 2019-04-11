# 3. zadanie: najcastejsie
# autor: Tomáš Kozák
# datum: 20.11.2018

tab = []

def citaj(meno_suboru):
    t = open(meno_suboru, 'r', encoding='utf-8-sig')
    slova = t.read().split()
    dlzka = len(slova)
    for i in range(dlzka):
        tab.append([slova[i],slova.count(slova[i])])
    t.close()

def najcastejsie():
    pole = tab[0][1]
    dalsie = tab[1][1]
    pomocne = []
    for i in range(len(tab)):
        dalsie = tab[i][1]
        if pole < dalsie:
            pole = dalsie
    for i in range(len(tab)):
        if pole == tab[i][1]:
            pomocne.append(tab[i][0])
    dlzka = len(pomocne)
    for i in range(dlzka):
        if pomocne.count(pomocne[i]) > 1:
            pomocne[i] = ''
    pomocne = ' '.join(pomocne).split()
    return pomocne

def len_pocet(n):
    pole = []
    for i in range(len(tab)):
        if n == tab[i][1]:
            pole.append(tab[i][0])
    dlzka = len(pole)        
    for i in range(dlzka):
        if pole.count(pole[i]) > 1:
           pole[i] = ''
    pole = ' '.join(pole).split()
    return pole

def najdlhsie():
    dlzka = len(tab[0][0])
    jednoDlzka = len(tab[1][0])
    pole = []
    for i in range(len(tab)):
        jednoDlzka = len(tab[i][0])
        if dlzka < jednoDlzka:
            dlzka = jednoDlzka
    for i in range(len(tab)):
        if dlzka == len(tab[i][0]):
            pole.append(tab[i][0])
    rozsah = len(pole)
    for i in range(rozsah):
        if pole.count(pole[i]) > 1:
            pole[i] = ''
    pole = ' '.join(pole).split()
    return pole

def najkratsie():
    dlzka = len(tab[0][0])
    jednoDlzka = len(tab[1][0])
    pole = []
    for i in range(len(tab)):
        jednoDlzka = len(tab[i][0])
        if dlzka > jednoDlzka:
            dlzka = jednoDlzka
    for i in range(len(tab)):
        if dlzka == len(tab[i][0]):
            pole.append(tab[i][0])
    rozsah = len(pole)
    for i in range(rozsah):
        if pole.count(pole[i]) > 1:
            pole[i] = ''
    pole = ' '.join(pole).split()
    return pole
    

def len_dlzka(n):
    pole = []
    for i in range(len(tab)):
        if n == len(tab[i][0]):
            pole.append(tab[i][0])
    dlzka = len(pole)
    for i in range(dlzka):
        if pole.count(pole[i]) > 1:
            pole[i] = ''
    pole = ' '.join(pole).split()
    return pole

if __name__ == '__main__':
    citaj('text1.txt')
    print('najcastejsie:', najcastejsie())
    print()
    print('najdlhsie:', najdlhsie())
    print()
    print('najkratsie:', najkratsie())
    print()
    print('len pocet 5:', len_pocet(5))
    print()
    print('len pocet 10:', len_pocet(10))
    print()
    print('len dlzka 10:', len_dlzka(10))
    print('pocet roznych slov =', len(tab))

