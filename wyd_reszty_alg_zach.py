#--== Wydawanie reszty algorytmem zachłannym ==--
#Copyright (c)by Jan T. Biernat
#
print("--== Wydawanie reszty algorytmem zachłannym ==--")
Nominaly = [ 50, 20, 10, 5, 2, 1 ]
p = 0
reszta = int(input("Ile reszty ma wydać: "))
print("Reszta: ")
while (reszta > 0):
    while reszta >= Nominaly[p]:
      reszta -= Nominaly[p]
      print(Nominaly[p])
    p+= 1
print("")
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