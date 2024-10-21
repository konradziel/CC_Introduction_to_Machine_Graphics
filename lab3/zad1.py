import numpy as np
from PIL import Image

def rysuj_ramki_szare(w, h, grub, kolor_ramki, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h-grub, grub:w-grub] = kolor
    return Image.fromarray(tab)

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            if j < w:
                for i in range(h):
                    tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

w = 300
h = 200
grub = 5

im_ramka = rysuj_ramki_szare(w, h, grub, 100, 200)
im_ramka.show()
im_ramka.save("obrazy/im_ramka.png")

im_pasy = rysuj_pasy_pionowe_szare(w, h, grub, 50)
im_pasy.show()
im_pasy.save("obrazy/im_pasy.png")
