# Triggle

## I faza projekta

### Formulacija problema i interfejs

#### Igra

- Strateška igra zauzimanja teritorije
- Za **2 do 4 igrača** (projekat je samo 2)
- Tabla je dužine **stranice 4 do 8**, obično se koristi 4
- Igrači **kače gumice** o ivice i kada dođe do formiranja **najmanjeg trougla** igrač koji je _poslednji odigrao_ **zauzima** taj prostor
- Igra se dok se ne **popuni cela tabla** ili jedan igrač popuni **više od 1/n table** n-broj igrača (29)

#### Predstavljanje stanja problema

- Za predstavljanje stanja smo odlučili ići putem **matrice**
  - Generiše se uz pomoć funkcije **napravi_tablu(n)** koja kreira tablu dužine stranice **n**
  - Svu funkcionalnost iscrtavanja i formatiranja iste matrice u konzoli vrši se uz pomoć funkcije **iscrtaj_tablu(tabla)**
  - Nakog svakog poteza vrši se "refresh" table i unosi se potez
- Funkcije za pomeraje tačaka (sve primaju koordinate početne tačke):
  1. desno(i, j) - pomera tačku za jedno mesto udesno
  2. desno_dole(i, j) - pomera tačku za jedno mesto desno-dole
  3. levo_dole(i, j) - pomera tačku za jedno mesto levo-dole
- Funkcije:

  1. **ispravan_potez(i,j)** ispitujemo da li je tačka i,j unutar šestougla
  2. **izvrsi_potez(stub, move)** izvršavamo potez sa stuba u smeru move i dodajemo ga u set spojenih stubova kako bi kasnije štampali/nalazili upotpunjene trouglove
  3. **proveri_male_trouglove()** prolazi kroz celu tablu i nalazi upotpunjene trouglove i vraća koordinate njihovih tačaka
  4. **obradi_potez(potez)** uzima potez u vidu stringa (C5DL), parsuje ga i izvršava potez ukoliko je to moguće, vraća broj trouglića nakon poteza

- U main funkciji:
  - Pravimo tablu i igrače
  - Biramo ko će prvi da igra
  - Iscrtavamo tablu i rezultat nakon svakog poteza
