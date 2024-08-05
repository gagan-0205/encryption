from PIL import Image
import numpy as np
enc_img = Image.open('$3almost_there.png').convert('RGB')
enc_img_arr = np.array(enc_img)
key = 100
height, width, channels = enc_img_arr.shape
dec_img_arr = np.zeros_like(enc_img_arr)

for i in range(height):
    for j in range(width):
        for c in range(channels):
            dec_img_arr[i,j,c] = (enc_img_arr[i,j,c] - (i+j)*key)
dec_img = Image.fromarray(dec_img_arr, mode='RGB')
dec_img.save('$4decrypted_finally.png')