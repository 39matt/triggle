from math import sqrt
from Stub import Stub
from Igrac import Igrac
import os

# PUBLIC VARIABLES
n = 0
spojeni_stubovi = set()

def napravi_tablu(n):
    mat = []
    for i in range(2 * n - 1):
        row = []
        for j in range(n * 2 - 1 - abs(n - i - 1)):
            row.append(i * 10 + j)
        mat.append(row)
    return mat

def iscrtaj_tablu(tabla):
    n = len(tabla) // 2 + 1
    visina = 2 * len(tabla) - 1
    sirina = max(len(red) for red in tabla) * 5 + n * 4 

    mreza = [[" " for _ in range(sirina)] for _ in range(visina)]

    # Draw the grid points
    for i, red in enumerate(tabla):
        max_row_len = len(tabla[len(tabla)//2])
        razmaci = (max_row_len - len(red)) * 5 // 2
        
        for j in range(len(red)):
            x = i * 2
            y = razmaci + j * 5 
            if x < visina and y < sirina:
                mreza[x][y] = "●"

    for start, end in spojeni_stubovi:
        try:
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))

            max_row_len = len(tabla[len(tabla)//2])
            
            start_offset = (max_row_len - len(tabla[x1])) * 5 // 2
            end_offset = (max_row_len - len(tabla[x2])) * 5 // 2

            mx1, my1 = x1 * 2, start_offset + y1 * 5
            mx2, my2 = x2 * 2, end_offset + y2 * 5

            if mx1 == mx2:
                for k in range(min(my1, my2) + 1, max(my1, my2)): 
                    mreza[mx1][k] = "─"
            elif my1 < my2:
                mreza[mx1 + 1][my1 + 1] = "╲"
            elif my1 > my2:
                mreza[mx1 + 1][my1 - 1] = "/"
        except Exception as e:
            print(f"Greška pri obradi veze {start} -> {end}: {e}")

    print("+" + "-" * (sirina//2 + sirina//5) + "+")
    for red in mreza:
        print("|" + "".join(red[:sirina//2 + sirina//5]) + "|")
    print("+" + "-" * (sirina//2 + sirina//5) + "+")

def desno(i, j):
    return i , j + 1

def desno_dole(i, j):
    return i + 1, j if i >= n - 1 else j + 1

def levo_dole(i, j):
    return i + 1, j - 1 if i >= n - 1 else j

def ispravan_potez(i, j) -> bool:
    if i >= 2 * n:
        return False
    if i >= 2 * n - 1:
        return False
    if j > 2 * n - 1 - abs(n - i - 1):
        return False
    return True

def izvrsi_potez(stub1: Stub, move):

    tmpStub = Stub(0,0)
    tmpStub.x = stub1.x
    tmpStub.y = stub1.y

    tmpStub2 = Stub(0,0)
    tmpStub2.x = tmpStub.x
    tmpStub2.y = tmpStub.y
    if move == 'D':
        for i in range(4):
            tmpStub2.x, tmpStub2.y = desno(tmpStub2.x, tmpStub2.y)
        if ispravan_potez(tmpStub2.x,tmpStub2.y):
            tmpStub2.x, tmpStub2.y = desno(stub1.x, stub1.y)
            for i in range(3):
                spojeni_stubovi.add((f"{tmpStub.x},{tmpStub.y}",f"{tmpStub2.x},{tmpStub2.y}"))
                tmpStub.nova_vrednost(desno(tmpStub.x,tmpStub.y))
                tmpStub2.nova_vrednost(desno(tmpStub2.x,tmpStub2.y))
            return 1

    elif move == 'DL':
        for i in range(4):
            tmpStub2.x, tmpStub2.y = levo_dole(tmpStub2.x, tmpStub2.y)
        if ispravan_potez(tmpStub2.x,tmpStub2.y):  
            tmpStub2.x, tmpStub2.y = levo_dole(tmpStub.x, tmpStub.y)
            for i in range(3):
                spojeni_stubovi.add((f"{tmpStub.x},{tmpStub.y}",f"{tmpStub2.x},{tmpStub2.y}"))
                tmpStub.nova_vrednost(levo_dole(tmpStub.x,tmpStub.y))
                tmpStub2.nova_vrednost(levo_dole(tmpStub2.x,tmpStub2.y))
            return 1
    elif move == 'DD':
        for i in range(4):
            tmpStub2.x, tmpStub2.y = desno_dole(tmpStub2.x, tmpStub2.y)
        if ispravan_potez(tmpStub2.x,tmpStub2.y):
            tmpStub2.x, tmpStub2.y = desno_dole(tmpStub.x, tmpStub.y)
            for i in range(3):
                spojeni_stubovi.add((f"{tmpStub.x},{tmpStub.y}",f"{tmpStub2.x},{tmpStub2.y}"))
                tmpStub.nova_vrednost(desno_dole(tmpStub.x,tmpStub.y))
                tmpStub2.nova_vrednost(desno_dole(tmpStub2.x,tmpStub2.y))
            return 1

    return None
        
def proveri_male_trouglove():
    triangles = set()

    for (start, end) in spojeni_stubovi:
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        
        for direction in ['D', 'DL', 'DD']:
            if direction == 'D':
                x3, y3 = desno(x2, y2)
                if (f"{x1},{y1}", f"{x3},{y3}") in spojeni_stubovi and (f"{x2},{y2}", f"{x3},{y3}") in spojeni_stubovi:
                    triangles.add(frozenset([(x1, y1), (x2, y2), (x3, y3)]))

            elif direction == 'DL':
                x3, y3 = levo_dole(x2, y2)
                if (f"{x1},{y1}", f"{x3},{y3}") in spojeni_stubovi and (f"{x2},{y2}", f"{x3},{y3}") in spojeni_stubovi:
                    triangles.add(frozenset([(x1, y1), (x2, y2), (x3, y3)]))

            elif direction == 'DD':
                x3, y3 = desno_dole(x2, y2)
                if (f"{x1},{y1}", f"{x3},{y3}") in spojeni_stubovi and (f"{x2},{y2}", f"{x3},{y3}") in spojeni_stubovi:
                    triangles.add(frozenset([(x1, y1), (x2, y2), (x3, y3)]))

    return triangles

def obradi_potez(potez):
    try:
        row_char = potez[0]
        col = int(potez[1])
        direction = potez[2:]
        ispravno = 1
        
        row = ord(row_char.upper()) - ord('A')
        
        if direction not in ['D', 'DD', 'DL']:
            print("Pogrešan smer! Unesi ponovo.")
            return None
        if not ispravan_potez(row, col):
            print("Potez nije ispravan. Pokusaj ponovo.")
            return None

        if direction == 'D':
            ispravno = izvrsi_potez(Stub(row, col), direction)
        elif direction == 'DD':
            ispravno = izvrsi_potez(Stub(row, col), direction)
        elif direction == 'DL':
            ispravno = izvrsi_potez(Stub(row, col), direction)
        
        if ispravno is None:
            return None
        return len(proveri_male_trouglove())
    except Exception as e:
        print(f"Greška pri unosu poteza: {e}")

if __name__ == '__main__':
    os.system('cls')
    stranica_table = n = 4
    tabla = napravi_tablu(stranica_table)
    igracX = Igrac("X")
    igracO = Igrac("O")
    prvi = ''
    trouglovi_count = 0

    print("Izaberite ko prvi igra: X ili O")
    while(prvi != "X" and prvi != 'O'):
        prvi = input()

    trenutni_igrac = igracX if prvi == "X" else igracO
    drugi_igrac = igracO if trenutni_igrac == igracX else igracX
    try:
        while(igracX.trouglici < 1/2 * stranica_table or igracO.trouglici < 1/2 * stranica_table):
            #print(spojeni_stubovi)
            os.system('cls')
            print(f"Guide: Unosite string formata XYSmer. Na primer A5DD - (0,5), Dole desno")
            print(f"Moguce je uneti A-G, 0-{stranica_table * 2 - 1} i D (desno) DD (Dole desno) DL (Dole levo)")
            print(f"Rezultat (X-O): {igracX.trouglici}-{igracO.trouglici}")
            iscrtaj_tablu(tabla)
            print(f"Igrac {trenutni_igrac.znak} je na redu!")

            potez = input()

            trouglovi_count_old = trouglovi_count
            ret = obradi_potez(potez)

            if ret is None:
                print("Neispravan unos, pokusaj ponovo!")
                continue
            else:
                trouglovi_count = ret

            
            for _ in range(trouglovi_count - trouglovi_count_old):
                trenutni_igrac.dodaj_trouglic()

            trenutni_igrac, drugi_igrac = drugi_igrac, trenutni_igrac
    except Exception as ex:
        print(f"Greska pri obradi poteza! {ex}")
    if igracX.trouglici >= 1/2 * stranica_table:
        print("Igrac X je pobednik!")
    elif igracO.trouglici >= 1/2 * stranica_table:
        print("Igrac O je pobednik!")