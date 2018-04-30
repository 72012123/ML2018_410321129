from PIL import Image
import numpy as np

k1 = Image.open("key1.png")
k2 = Image.open("key1.png")
i = Image.open("I.png")
E = Image.open("E.png")
Eprime = Image.open("Eprime.png")

Epoch = 1
w = np.array([[10, 10, 10]])
width = k1.width
height = k1.height
eta = 1e-8
error = [convergence()]

def convergence(self)
    

while Epoch < 10 and :
    for i in range(0, width):
        for j in range(0, height):
            a[i][j] = w[0]*k1.getpixel((i, j)) + w[1]*k2.getpixel((i, j)) + w[2]*i.getpixel((i, j))
            e[i][j] = E.getpixel((i, j)) - a[i][j]
            w[0] += eta*e[i][j]*k1.getpixel((i, j))
            w[1] += eta*e[i][j]*k2.getpixel((i, j))
            w[2] += eta*e[i][j]*E.getpixel((i, j))
    Epoch += 1

    

