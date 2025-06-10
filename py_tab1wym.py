#--== Python ==--
#Tablica jednowymiarowa.
#(c)by Jan T. Biernat
#
#Opis:
#Napisz program, który poprosi użytkownika o podanie
#10 liczb całkowitych i zapisze je do tablicy/listy.
#Następnie obliczy:
#1. Sumę podanych liczb.
#2. Poda ilość liczb parzystych.
#3. Poda najmniejszą i największą liczbę w tablicy/liście.
#
#
#Deklaracja zmiennych.
tab = []
liczba :int = 0
ilosc = 0
#
#Program.
for i in range(10):                         #1.
    liczba = int(input("Podaj liczbę: "))   #2.
    tab.append(liczba)                      #3.
print("\nPodałeś następujące liczby:")      #4.
for i in range(len(tab)):                   #5.
    print(tab[i])                           #6.
    if(tab[i] % 2 == 0): ilosc+= 1          #7.
print("Suma = ", sum(tab))                  #8.
print("Ilość liczb parzystych: ", ilosc)    #9.
print("Najmniejsza liczba to: ", min(tab))  #10.
print("Największa liczba to: ", max(tab))   #11.
"""
Legenda:
1.  Pętla FOR oraz instrukcje wewnątrz pętli będą powtórzone
    10 razy.
2.  Pobranie danych (w tym przykładzie są to liczby całkowite) z klawiatury.
    Po pobraniu liczby z klawiatury następuje przekonwertowanie
    jej na wartość liczbową całkowitą (instrukcja int).
    Następnie następuje przypisanie liczby całkowitej do zmiennej
    liczbowej całkowitej "liczba".
3.  Dodanie pobranej liczby całkowitej do tablicy/listy o nazwie "tab".
4.  Wyświetl na ekranie tekst umieszczony pomiędzy cudzysłowami.
5.  Pętla FOR oraz zawarte wewnątrz instrukcje będą wykonane 10 razy.
    To znaczy: a) na ekranie zostanie wyświetlona zawartość tablicy/listy
                  o nazwie "tab",
               b) zostaną wykryte liczby parzyste.
6.  Wyświetlenie na ekranie zawartości tablicy/listy o nazwie "tab".
7.  Sprawdzenie, czy podana przez użytkownika liczba całkowita jest parzysta.
    Jeżeli tak, to zwiększ zawartość zmiennej "ilosc" o wartość 1.
8.  Wyświetl na ekranie tekst znajdujący się pomiędzy cudzysłowami
    oraz oblicz i wyświetl sumę liczb znajdujących się w tablicy
    (na liście) o nazwie "tab".
9.  Wyświetl na ekranie tekst umieszczony pomiędzy cudzysłowami
    oraz zawartość zmiennej "ilosc", określającą ilość liczb parzystych.
10. Wyświetl na ekranie tekst znajdujący się pomiędzy cudzysłowami
    oraz wyświetl liczbę najmniejszą, jak znajduje się w tablicy
    (na liście) o nazwie "tab".
11. Wyświetl na ekranie tekst znajdujący się pomiędzy cudzysłowami
    oraz wyświetl liczbę największą, jak znajduje się w tablicy
    (na liście) o nazwie "tab".
"""
