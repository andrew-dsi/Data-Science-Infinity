

import numpy as np
from skimage import io
import matplotlib.pyplot as plt

camaro = io.imread("camaro.jpg")
print(camaro)

camaro.shape

plt.imshow(camaro)
plt.show()


# Cropping the image

cropped = camaro[0:500,:,:]
plt.imshow(cropped)
plt.show()

cropped = camaro[:,400:1000,:]
plt.imshow(cropped)
plt.show()

cropped = camaro[350:1100,200:1400,:]
plt.imshow(cropped)
plt.show()

io.imsave("camaro_cropped.jpg", cropped)


# Flip our image

vertical_flip = camaro[::-1,:,:]
plt.imshow(vertical_flip)
plt.show()

io.imsave("camaro_vertical_flip.jpg", vertical_flip)

horizontal_flip = camaro[:,::-1,:]
plt.imshow(horizontal_flip)
plt.show()

io.imsave("camaro_horizontal_flip.jpg", horizontal_flip)


# Colour channels

red = np.zeros(camaro.shape, dtype = "uint8")
red[:,:,0] = camaro[:,:,0]
plt.imshow(red)
plt.show()

green = np.zeros(camaro.shape, dtype = "uint8")
green[:,:,1] = camaro[:,:,1]
plt.imshow(green)
plt.show()

blue = np.zeros(camaro.shape, dtype = "uint8")
blue[:,:,2] = camaro[:,:,2]
plt.imshow(blue)
plt.show()

camaro_rainbow = np.vstack((red,green,blue))
plt.imshow(camaro_rainbow)
plt.show()

io.imsave("camaro_camaro_rainbow.jpg", camaro_rainbow)



































































