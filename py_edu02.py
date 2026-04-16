#--== Python ==--
#Ćwiczenie: Zmienna i formatowanie liczby.
#
w = 5/3                                               #1
print("Wynik z dzielenie wynosi: ", w)                #2
print("Wynik z dzielenie wynosi: ", format(w, '.2f')) #3
"""
Legenda:
1. Zadeklarowanie zmiennej "w" i przypisanie do niej wyniku
   z dzielenia dwóch liczb.
=
2. Wyświetlenie na ekranie tekstu umieszczonego pomiędzy
   cudzysłowami oraz wyniku z dzielenia dwóch liczb.
   Wynik z dzielenia przechowywany jest w zmiennej "w".
=
3. Wyświetlenie na ekranie tekstu umieszczonego pomiędzy
   cudzysłowami oraz wyniku z dzielenia dwóch liczb.
   Wynik z dzielenia przechowywany jest w zmiennej "w".
   Przed wyświetleniem wyniku na ekranie, następuje jego
   formatowanie. Formatowanie polega na ograniczeniu wyświetlanych
   liczb po przecinku. Do formatowania liczb używamy instrukcji "format".
   Zapis .2f oznacza, że po przecinku będą wyświetlane tylko 2 liczby.
"""
