from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from PIL.ImageChops import difference

#Zad1

im = Image.open('kot.jpg').convert('RGB')

#Zad2
#a
im_r, im_g, im_b = im.split()

#b
im1 = Image.merge('RGB', (im_b, im_r, im_g))
difference = ImageChops.difference(im1, im)

#c
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(im)

plt.subplot(1, 3, 2)
plt.title('Merged Image')
plt.imshow(im1)

plt.subplot(1, 3, 3)
plt.title('Difference')
plt.imshow(difference)

plt.savefig('fig1.png')
plt.show()


#Zad3
#a
im2 = Image.merge('RGB', (im_b, im_g, im_r))
im2.save('im2.jpg')
im2.save('im2.png')

#b
im2_jpg = Image.open('im2.jpg')
im2_png = Image.open('im2.png')

difference2 = ImageChops.difference(im2_jpg, im2_png)

#c
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('im2.jpg')
plt.imshow(im2_jpg)

plt.subplot(1, 3, 2)
plt.title('im2.png')
plt.imshow(im2_png)

plt.subplot(1, 3, 3)
plt.title('Difference')
plt.imshow(difference2)

plt.savefig('fig2.png')
plt.show()


#Zad4
def recognize_transformation(original, mix):
    original_r, original_g, original_b = original.split()
    mix_r, mix_g, mix_b = mix.split()

    # Check for permutation
    if mix_r == original_r and mix_g == original_g and mix_b == original_b:
        return "No transformation"
    elif mix_r == original_g and mix_g == original_b and mix_b == original_r:
        return "Permutation: RGB -> GBR"
    elif mix_r == original_b and mix_g == original_r and mix_b == original_g:
        return "Permutation: RGB -> BRG"

    # Check for negation
    if ImageChops.invert(original_r) == mix_r:
        return "Negation of Red Channel"
    elif ImageChops.invert(original_g) == mix_g:
        return "Negation of Green Channel"
    elif ImageChops.invert(original_b) == mix_b:
        return "Negation of Blue Channel"

    return "Unknown transformation"

mix = Image.merge('RGB', (im_b, im_r, im_g))
transformation = recognize_transformation(im, mix)
print(transformation)


#Zad5
gray_array = np.random.randint(0, 256, (im.height, im.width), dtype=np.uint8)
im3 = Image.fromarray(gray_array, 'L')

im_r_gray = Image.merge('RGB', (im3, im_g, im_b))
im_g_gray = Image.merge('RGB', (im_r, im3, im_b))
im_b_gray = Image.merge('RGB', (im_r, im_g, im3))

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title('Red Replaced')
plt.imshow(im_r_gray)

plt.subplot(1, 3, 2)
plt.title('Green Replaced')
plt.imshow(im_g_gray)

plt.subplot(1, 3, 3)
plt.title('Blue Replaced')
plt.imshow(im_b_gray)

plt.savefig('fig4.png')
plt.show()

#Zad6
histogram = im.histogram()

plt.figure(figsize=(10, 5))
plt.hist(histogram, bins=256, color='black')
plt.title('Image Histogram')
plt.show()

plt.figure(figsize=(15, 5))
for i, color in enumerate(['r', 'g', 'b']):
    plt.subplot(1, 3, i+1)
    plt.hist(im.split()[i].histogram(), bins=256, color=color)
    plt.title(f'{color.upper()} Channel Histogram')

plt.show()

green_channel = im.split()[1]
pixel_count = green_channel.histogram()[1]
print(f'Pixels with value 1 in green channel: {pixel_count}')


#Zad7
#a
def are_images_identical(im1, im2):
    if im1.size != im2.size or im1.mode != im2.mode:
        return False
    diff = ImageChops.difference(im1, im2)
    return not diff.getbbox()

identical = are_images_identical(im, im1)
print(f'Images are identical: {identical}')

#b
def highlight_differences(im1, im2):
    diff = ImageChops.difference(im1, im2)
    diff = diff.convert('RGB')
    diff = Image.eval(diff, lambda x: 255 if x else 0)
    return diff

highlighted_diff = highlight_differences(im, im1)
highlighted_diff.show()


#Zad8
im = Image.open('beksinski1.png').convert('RGB')
r, g, b = im.split()