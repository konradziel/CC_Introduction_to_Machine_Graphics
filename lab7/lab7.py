from PIL import Image
import math

def rysuj_kwadrat_srednia(obraz, m, n, k): # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = k // 2
    for a in range(k):
        for b in range(k):
            temp = [0, 0, 0]  # R, G, B
            for i in range(k):
                for j in range(k):
                    x = m + i - d
                    y = n + j - d
                    if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                        p = pix[x, y]
                        temp[0] += p[0]
                        temp[1] += p[1]
                        temp[2] += p[2]
            x = m + a - d
            y = n + b - d
            if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                pix1[x, y] = (int(temp[0]/k**2), int(temp[1]/k**2), int(temp[2]/k**2))
    return obraz1

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = k // 2

    for a in range(k):
        for b in range(k):
            temp = [0, 0, 0]  # R, G, B
            for i in range(k):
                for j in range(k):
                    x = m + i - d
                    y = n + j - d
                    if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                        p = pix[x, y]
                        temp[0] = max(temp[0], p[0])
                        temp[1] = max(temp[1], p[1])
                        temp[2] = max(temp[2], p[2])
            
            x = m + a - d
            y = n + b - d
            if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = k // 2

    for a in range(k):
        for b in range(k):
            temp = [255, 255, 255]  # R, G, B
            for i in range(k):
                for j in range(k):
                    x = m + i - d
                    y = n + j - d
                    if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                        p = pix[x, y]
                        temp[0] = min(temp[0], p[0])
                        temp[1] = min(temp[1], p[1])
                        temp[2] = min(temp[2], p[2])
            
            x = m + a - d
            y = n + b - d
            if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

def rysuj_kolo(obraz, m_s, n_s, r, kolor):
    obraz1 = obraz.copy()
    pix1 = obraz1.load()
    
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            if i*i + j*j <= r*r:
                x = m_s + i
                y = n_s + j
                if 0 <= x < obraz.size[0] and 0 <= y < obraz.size[1]:
                    pix1[x, y] = kolor
    return obraz1

def rysuj_kolo_kopia(obraz, m_s, n_s, r, m_k, n_k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            if i*i + j*j <= r*r:
                x = m_s + i
                y = n_s + j
                x_source = m_k + i
                y_source = n_k + j
                
                if (0 <= x < obraz.size[0] and 0 <= y < obraz.size[1] and 
                    0 <= x_source < obraz.size[0] and 0 <= y_source < obraz.size[1]):
                    pix1[x, y] = pix[x_source, y_source]
    return obraz1

def odbij_w_pionie_v1(im):
    px0 = im.load()  # pobieramy piksele z oryginalnego obrazu
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1- i, j]  # kopiujemy z oryginalnego obrazu
    return img

def odbij_w_pionie_v2(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w-1-i, j]  # kopiujemy z tego samego obrazu
    return img

if __name__ == "__main__":
    im = Image.open('baby_yoda.jpg')
    print("tryb obrazu", im.mode)
    print("rozmiar", im.size)

    # Test obu wersji funkcji odbij_w_pionie
    obraz_v1 = odbij_w_pionie_v1(im)
    obraz_v1.save('obraz_odbicie_v1.png')
    
    obraz_v2 = odbij_w_pionie_v2(im)
    obraz_v2.save('obraz_odbicie_v2.png')

    # 1.1 Rysowanie trzech kwadratów z wartością maksymalną
    obraz1 = im.copy()
    obraz1 = rysuj_kwadrat_max(obraz1, 100, 100, 25)  # pierwszy kwadrat
    obraz1 = rysuj_kwadrat_max(obraz1, 200, 150, 35)  # drugi kwadrat
    obraz1 = rysuj_kwadrat_max(obraz1, 150, 200, 45)  # trzeci kwadrat
    obraz1.save('obraz1.png')

    # 1.2 Rysowanie trzech kwadratów z wartością minimalną
    obraz2 = im.copy()
    obraz2 = rysuj_kwadrat_min(obraz2, 100, 100, 25)  # pierwszy kwadrat
    obraz2 = rysuj_kwadrat_min(obraz2, 200, 150, 35)  # drugi kwadrat
    obraz2 = rysuj_kwadrat_min(obraz2, 150, 200, 45)  # trzeci kwadrat
    obraz2.save('obraz2.png')

    # 2. Kopiowanie fragmentu obrazu w kształcie koła
    obraz3 = rysuj_kolo_kopia(im, 48, 250, 16, 48, 172)  # kopiuje fragment z punktu (100,100) do koła o środku (200,150)
    obraz3.save('obraz3.png')

    # 2.1 Efekt wielu kół
    obraz4 = im.copy()
    import math
    num_circles = 5
    center_x, center_y = 48, 172  # środek dużego okręgu
    radius = 60  # promień dużego okręgu
    for i in range(num_circles):
        angle = 2 * math.pi * i / num_circles  # kąt dla każdego koła
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        obraz4 = rysuj_kolo_kopia(obraz4, x, y, 16, 48, 172)
    obraz4.save('obraz4.png')