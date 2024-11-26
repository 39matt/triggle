import string



class Tabla:
    def __init__(self, dimenzija):
        self.dimenzija = dimenzija
        self.matrica = []

        self.definisi_tablu()
        

    def definisi_tablu(self):
        for i in range(3, self.dimenzija):
            row = [" "] * (2 * self.dimenzija - 1)
            for j in range(self.dimenzija - 1 - i, self.dimenzija + i, 2):
                row[j] = "."
            self.matrica.append(row)
        for i in range(self.dimenzija - 4):
            row = [" "] * (2 * self.dimenzija - 1)
            for j in range(i + 1, 2 * self.dimenzija - 2 - i, 2): 
                row[j] = "."
            self.matrica.append(row)
        
    def iscrtaj_tablu(self):
        print("  ", end="")
        for broj in range(1, self.dimenzija*2):
            if broj > 9:
                print(f"{broj} ", end="")
            else:
                print(f"{broj}  ", end="")  # Numeracija kolona
        print()

        slova = string.ascii_uppercase
        for i, red in enumerate(self.matrica):
            print(f"{slova[i]} ", end="")  # Oznake redova slovima
            for elem in red:
                print(f"{elem}  ", end="")
            print('\n')


if __name__ == '__main__':
    tabla = Tabla(7)
    tabla.iscrtaj_tablu()