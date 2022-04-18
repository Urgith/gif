import matplotlib.pyplot as plt
import imageio
import random
import time


def gif(dlugosc, szybkosc, rozmiar): # definiujemy funkcję tworzenie pliku gif
  '''funkcja ta tworzy plik gif należy podać długość tego pliku(liczba obrazków), szybkość przechodzenia z 1 pliku na kolejny oraz rozmiar planszy'''

  kierunek = 's'                     # na początku zaczynamy jako kwadrat
  sztuczka = 0                       # zmienna, która znormalizuje ruch naszego agenta
  k = 0                              # zmienna, określająca ilość zmian koloru

  x = 0                              # początkowa współrzędna x
  y = 0                              # początkowa współrzędna y
  przejscie = 0                      # liczba przejść poza granicę planszy

  d = []                             # współrzędne x przed pierwszym przejsciem poza granicę planszy
  e = []                             # wspołrzędne y przed pierwszym przejsciem poza granicę planszy
  lista = []                         # zmienna zawierająca wszystkie współrzędne list powstałych po pierwszym przejściu przez granicę planszy
  kolory = [(random.random(), random.random(), random.random())]             # zmienna zawierająca kolory wykresów

  for i in range(dlugosc):                                                   # główna pętla generująca obrazki formatu .png
    fig, _ = plt.subplots()                                                 # tworzymy zmienną, która przechowuje nasze obrazki
    plt.xticks(range(-rozmiar, rozmiar + 1))
    plt.yticks(range(-rozmiar, rozmiar + 1))
    c = plt.axis([-rozmiar - 0.5, rozmiar + 0.5, -rozmiar - 0.5, rozmiar + 0.5]) # tworzymy stabilny obszar w zakresie [(-4,4)x(-4,4)]
    plt.grid(True)                                                               # tworzymy siatkę wykresu

    if przejscie >= 1:                                                       # jeżeli conajmniej raz przeszliśmy przez siatkę, to:
      for j in range(len(lista)):                                            # pętla dodająca nowe kolory
        if j > k - 2 - (przejscie - 1):
          k += 1
          kolory.append((random.random(), random.random(), random.random()))

      lista[przejscie - 1].append([x, y])                                    # do najnowszej części wykresu dodajemy najnowsze współrzędne
      for l in range(len(lista)):                                            # dla każdego elementu z listy (w której mamy nowo powstałe wykresy:
        wspolrzednex = []                                                    # zerujemy wspolrzedne x badanej części wykresu
        wspolrzedney = []                                                    # zerujemy wspolrzedne y badanej części wykresu

        for j in range(len(lista[l])):                                       # dodajemy do współrzędnych odpowiednie współrzędne:
          wspolrzednex.append(lista[l][j][0])                                # x
          wspolrzedney.append(lista[l][j][1])                                # y

        plt.plot(wspolrzednex, wspolrzedney, 'o:', color=kolory[l + 1], linewidth=2, markersize=5)            # rysujemy ślad dla każdego podwykresu z zaznaczeniem miejsc końcowych
        plt.plot(lista[przejscie - 1][-1][0], lista[przejscie - 1][-1][1], kierunek, color='k', markersize=8) # rysujemy agenta na aktualnie zajmowanej pozycji

    else:                                                        # jeżeli jeszcze nie przeszliśmy poza siatkę, to:
      d.append(x)                                                # dodajemy do listy współrzędnych x
      e.append(y)                                                # dodajemy do listy współrzędnych y

    plt.plot(d, e, 'o:', color=kolory[0], linewidth=2, markersize=5) # rysujemy pierwszą linię wraz z miejscem końcowym, której elementów było coraz więcej aż do pierwszego przejścia

    try:                                                         # próbuj rysować agenta:
      plt.plot(d[i], e[i], kierunek, Color='k', markersize=8)
    except:                                                      # jeżeli przekroczymy zakres(przejdziemy pierwszy raz poza granicę), to:
      pass                                                       # nic nie rób(nie rysuj już agenta)

    if sztuczka == 0:          # jeżeli w ostatnim ruchu nasz agent nie przeszedł poza granicę:
      a = random.randint(1, 4) # losujemy liczbę z zakresu (1-4), w zależności od wylosowanej liczby nasz agent będzie poruszał się w danym kierunku
    else: sztuczka -= 1        # to gwarantuje nam wystąpienie takiej sytuacji tylko jednorazowo

    if a == 1:                 # ruch w górę
      y += 1                   # przesówamy o 1 w górę
      kierunek = '^'           # odpowiednio zmieniamy kierunek

      if y > c[3]:             # jeżeli wyszliśmy poza siatkę w górę:
        sztuczka = 1           # przez 1 powtórzenie pętli nie zmieni się kierunek
        k += 1
        lista.append('a')      # sztucznie tworzymy slot w liście
        lista[przejscie] = []  # przygotowywujemy sobie miejsce dla nowej części wykresu
        y = c[2] + 0.5         # przesówamy się na maxa w dół
        przejscie += 1         # zapisujemy, ze wykonało się kolejne przejście

    elif a == 2:               # ruch w prawo: -||-(podobnie)
      x += 1
      kierunek = '>'

      if x > c[1]:
        sztuczka = 1
        k += 1
        lista.append('a')
        lista[przejscie] = []
        x = c[0] + 0.5
        przejscie += 1

    elif a == 3:               # ruch w dół: -||-(podobnie)
      y -= 1
      kierunek = 'v'

      if y < c[2]:
        sztuczka = 1
        k += 1
        lista.append('a')
        lista[przejscie] = []
        y = c[3] - 0.5
        przejscie += 1

    else:                      # ruch w lewo: -||-(podobnie)
      x -= 1
      kierunek = '<'

      if x < c[0]:
        sztuczka = 1
        k += 1
        lista.append('a')
        lista[przejscie] = []
        x = c[1] - 0.5
        przejscie += 1

    fig.savefig('filename' + str(i) + '.png')          # zapisujemy wszystkie powstałe pliki(to jest w pętli głównej)
    plt.close('all')                                       # zamykamy plik, który wcześniej zapisalismy, aby zużywać zdecydowanie mniej pamięci

  pliki = []                                           # tworzymy listę z plikami
  for i in range(dlugosc):
    pliki.append('filename' + str(i) + '.png')         # dodajemy stworzone pliki(obrazki) do listy plików

  otwarte_pliki = []
  for i in range(len(pliki)):
    otwarte_pliki.append(imageio.imread(pliki[i]))     # otwieramy pliki, które zapiszemy jako plik gif
  imageio.mimsave('koniec.gif', otwarte_pliki, duration=szybkosc) # tworzymy plik gif

start = time.time()                                    # tu rozpoczyna się nasz program
gif(100, 0.1, 8)                                       # odpalamy program
print('Tyle trwał nasz program:', time.time() - start) # pauzujemy stoper
