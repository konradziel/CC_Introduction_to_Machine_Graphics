from PIL import Image
import numpy as np


def koloruj_w_paski(obraz, grub, kolory):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8) * 255

    ile_kolorow = len(kolory)
    for i in range(h):
        kolor_index = (i // grub) % ile_kolorow
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolory[kolor_index]

    return Image.fromarray(tab)


kolory_paskow = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0]
]

inicjaly_obraz = Image.open("obrazy/inicjaly_lab1.bmp").convert('1')

kolorowy_obraz = koloruj_w_paski(inicjaly_obraz, 10, kolory_paskow)

kolorowy_obraz.save("obrazy/inicjaly_paski.jpg")
kolorowy_obraz.save("obrazy/inicjaly_paski.png")