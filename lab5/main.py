from PIL import Image, ImageChops
import matplotlib.pyplot as plt


def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):

    if isinstance(obraz_bazowy, str):
        base_image = Image.open(obraz_bazowy).convert("RGB")
    else:
        base_image = obraz_bazowy.convert("RGB")

    initials_image = Image.open(obraz_wstawiany).convert("1")

    base_width, base_height = base_image.size
    initials_width, initials_height = initials_image.size

    new_image = base_image.copy()

    initials_cropped = initials_image.crop(
        (0, 0, min(initials_width, base_width - n), min(initials_height, base_height - m)))

    # Insert initials onto the base image
    for i in range(initials_cropped.size[1]):
        for j in range(initials_cropped.size[0]):
            if initials_cropped.getpixel((j, i)) == 0:
                new_image.putpixel((n + j, m + i), tuple(kolor))

    return new_image




def odkoduj(obraz1, obraz2):
    img1 = Image.open(obraz1).convert("L")
    img2 = Image.open(obraz2).convert("L")

    difference_image = Image.new("L", img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            if img1.getpixel((x, y)) != img2.getpixel((x, y)):
                difference_image.putpixel((x, y), 255)
            else:
                difference_image.putpixel((x, y), 0)

    return difference_image



#Exercise 1
base_image_path = "beksinski.png"
initials_image_path = "inicjaly.jpg"

base_image = Image.open(base_image_path)
base_width, base_height = base_image.size

image_with_initials = wstaw_inicjaly(base_image_path, initials_image_path, 0, base_width - 40,
                                     [255, 0, 0])  # Red top-right
image_with_initials = wstaw_inicjaly(image_with_initials, initials_image_path, base_height -30, 0,
                                     [0, 255, 0])  # Green bottom-left
image_with_initials = wstaw_inicjaly(image_with_initials, initials_image_path, base_height // 2, 0,
                                     [0, 0, 255])  # Blue middle

image_with_initials.save("obraz_inicjaly.png")

#Exercise 2
original_image = Image.open("beksinski.png")
original_image.save("obraz1.jpg")

for i in range(2, 6):
    img = Image.open(f"obraz{i - 1}.jpg")
    img.save(f"obraz{i}.jpg")

image5 = Image.open("obraz5.jpg")
difference = ImageChops.difference(original_image, image5)

plt.figure(figsize=(12, 8))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(original_image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Image 5")
plt.imshow(image5)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Difference")
plt.imshow(difference)
plt.axis('off')

plt.show()

image4 = Image.open("obraz4.jpg")
difference_4_5 = ImageChops.difference(image4, image5)

plt.figure()
plt.title("Difference between obraz4 and obraz5")
plt.imshow(difference_4_5)
plt.axis('off')
plt.show()

#Exercise 3
decoded_image = odkoduj("jesien.jpg", "zakodowany1.bmp")
decoded_image.save("kod.bmp")

decoded_image2 = odkoduj("jesien.jpg", "zakodowany2.bmp")
decoded_image2.save("kod2.bmp")
