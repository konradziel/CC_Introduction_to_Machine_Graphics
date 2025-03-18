from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

def histogram_norm(image):
    # Pobieramy histogram - bierzemy tylko pierwsze 256 wartości dla trybu L
    hist = image.histogram()[:256]
    # Normalizujemy przez liczbę pikseli - dzielimy każdą wartość przez (szerokość * wysokość)
    total_pixels = image.width * image.height
    hist_norm = [h / total_pixels for h in hist]
    return hist_norm

def histogram_cumul(image):
    hist_norm = histogram_norm(image)
    # Robimy histogram skumulowany - sumujemy wartości od początku
    hist_cumul = []
    cumsum = 0
    for h in hist_norm:
        cumsum += h
        hist_cumul.append(cumsum)
    return hist_cumul

def histogram_equalization(image):
    # Pobieramy histogram skumulowany
    hist_cumul = histogram_cumul(image)
    # Tworzymy nowy obraz z wyrównanym histogramem
    img_array = np.array(image)
    equalized = np.zeros_like(img_array)
    
    # Przekształcamy każdy piksel według wzoru: nowa_wartość = 255 * hist_cumul[stara_wartość]
    for i in range(image.height):
        for j in range(image.width):
            pixel_value = img_array[i, j]
            equalized[i, j] = int(255 * hist_cumul[pixel_value])
    
    return Image.fromarray(equalized)

def plot_histograms(image):
    # Rysujemy wszystkie histogramy na jednym wykresie
    plt.figure(figsize=(15, 5))
    
    # Histogram oryginalny
    plt.subplot(141)
    plt.hist(np.array(image).flatten(), bins=256, range=(0, 256), density=True)
    plt.title('Histogram Oryginalny')
    
    # Histogram znormalizowany
    plt.subplot(142)
    hist_norm = histogram_norm(image)
    plt.plot(hist_norm)
    plt.title('Histogram Znormalizowany')
    
    # Histogram skumulowany
    plt.subplot(143)
    hist_cumul = histogram_cumul(image)
    plt.plot(hist_cumul)
    plt.title('Histogram Skumulowany')
    
    # Histogram po wyrównaniu
    equalized = histogram_equalization(image)
    plt.subplot(144)
    plt.hist(np.array(equalized).flatten(), bins=256, range=(0, 256), density=True)
    plt.title('Histogram po Wyrównaniu')
    
    plt.tight_layout()
    plt.savefig('fig1.png')
    plt.close()

def plot_images_comparison(original, equalized_custom, equalized_imageops):
    # Rysujemy porównanie obrazów obok siebie
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.imshow(original, cmap='gray')
    plt.title('Obraz Oryginalny', pad=20)
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(equalized_custom, cmap='gray')
    plt.title('Wyrównanie Własne', pad=20)
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(equalized_imageops, cmap='gray')
    plt.title('Wyrównanie ImageOps', pad=20)
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig2.png', bbox_inches='tight')
    plt.close()

def konwertuj1(image, w_r, w_g, w_b):
    # Konwersja RGB -> L z użyciem round()
    img_array = np.array(image)
    r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    result = np.round(r * w_r + g * w_g + b * w_b).astype(np.uint8)
    return Image.fromarray(result)

def konwertuj2(image, w_r, w_g, w_b):
    # Konwersja RGB -> L z użyciem int() zamiast round()
    img_array = np.array(image)
    r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    result = (r * w_r + g * w_g + b * w_b).astype(np.uint8)
    return Image.fromarray(result)

def print_image_stats(image, name):
    # Wyświetlamy podstawowe statystyki obrazu
    arr = np.array(image)
    print(f"\nStatystyki dla {name}:")
    print(f"Średnia: {np.mean(arr):.2f}")
    print(f"Odchylenie std: {np.std(arr):.2f}")
    print(f"Min: {np.min(arr)}")
    print(f"Max: {np.max(arr)}")

# Główna część programu
if __name__ == "__main__":
    # Wczytujemy obraz i konwertujemy do trybu L jeśli trzeba
    img = Image.open('zeby.png')
    if img.mode != 'L':
        img = img.convert('L')
    
    # Wyrównujemy histogram własną metodą
    equalized_img = histogram_equalization(img)
    equalized_img.save('equalized.png')
    
    # Generujemy wykresy histogramów
    plot_histograms(img)
    
    # Wyświetlamy statystyki dla porównania
    print_image_stats(img, "obraz oryginalny")
    print_image_stats(equalized_img, "obraz po wyrównaniu (własna metoda)")
    
    # Wyrównujemy histogram metodą z ImageOps
    equalized_imageops = ImageOps.equalize(img)
    equalized_imageops.save('equalized1.png')
    
    # Generujemy porównanie obrazów
    plot_images_comparison(img, equalized_img, equalized_imageops)
    
    # Konwersja obrazu mgla.jpg
    mgla = Image.open('mgla.jpg')
    
    # Standardowe wagi dla konwersji PIL
    w_r, w_g, w_b = 299/1000, 587/1000, 114/1000
    
    # Konwersja różnymi metodami
    mgla_L1 = konwertuj1(mgla, w_r, w_g, w_b)
    mgla_L1.save('mgla_L1.png')
    
    mgla_L = mgla.convert('L')
    mgla_L.save('mgla_L.png')
    
    mgla_L2 = konwertuj2(mgla, w_r, w_g, w_b)
    mgla_L2.save('mgla_L2.png')
    
    # Porównanie statystyk konwersji
    print("\nPorównanie metod konwersji:")
    print_image_stats(mgla_L, "PIL convert('L')")
    print_image_stats(mgla_L1, "konwertuj1 (round)")
    print_image_stats(mgla_L2, "konwertuj2 (int)")