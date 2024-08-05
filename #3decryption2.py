from PIL import Image
import numpy as np

# Load the encrypted image and convert to NumPy array
enc_img = Image.open('$2encrypted1to2.png').convert('RGB')
enc_img_arr = np.array(enc_img)

# Set the decryption key and image dimensions
key = 100
height, width, channels = enc_img_arr.shape

# Initialize decrypted image array
dec_img_arr = np.zeros_like(enc_img_arr)

# Decrypt the image using zigzag method
for i in range(height):
    for j in range(width):
        if i % 2 == 0: # Even row
            x = j
            y = i
        else: # Odd row
            x = width - 1 - j
            y = i
        for c in range(channels):
            if i % 2 == 0:
                dec_img_arr[y,x,c] = (enc_img_arr[i,j,c] - (y+x)*key) % 256
            else:
                dec_img_arr[y,x,c] = (enc_img_arr[i,j,c] - ((width-1-x)+y)*key) % 256

# Save the decrypted image
dec_img = Image.fromarray(dec_img_arr, mode='RGB')
dec_img.save('$3almost_there.png')