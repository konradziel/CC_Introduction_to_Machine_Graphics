from PIL import Image
import numpy as np

def rysuj_ramke_w_obrazie(obraz, grub): # grub grubość ramki w pikselach
    obraz = np.array(obraz, dtype=np.uint8)

    obraz[:grub, :] = 0 # Górna ramka
    obraz[-grub:, :] = 0  # Dolna ramka
    obraz[:, :grub] = 0  # Lewa ramka
    obraz[:, -grub:] = 0 # Prawa ramka

    obraz = obraz.astype(bool)

    nowy_obraz = Image.fromarray(obraz)

    return nowy_obraz

obraz = Image.new('1', (300, 300), 1)
nowy_obraz = rysuj_ramke_w_obrazie(obraz, 10)
nowy_obraz.show()