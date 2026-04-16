#--== Python ==--
#Ćwiczenie: Stałe i pobieranie danych z klawiatury.
#
P2 = 1.732                                                      #1.
l = float(input("Podaj liczbę: "))                              #2.
print("Iloczyn/Wynik z mnożenia dwóch liczb wynosi: ", (l*P2))  #3.
w = l*P2                                                        #4.
print("Iloczyn/Wynik z mnożenia dwóch liczb wynosi: ", w)       #5.
"""
Legenda:
1. Zadeklarowanie stałej "P2", która przechowuje
   pierwiastek 2 stopnia z liczby 3.
   W Python'ie przyjęło się pisanie deklaracji stałych DUŻYMI LITERAMI.
   Spowodowane jest to brakiem innego odróżnienia stałej od zmiennej.
   Uwaga: w Python'ie nie ma stałych.
=
2. Pobranie danych (w tym przypadku liczby) z klawiatury.
   Następnie wykonana jest konwersja podanej liczby do typu
   float (czyli do typu rzeczywistego).
   Konwersje na liczbę rzeczywistą umożliwia instrukcja float.
=
3. Wyświetlenie na ekranie tekstu umieszczonego pomiędzy cudzysłowami
   oraz iloczynu (wyniku z mnożenia) dwóch liczb.
   Liczby przechowywane są w stałej "P2" i zmiennej "l".
=
4. Obliczenie iloczynu (wyniku z mnożenia) dwóch liczb i przypisanie
   tego wyniku do zmiennej "w". Liczby przechowywane są w stałej "P2"
   i zmiennej "l".
=
 5. Wyświetlenie na ekranie tekstu umieszczonego pomiędzy cudzysłowami
    oraz zawartości zmiennej "w".
"""