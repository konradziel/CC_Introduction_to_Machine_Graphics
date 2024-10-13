from PIL import Image
import numpy as np


def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_bazowy = np.asarray(obraz_bazowy).astype(np.int_)
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)

    h_bazowy, w_bazowy = tab_bazowy.shape[:2]
    h_wstawiany, w_wstawiany = tab_wstawiany.shape[:2]

    n_k = min(h_bazowy, n + h_wstawiany)  # końcowy zakres wstawiania w pionie
    m_k = min(w_bazowy, m + w_wstawiany)  # końcowy zakres wstawiania w poziomie
    n_p = max(0, n)  # początkowy zakres w pionie
    m_p = max(0, m)  # początkowy zakres w poziomie

    # Wstawienie obrazu w miejsce w obrazie bazowym
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowy[i][j] = tab_wstawiany[i - n][j - m]

    # Zamiana z powrotem na obraz
    wynikowy_obraz = Image.fromarray(tab_bazowy.astype(bool))

    return wynikowy_obraz


bazowy_obraz = Image.new('1', (300, 300), 0)  # Biały obraz 300x300
wstawiany_obraz = Image.new('1', (100, 100), 1)  # Czarny obraz 100x100

# Pozycja, gdzie wstawimy obraz
m, n = 100, 100

nowy_obraz = wstaw_obraz_w_obraz(bazowy_obraz, wstawiany_obraz, m, n)

nowy_obraz.show()
