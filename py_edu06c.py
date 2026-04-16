#--== Python ==--
#Ćwiczenie: Pętla FOR.
#
for n in range(10):              #1
 print("Liczba: ", f"{(n+1):2}") #2
print("Koniec")                  #3
"""
Legenda:
1. for n in range(10):
   Wykonanie instrukcji zawartych w pętli FOR z góry określoną ilość razy.
   W tym przykładzie instrukcja PRINT będzie powtórzona 10 razy.
   Konstrukcja pętli FOR jest następująca:
      for wartosc_poczatkowa in range(wartosc_koncowa):
       instrukcja1
       instrukcja2
       ...
       instrukcjaN
   Instrukcje którymi steruje pętla FOR muszą być przesunięte
   względem pętli minimum o jeden znak pusty (tj. znak spacji)
   w prawą stronę.
   W parametrze WARTOSC_POCZATKOWA umieszczamy zmienną liczbową
                całkowitą np. n lub liczbę całkowitą np. 0.
   W parametrze WARTOSC_KONCOWA umieszczamy zmienną liczbową całkowitą
                np. rozmiar lub liczbę całkowitą np. 10.
                Parametr WARTOSC_KONCOWA decyduje o ilości powtórzeń
                         instrukcji zawartych w pętli FOR.
               Instrukcja RANGE() w pętli FOR służy do generowania kolejnych
                                  liczb całkowitych, co pozwala na kontrolę
                                  wykonywania powtórzeń instrukcji w pętli.
                                  Instrukcja RANGE() Jest kluczowa, gdy chcesz
                                  wykonać dany blok instrukcji z góry określoną
                                  ilość razy.
=
2. print("Liczba: ", f"{(n+1):2}")
   Wyświetla na ekranie tekst umieszczony pomiędzy cudzysłowami
   oraz zawartość zmiennej liczbowej całkowitej "n" powiększonej
   zawsze o wartość 1. Powiększenie zawartości zmiennej liczbowej
   "n" o wartość 1, powoduje wyświetlanie ciągu liczb od wartości
   1 do 10. W innym przypadku ciąg liczb byłby wyświetlany od
   wartości 0 do 9.
   Zapis f" informuje, że liczba będzie formatowana.
   Zapis ):2} informuje, że przed liczbą składającą się z 1 cyfry
              zostanie wstawiony znak pusty.
              Np.:  1
                   10
=
3. print("koniec")
   Wyświetla na ekranie komunikat "Koniec".
"""
