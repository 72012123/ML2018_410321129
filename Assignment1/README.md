# Assignment 1
Image Decryption by Single-Layer Neual Network

加密公式:

![image](https://github.com/72012123/ML2018_410321129/blob/master/Assignment1/image/%E5%85%AC%E5%BC%8F.JPG?raw=true)

解密公式:

![image](https://github.com/72012123/ML2018_410321129/blob/master/Assignment1/image/%E8%A7%A3%E5%AF%86.JPG?raw=true)

1.使用imageio讀圖並轉成陣列

2.使用Adaptive Least Mean Square Error Method by Gradient Descent演算法算出 w1, w2, w3的值

3.在使用取得的w1, w2, w3的值解密取得圖片

# Gradient Descent

針對隨機化的w1, w2, w3使用下列的演算法訓練

![image](https://github.com/72012123/ML2018_410321129/blob/master/Assignment1/image/%E8%99%9B%E6%93%AC%E7%A2%BC.JPG?raw=true)

解密前:

![image](https://github.com/72012123/ML2018_410321129/blob/master/Assignment1/image/Eprime.png?raw=true)

解密後:

![image](https://github.com/72012123/ML2018_410321129/blob/master/Assignment1/image/Eprime-decrypted.png?raw=true)

# W的值

w1 = 0.24914330709723681

w2 = 0.66138190104153194

w3 = 0.08923952571665969

# 結果討論

learning rate = 0.00001，而再跑程式的時候發現訓練一回就能解密出清晰的圖片了，原本是使用PIL的getpixel做運算，可是發現跑出來的結果仍然是模糊的圖片，不過換成imageio就跑出清晰的圖片了
