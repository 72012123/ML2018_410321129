from PIL import Image
import numpy as np

k1 = Image.open("key1.png").convert('RGB')
k2 = Image.open("key1.png").convert('RGB')
i = Image.open("I.png").convert('RGB')
E = Image.open("E.png").convert('RGB')
Eprime = Image.open("Eprime.png").convert('RGB')

Epoch = 1
w = np.array([[10, 10, 10]])
width = k1.width
height = k1.height
eta = 1e-8

output = Image.new("L", (width, height), 0)
    
while Epoch < 10:
    for i in range(0, width):
        for j in range(0, height):
            a = w[i*width][0]*k1.getpixel((i, j)) + w[i*width][1]*k2.getpixel((i, j)) + w[i*width][2]*i.getpixel((i, j))
            e = E.getpixel((i, j)) - a
            w.append(w[i*width][0]+eta*e*k1.getpixel((i, j)), w[i*width][1]+eta*e*k2.getpixel((i, j)), w[i*width][2]+eta*e*i.getpixel((i, j)))
    Epoch += 1
