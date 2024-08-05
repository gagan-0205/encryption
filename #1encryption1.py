from PIL import Image
import numpy as np
img = Image.open('cp2077.png').convert('RGB')
img_arr = np.array(img)
key = 100
height, width, channels = img_arr.shape
enc_img_arr = np.zeros_like(img_arr)

for i in range(height):
    for j in range(width):
        for c in range(channels):
            enc_img_arr[i,j,c] = (img_arr[i,j,c] + (i+j)*key)

enc_img = Image.fromarray(enc_img_arr, mode='RGB')
enc_img.save('$1encrypted2.png')