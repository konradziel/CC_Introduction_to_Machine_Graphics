from PIL import Image, ImageFilter, ImageChops
import matplotlib.pyplot as plt
import numpy as np
from PIL.ImageChops import difference


def filtruj(obraz, kernel, scale):
    """
    Funkcja wykonująca konwolucję obrazu z podanym kernelem i skalą
    """
    return obraz.filter(ImageFilter.Kernel(size=(int(len(kernel) ** 0.5), int(len(kernel) ** 0.5)), 
                                         kernel=kernel, 
                                         scale=scale))

def create_subplot_with_comparison(fig, row, col, image1, image2, title1, title2):
    """Helper function to create subplot with comparison"""
    ax1 = fig.add_subplot(row, col, 1)
    ax1.imshow(image1)
    ax1.set_title(title1)
    ax1.axis('off')
    
    ax2 = fig.add_subplot(row, col, 2)
    ax2.imshow(ImageChops.difference(image1, image2))
    ax2.set_title(f"Różnica: {title1} vs {title2}")
    ax2.axis('off')

def main():
    # Wczytanie obrazu
    im = Image.open('baby_yoda.jpg')
    
    # 2. Filtr BLUR
    # a. Zastosowanie filtru BLUR
    blur_filter = im.filter(ImageFilter.BLUR)
    
    # b. Pobranie informacji o filtrze BLUR i zastosowanie własnej implementacji
    blur_kernel = [1/9, 1/9, 1/9,
                  1/9, 1/9, 1/9,
                  1/9, 1/9, 1/9]
    blur_custom = filtruj(im, blur_kernel, 1)
    
    # c. Utworzenie diagramu porównawczego
    fig1 = plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.imshow(im)
    plt.title('Oryginalny')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(blur_filter)
    plt.title('BLUR filter')
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(ImageChops.difference(blur_filter, blur_custom))
    plt.title('Różnica')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig1.png')
    plt.close()

    # d. Statystyki obrazu porównania
    difference_img = ImageChops.difference(blur_filter, blur_custom)
    diff_stats = difference_img.getextrema()
    print("Statystyki obrazu porównania:")
    print(f"Minimalna różnica w kanale R: {diff_stats[0][0]}")
    print(f"Maksymalna różnica w kanale R: {diff_stats[0][1]}")
    print(f"Minimalna różnica w kanale G: {diff_stats[1][0]}")
    print(f"Maksymalna różnica w kanale G: {diff_stats[1][1]}")
    print(f"Minimalna różnica w kanale B: {diff_stats[2][0]}")
    print(f"Maksymalna różnica w kanale B: {diff_stats[2][1]}")

    # 3. SOBEL i EMBOSS
    # Konwersja na tryb L
    im_L = im.convert('L')
    
    # a. Zastosowanie filtru EMBOSS
    emboss = im_L.filter(ImageFilter.EMBOSS)
    
    # b. SOBEL filters
    sobel1_kernel = [-1, 0, 1,
                     -2, 0, 2,
                     -1, 0, 1]
    sobel2_kernel = [-1, -2, -1,
                      0,  0,  0,
                      1,  2,  1]
    
    sobel1 = filtruj(im_L, sobel1_kernel, 1)
    sobel2 = filtruj(im_L, sobel2_kernel, 1)
    
    # Utworzenie diagramu
    fig2 = plt.figure(figsize=(20, 5))
    plt.subplot(141)
    plt.imshow(im_L, cmap='gray')
    plt.title('Obraz L')
    plt.axis('off')
    
    plt.subplot(142)
    plt.imshow(emboss, cmap='gray')
    plt.title('EMBOSS')
    plt.axis('off')
    
    plt.subplot(143)
    plt.imshow(sobel1, cmap='gray')
    plt.title('SOBEL1')
    plt.axis('off')

    plt.subplot(144)
    plt.imshow(sobel1, cmap='gray')
    plt.title('SOBEL2')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig2.png')
    plt.close()

    # 4. Porównanie filtrów 2,4,6,8
    filters = [
        (ImageFilter.DETAIL, "DETAIL"),
        (ImageFilter.EDGE_ENHANCE_MORE, "EDGE_ENHANCE_MORE"),
        (ImageFilter.SHARPEN, "SHARPEN"),
        (ImageFilter.SMOOTH_MORE, "SMOOTH_MORE")
    ]
    
    fig3 = plt.figure(figsize=(15, 10))
    for idx, (filter_type, name) in enumerate(filters):
        plt.subplot(4, 2, idx*2+1)
        filtered = im.filter(filter_type)
        plt.imshow(filtered)
        plt.title(name)
        plt.axis('off')
        
        plt.subplot(4, 2, idx*2+2)
        plt.imshow(ImageChops.difference(filtered, im))
        plt.title(f"Różnica: {name} vs Original")
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig3.png')
    plt.close()

    # 5. Filtry parametryczne
    filters_param = [
        (ImageFilter.GaussianBlur(radius=2), "GaussianBlur(2)"),
        (ImageFilter.UnsharpMask(radius=2, percent=150), "UnsharpMask(2,150)"),
        (ImageFilter.MedianFilter(size=3), "MedianFilter(3)"),
        (ImageFilter.MinFilter(size=3), "MinFilter(3)"),
        (ImageFilter.MaxFilter(size=3), "MaxFilter(3)")
    ]
    
    fig4 = plt.figure(figsize=(15, 12))
    for idx, (filter_type, name) in enumerate(filters_param):
        plt.subplot(5, 2, idx*2+1)
        filtered = im.filter(filter_type)
        plt.imshow(filtered)
        plt.title(name)
        plt.axis('off')
        
        plt.subplot(5, 2, idx*2+2)
        plt.imshow(ImageChops.difference(filtered, im))
        plt.title(f"Różnica: {name} vs Original")
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig4.png')
    plt.close()

if __name__ == "__main__":
    main()
