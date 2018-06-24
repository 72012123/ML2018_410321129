import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
import numpy as np

mnist = fetch_mldata('MNIST original', data_home='minst_datasets')
img = np.reshape(mnist.data[0,:], (28,28))
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()