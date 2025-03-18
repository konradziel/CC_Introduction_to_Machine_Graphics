from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    img_copy = obraz.copy()
    width, height = inicjaly.size
    
    for i in range(width):
        for j in range(height):
            if inicjaly.getpixel((i, j)) == 0:
                img_copy.putpixel((m + i, n + j), kolor)
    
    return img_copy

def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
    img_copy = obraz.copy()
    width, height = inicjaly.size
    
    for i in range(width):
        for j in range(height):
            if inicjaly.getpixel((i, j)) == 0:
                pixel = img_copy.getpixel((m + i, n + j))
                if isinstance(pixel, int):
                    img_copy.putpixel((m + i, n + j), 255 - pixel)
                else:
                    img_copy.putpixel((m + i, n + j), tuple(255 - x for x in pixel))
    
    return img_copy

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    img_copy = obraz.copy()
    width, height = inicjaly.size
    pix = img_copy.load()
    init_pix = inicjaly.load()
    
    for i in range(width):
        for j in range(height):
            if init_pix[i, j] == 0:  # czarny piksel w inicjałach
                pix[m + i, n + j] = kolor
    
    return img_copy

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):
    img_copy = obraz.copy()
    width, height = inicjaly.size
    pix = img_copy.load()
    init_pix = inicjaly.load()
    
    for i in range(width):
        for j in range(height):
            if init_pix[i, j] == 0:
                pixel = pix[m + i, n + j]
                if isinstance(pixel, int):
                    pix[m + i, n + j] = 255 - pixel
                else:
                    pix[m + i, n + j] = tuple(255 - x for x in pixel)
    
    return img_copy

def kontrast(obraz, wsp_kontrastu):
    img_copy = obraz.copy()
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return img_copy.point(lambda i: 128 + (i - 128) * mn)

def transformacja_logarytmiczna(obraz):
    img_copy = obraz.copy()
    return img_copy.point(lambda i: 255 * np.log(1 + i / 255))

def transformacja_gamma(obraz, gamma):
    img_copy = obraz.copy()
    return img_copy.point(lambda i: (i / 255) ** (1 / gamma) * 255)

def zadanie5_porownanie_metod(obraz):
    # Metoda 1 - nieprawidłowa (z użyciem uint8)
    T = np.array(obraz, dtype='uint8')
    T += 100
    obraz_nieprawidlowy = Image.fromarray(T, "RGB")
    
    # Metoda 2 - point
    obraz_point = obraz.point(lambda i: i + 100)
    
    # Porównanie wyników
    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.imshow(obraz)
    plt.title("Oryginalny")
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(obraz_nieprawidlowy)
    plt.title("Metoda z uint8\n(nieprawidłowa)")
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(obraz_point)
    plt.title("Metoda point\n(prawidłowa)")
    plt.axis('off')
    
    plt.savefig("fig5_porownanie.png")
    plt.close()
    
    return obraz_nieprawidlowy, obraz_point

def dodaj_wartosc_jak_point(obraz, wartosc):
    T = np.array(obraz, dtype='float64')
    T += wartosc
    T = np.clip(T, 0, 255)
    return Image.fromarray(T.astype('uint8'), "RGB")

def main():
    # Zadanie 1
    obraz = Image.open("baby_yoda.jpg")
    inicjaly = Image.open("inicjaly.jpg").convert('L')
    
    # Zadanie 2a
    img_width, img_height = obraz.size
    init_width, init_height = inicjaly.size
    obraz1 = wstaw_inicjaly(obraz, inicjaly, 
                           img_width - init_width, 
                           img_height - init_height, 
                           (255, 0, 0))  #czerwony kolor
    obraz1.save("obraz1.png")
    
    # Zadanie 2b
    obraz2 = wstaw_inicjaly_maska(obraz, inicjaly,
                                 (img_width - init_width) // 2,
                                 (img_height - init_height) // 2)
    obraz2.save("obraz2.png")
    
    # Zadanie 3 - porównanie metod
    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.imshow(obraz)
    plt.title("Oryginalny")
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(obraz1)
    plt.title("getpixel/putpixel")
    plt.axis('off')
    
    plt.subplot(133)
    obraz3 = wstaw_inicjaly_load(obraz, inicjaly,
                                img_width - init_width,
                                img_height - init_height,
                                (255, 0, 0))
    plt.imshow(obraz3)
    plt.title("load")
    plt.axis('off')
    plt.savefig("fig1.png")
    plt.close()
    
    # Zadanie 4a - kontrast
    plt.figure(figsize=(15, 5))
    plt.subplot(141)
    plt.imshow(obraz)
    plt.title("Oryginalny")
    plt.axis('off')
    
    for i, wsp in enumerate([20, 50, 80]):
        plt.subplot(142 + i)
        plt.imshow(kontrast(obraz, wsp))
        plt.title(f"Kontrast {wsp}")
        plt.axis('off')
    plt.savefig("fig2.png")
    plt.close()
    
    # Zadanie 4b - transformacja logarytmiczna
    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.imshow(obraz)
    plt.title("Oryginalny")
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(transformacja_logarytmiczna(obraz))
    plt.title("Logarytmiczna")
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(obraz.point(lambda i: i * 2 + 100))
    plt.title("Liniowa (a=2, b=100)")
    plt.axis('off')
    plt.savefig("fig3.png")
    plt.close()
    
    # Zadanie 4c - transformacja gamma
    plt.figure(figsize=(15, 5))
    plt.subplot(141)
    plt.imshow(obraz)
    plt.title("Oryginalny")
    plt.axis('off')
    
    for i, gamma in enumerate([0.5, 1.0, 2.0]):
        plt.subplot(142 + i)
        plt.imshow(transformacja_gamma(obraz, gamma))
        plt.title(f"Gamma {gamma}")
        plt.axis('off')
    plt.savefig("fig4.png")
    plt.close()

    # Zadanie 5 - porównanie metod dodawania wartości
    obraz_zly, obraz_dobry = zadanie5_porownanie_metod(obraz)
    obraz_nasza_funkcja = dodaj_wartosc_jak_point(obraz, 100)
    
    # Porównanie wyników naszej funkcji z point
    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.imshow(obraz)
    plt.title("Oryginalny")
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(obraz_dobry)
    plt.title("Metoda point")
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(obraz_nasza_funkcja)
    plt.title("Nasza implementacja")
    plt.axis('off')
    
    plt.savefig("fig5_implementacja.png")
    plt.close()

if __name__ == "__main__":
    main()
