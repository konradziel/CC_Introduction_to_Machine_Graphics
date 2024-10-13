from PIL import Image
import numpy as np


def rysuj_ramki(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)

    czarny = True
    for i in range(0, min(h, w) // 2, grub):
        if czarny:
            obraz[i:h - i, i:i + grub] = 0  # Lewa pionowa ramka
            obraz[i:h - i, w - i - grub:w - i] = 0  # Prawa pionowa ramka
            obraz[i:i + grub, i:w - i] = 0  # Górna pozioma ramka
            obraz[h - i - grub:h - i, i:w - i] = 0  # Dolna pozioma ramka
        czarny = not czarny

    obraz = obraz.astype(bool)

    nowy_obraz = Image.fromarray(obraz)

    return nowy_obraz


def rysuj_pasy_pionowe(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)

    czarny = True
    for i in range(0, w, grub):
        if czarny:
            obraz[:, i:i + grub] = 0  # Pionowy pas
        czarny = not czarny

    obraz = obraz.astype(bool)

    nowy_obraz = Image.fromarray(obraz)

    return nowy_obraz


def rysuj_wlasne(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)

    # Tworzenie szachownicy
    for i in range(0, h, grub):
        for j in range(0, w, grub):
            if (i // grub + j // grub) % 2 == 0:
                obraz[i:i + grub, j:j + grub] = 0

    obraz = obraz.astype(bool)

    nowy_obraz = Image.fromarray(obraz)

    return nowy_obraz


#Test 2.1
w, h, grub = 600, 300, 20

nowy_obraz = rysuj_ramki(w, h, grub)

nowy_obraz.show()


#Test 2.2
w, h, grub = 300, 100, 20

nowy_obraz = rysuj_pasy_pionowe(w, h, grub)

nowy_obraz.show()

#Test 3.2
w, h, grub = 300, 300, 30

nowy_obraz = rysuj_wlasne(w, h, grub)

nowy_obraz.show()

