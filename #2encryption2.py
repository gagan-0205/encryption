from PIL import Image
import numpy as np

# Load the image and convert to NumPy array
img = Image.open('$1encrypted1.png').convert('RGB')
img_arr = np.array(img)

# Set the encryption key and image dimensions
key = 100
height, width, channels = img_arr.shape

# Initialize encrypted image array
enc_img_arr = np.zeros_like(img_arr)

# Encrypt the image using zigzag method
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
                enc_img_arr[i,j,c] = (img_arr[y,x,c] + (y+x)*key) % 256
            else:
                enc_img_arr[i,j,c] = (img_arr[y,x,c] + ((width-1-x)+y)*key) % 256

# Save the encrypted image
enc_img = Image.fromarray(enc_img_arr, mode='RGB')
enc_img.save('$2encrypted1to2.png')
