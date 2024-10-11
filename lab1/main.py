from PIL import Image
import numpy as np

photo = Image.open("photoMONO.bmp")
print("-------------- photo information")
print("mode:", photo.mode)
print("format:", photo.format)
print("size", photo.size)

photo.show()

array_photo = np.asarray(photo)
print("------------ photo array information ------------")
print("Array data type:", array_photo.dtype)
print("Array shape:", array_photo.shape)
print("Array size:", array_photo.size)
print("Array dimension:", array_photo.ndim)
print("Array item size:", array_photo.itemsize)
print("First element:", array_photo[0][0])
print("Second element:", array_photo[1][0])
print("*******************************")
print(array_photo)

int_photo = array_photo.astype(np.uint8)
print(int_photo)

t1_text = open('t1.txt', 'w')
for rows in int_photo:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')

t1_text.close()


