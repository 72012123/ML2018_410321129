from PIL import Image
import imageio
import matplotlib.pyplot as plt
import numpy as np

k1 = imageio.imread('key1.png')
k2 = imageio.imread('key2.png')
I = imageio.imread('I.png')
E = imageio.imread('E.png')
Eprime = imageio.imread('Eprime.png')

Epoch = 1
w = np.random.rand(3)

eta =  0.00001
    
while Epoch < 2:
    for i in range(0, 300):
        for j in range(0, 400):
            a = w[0] * k1[i][j] + w[1] * k2[i][j] + w[2] * I[i][j]
            e = (E[i][j] - a)
            w[0] = w[0] + eta * e * k1[i][j]
            w[1] = w[1] + eta * e * k2[i][j]
            w[2] = w[2] + eta * e * I[i][j]
    Epoch += 1

decrypted = (Eprime-(w[0]*k1)-(w[1]*k2))/w[2]
print(w[0],w[1],w[2])
plt.imshow(decrypted,plt.cm.gray)
plt.savefig('Eprime-decrypted.png')
plt.show()
