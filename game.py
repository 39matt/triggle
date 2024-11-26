import string

class Tabla:
    def __init__(self, dimenzija):
        self.dimenzija = dimenzija
        self.matrica = []

        
        for i in range(3, self.dimenzija):
            row = [" "] * (2 * self.dimenzija - 1)
            for j in range(self.dimenzija - 1 - i, self.dimenzija + i, 2):  # Step by 2 to leave space
                row[j] = "."
            self.matrica.append(row)
    
        # Bottom half (excluding the middle row)
        for i in range(self.dimenzija - 4):
            row = [" "] * (2 * self.dimenzija - 1)
            for j in range(i + 1, 2 * self.dimenzija - 2 - i, 2):  # Step by 2 to leave space
                row[j] = "."
            self.matrica.append(row)
                
        
    def iscrtaj_tablu(self):
        for row in self.matrica:
            print("".join(row))
       


if __name__ == '__main__':
    tabla = Tabla(7)
    tabla.iscrtaj_tablu()