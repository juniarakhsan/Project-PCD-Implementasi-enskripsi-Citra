import  imageio as img 
import numpy as np 
import matplotlib.pyplot as plt

def isOne(key):
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    return (a*d) - (b*c) ==1

def encrypt(image,key):
    if(not isOne(key)):
        return "Determinan harus 1"
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    
    result = np.zeros_like(image)
    for i in range(0, image.shape[0]-1,2):
       for j in range(image.shape[1]):
           r1 = ((a*image[i,j,0])+(c*image[i+1,j,0]))%256
           r2 = ((b*image[i,j,0])+(d*image[i+1,j,0]))%256
           
           g1 = ((a*image[i,j,1])+(c*image[i+1,j,1]))%256
           g2 = ((b*image[i,j,1])+(d*image[i+1,j,1]))%256
           
           b1 = ((a*image[i,j,2])+(c*image[i+1,j,2]))%256
           b2 = ((b*image[i,j,2])+(d*image[i+1,j,2]))%256
           
           result[i,j,0] = r1
           result[i+1,j,0] = r2
           
           result[i,j,1] = g1
           result[i+1,j,1] = g2
           
           result[i,j,2] = b1
           result[i+1,j,2] = b2
           
    return result


def decrypt(image,key):
    if(not isOne(key)):
        return "Determinan harus 1"
    d = key[0][0]
    b = 256-key[0][1]
    c = 256-key[1][0]
    a = key[1][1]
    result = np.zeros_like(image)
    for i in range(0, image.shape[0]-1,2):
       for j in range(image.shape[1]):
           r1 = ((a*image[i,j,0])+(c*image[i+1,j,0]))%256
           r2 = ((b*image[i,j,0])+(d*image[i+1,j,0]))%256
           
           g1 = ((a*image[i,j,1])+(c*image[i+1,j,1]))%256
           g2 = ((b*image[i,j,1])+(d*image[i+1,j,1]))%256
           
           b1 = ((a*image[i,j,2])+(c*image[i+1,j,2]))%256
           b2 = ((b*image[i,j,2])+(d*image[i+1,j,2]))%256
           
           result[i,j,0] = r1
           result[i+1,j,0] = r2
           
           result[i,j,1] = g1
           result[i+1,j,1] = g2
           
           result[i,j,2] = b1
           result[i+1,j,2] = b2
           
    return result

image = img.imread("D:\PCD Implementasi Enskripsi Citra/234291.jpeg")
key = np.array([
    [4,3],
    [9,7]
    
])

imgEnc = encrypt(image,key)
imgDec = decrypt(imgEnc, key)



plt.figure(figsize=(10,10))
plt.subplot(1,3,1)
plt.imshow(image)

plt.subplot(1,3,2)
plt.imshow(imgEnc)

plt.subplot(1,3,3)
plt.imshow(imgDec)
plt.show()