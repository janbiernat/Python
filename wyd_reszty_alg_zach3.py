#--== Wydawanie reszty algorytmem zachłannym 3 ==--
#Copyright (c)by Jan T. Biernat
#
print("--== Wydawanie reszty algorytmem zachłannym 3 ==--")
Nominaly = []
p = 0
i = 0
#
#Pobierz dane od użytkownika
ile = int(input("Ile jest nominałów: "))
print("\n UWAGA: Proszę podawać nominały od największego do najmniejszego! \n")
while (i < ile):
    Nominaly.append(int(input("Podaj nominał: ")))
    i += 1
reszta = int(input("Ile reszty ma wydać: "))
#
#Wydanie reszty
print("Reszta: ")
while (reszta > 0):
    while reszta >= Nominaly[p]:
      reszta -= Nominaly[p]
      print(Nominaly[p], " ", end="")
    p+= 1
print("\n")
"""
Opis: Algorytm zachłanny wykorzystany do wydawania reszty,
      polega na użyciu największego nominału w każdym kroku.
      Największy wykorzystany nominał nie może przekroczyć
      pozostałej kwoty do wydania.
=
Przykład:
Mamy do wydania resztę w kwocie 16zł.
W kasie posiadamy następujące
nominały: 5zł, 2zł, 1zł.
Wynikiem działania algorytmu będzie: 5zł, 5zł, 2zł, 2zł i 2zł.
=
Algorytm działa w następujący sposób:
1. Podajemy nominały od największego
   do najmniejszego lub sortujemy
   podane nominały od największego
   do najmniejszego.
2. Na początku wydajemy największy
   nominał lub nominał równy wartości
   reszty do wydania.
3. Po wydaniu nominału odejmujemy
   go od reszty, którą mamy wydać.
4. Wróć do kroku 2 i 3.
   Powtarzaj tak długo, aż
   reszta do wydania będzie
   równa zero.
"""
