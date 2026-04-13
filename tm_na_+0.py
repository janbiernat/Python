#Tabliczka mnożenia na krzyż.
#(c) by Jan T. Biernat
#
#Napisz program, który wyświetli
#tabliczkę mnożenia na krzyż.
#
ROZMIAR = 10                                #1
#Nagłówek dla kolumn.
print("  ", end="")                         #2
for n in range(ROZMIAR):                    #3
    print(f"{(n+1):4}", end="")             #4
print("")                                   #5
#
#Nagłówek dla wierszy.
for a in range(ROZMIAR):                    #6
    print(f"{(a+1):2}", end="")             #7
    for b in range(ROZMIAR):                #8
        print(f"{((a+1)*(b+1)):4}", end="") #9
    print("")                               #5
print("")                                   #5
input("Naciśnij ENTER ...")                 #10
"""
Legenda:
1. Wiersz 7. ROZMIAR = 10
   Zadeklarowanie zmiennej liczbowej całkowitej o nazwie
   ROZMIAR z przypisaną wartością 10.
   W języku Python nie ma stałej. Umownie stałą piszemy
   dużymi literami, by nie zmieniać jej zawartości.
=
2. Wiersz 9. print("  ", end="")
   Wyświetlenie na ekranie dwóch znaków pustych znajdujących się
   pomiędzy cudzysłowami. Do wyświetlenia na ekranie znaków służy
   instrukcja print. Zapis end="" powoduje wyświetlenie całego tekstu
   w 1 wierszu.
=
3. Wiersz 10. for n in range(ROZMIAR):
   Wykonanie instrukcji zawartych w pętli FOR z góry określoną ilość razy.
   Instrukcje są przesunięte minimum o 1 znak pusty w prawą stronę,
   względem pętli FOR do której należą.
   Np.:  for n in range(ROZMIAR):
          print("witaj")
   Pętla FOR posiada dwa parametry:
     Parametr 1 jest umieszczony pomiędzy
                wyrazem for a in. Zazwyczaj
                jest to liczba całkowita 
                określająca wartość początkowa, np. 1
                lub zmienna liczbowa całkowita np. "n".
     Parametr 2 zawiera instrukcję RANGE(),
                która posiada jeden parametr.
                W tym parametrze umieszcza się
                liczbę całkowitą określającą
                ile razy mają być wykonane
                instrukcje należące do pętli FOR
                lub zmienną liczbą całkowitą zawierającą
                wartość liczbową określającą ilość powtórzeń
                pętli FOR (w tym przykładzie jest to zmienna ROZMIAR).
=
4. Wiersz 11. print(f"{(n+1):4}", end="")
   Wyświetlenie na ekranie nagłówków dla kolumn
   tabliczki mnożenia.
   Zapis f"{(n+1):4}" określa:
     4.1. f"{ - informuje, ze liczby będą formatowane na ekranie.
     4.2. (n+1) - informuje, że zawartość zmiennej liczbowej całkowitej
                  "n" będzie zawsze zwiększana o wartość 1.
     4.3. :4} - informuje, że przed liczbą posiadającą 1 cyfrę
                będą umieszczane 3 znaki puste, natomiast przed
                liczbą 2 cyfrową będą umieszczane dwa znaki puste.
     4.4 end="" - zapis informuje, że wszystkie liczby będą wyświetlone
                  w 1 wierszu.
=
5. Wiersz 12. print("") - przeniesienie kursora tekstowego do kolejnego wiersza.
=
9. Wiersz 18. print(f"{((a+1)*(b+1)):4}", end="")
   Wyświetlanie na ekranie wyniku z pomnożenia na krzyż
   nagłówków kolumn i nagłówków wierszy.
   9.1. f" - przed cudzysłowem oznacza, że liczba będzie formatowana.
   9.2. a+1 - zwiększenie zawartości zmiennej liczbowej całkowitej "a"
        o wartość 1. Np.: zmienna a przechowuje wartość 5 po dodaniu
                          1 wartość będzie wynosiła 6.
   9.3. b+1 - zwiększenie zawartości zmiennej liczbowej całkowitej "b"
        o wartość 1. Np.: zmienna a przechowuje wartość 5 po dodaniu
                          1 wartość będzie wynosiła 6.
   9.4. (a+1)*(b+1) - pomnożenie powiększonych o wartość 1 zawartości
                      zmiennych liczbowych całkowitych "a" i "b".
   9.5. :4}" - formatowanie wyniku z pomnożenia 2 liczb przechowywanych
               w zmiennych "a" i "b" uprzednio powiększonych o wartość 1.
               Formatowanie polega na przesunięciu wyniku i dodanie
               przed wynikiem pustych znaków wiodących.
               Np.: mamy wynik 9 to przed liczbą 9 zostaną umieszczone
                    trzy znaki puste (tj. znaki spacji), które razem
                    z liczbą będą tworzyć ciąg składający się z 4 znaków.
                Dzięki formatowaniu, możliwe jest wyświetlenie
                pogrupowanych liczb w następujący sposób:
                jednostki pod jednostkami, dziesiątki pod dziesiątkami,
                setki pod setkami i tak dalej.
   9.6. end="" - powoduje wypisanie wszystkich 10 wyników w 1 wierszu.
=
10. Wiersz 21. Oczekiwanie na naciśnięcie klawisza ENTER przez użytkownika.
=
"""
