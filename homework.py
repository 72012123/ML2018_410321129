from PIL import Image
import imageio
import matplotlib.pyplot as plt
import numpy as np

k1 = Image.open("key1.png")
k2 = Image.open("key1.png")
I = Image.open("I.png")
E = Image.open("E.png")
Eprime = Image.open("Eprime.png")

Epoch = 1
w = np.random.rand(3)
width = k1.width
height = k1.height
eta =  0.00001

output = Image.new("L", (width, height), 0)
    
while Epoch < 10:
    for i in range(0, width):
        for j in range(0, height):
            a = w[0] * k1.getpixel((i, j)) + \
                w[1] * k2.getpixel((i, j)) + \
                w[2] * I.getpixel((i, j))
            e = (E.getpixel((i, j)) - a)
            w[0] = w[0] + eta * e * k1.getpixel((i, j))
            w[1] = w[1] + eta * e * k2.getpixel((i, j))
            w[2] = w[2] + eta * e * I.getpixel((i, j))
    Epoch += 1

for i in range(0, width):
    for j in range(0, height):
        output.putpixel((i, j), int(round((Eprime.getpixel((i, j)) - w[0] * k1.getpixel((i, j)) - w[1] * k2.getpixel((i, j)))/w[2])))

output.show()
output.save("Eprime-decrypted.png")