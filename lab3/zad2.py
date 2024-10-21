from PIL import Image
import numpy as np

def negatyw(obraz):
    if obraz.mode == '1':
        negatyw_obraz = obraz.point(lambda p: 1 - p)
    elif obraz.mode == 'L':
        negatyw_obraz = obraz.point(lambda p: 255 - p)
    elif obraz.mode == 'RGB':
        tab = np.array(obraz)
        negatyw_obraz = Image.fromarray(255 - tab)
    else:
        raise ValueError(f"Nieznany tryb obrazu: {obraz.mode}")
    return negatyw_obraz

def rysuj_ramke_kolor(w, h, grub, kolor_ramki, kolor_tla):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h - grub, grub:w - grub, 0] = kolor_tla[0]
    tab[grub:h - grub, grub:w - grub, 1] = kolor_tla[1]
    tab[grub:h - grub, grub:w - grub, 2] = kolor_tla[2]
    return Image.fromarray(tab)

def rysuj_po_skosie_szare(h, w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)

def rysuj_ramki_kolorowe(w, kolor_ramki, a, b, c):
    return rysuj_ramke_kolor(w, w, 20, kolor_ramki, [a * 10 % 256, b * 20 % 256, c * 30 % 256])

gwiazdka_obraz = Image.open("obrazy/gwiazdka.bmp")
gwiazdka_negatyw = negatyw(gwiazdka_obraz)
gwiazdka_negatyw.show()
gwiazdka_negatyw.save("obrazy/gwiazdka_negatyw.png")

a = len("Konrad")
b = len("Zielinski")
c = -a

im_ramka_kolorowa = rysuj_ramki_kolorowe(200, [20, 120, 220], a, b, c)
im_ramka_kolorowa.show()
im_ramka_kolorowa.save("obrazy/ramka_kolorowa.png")

ramka_negatyw = negatyw(im_ramka_kolorowa)
ramka_negatyw.show()
ramka_negatyw.save("obrazy/ramka_negatyw.png")

im_skos_szary = rysuj_po_skosie_szare(100, 300, a, b)
im_skos_szary.show()
im_skos_szary.save("obrazy/skos_szary.png")

skos_negatyw = negatyw(im_skos_szary)
skos_negatyw.show()
skos_negatyw.save("obrazy/skos_negatyw.png")
