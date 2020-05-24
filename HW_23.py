import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# К этим заданиям нужен код и результаты)

# Task 0. Наделала кучу грибных фоток и выложила в соответствующей папке на гите
me = plt.imread('KateY.png')
me.shape
ya = me[:, :, :-1]
ya.shape

plt.imshow(ya)
plt.axis('off')
plt.show()


ya[:, :, [0,1]] = 0
plt.imshow(ya)
plt.axis('off')
plt.show()
plt.savefig('blue_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
ya[:, :, [0,2]] = 0
plt.imshow(ya)
plt.axis('off')
plt.show()
plt.savefig('green_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
ya[:, :, [1,2]] = 0
plt.imshow(ya)
plt.axis('off')
plt.show()
plt.savefig('red_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('gray_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='inferno')
plt.axis('off')
plt.show()
plt.savefig('inferno_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='terrain')
plt.axis('off')
plt.show()
plt.savefig('terrain_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='flag')
plt.axis('off')
plt.show()
plt.savefig('flag_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='prism')
plt.axis('off')
plt.show()
plt.savefig('prism_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='gist_earth')
plt.axis('off')
plt.show()
plt.savefig('gist_earth_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='gnuplot')
plt.axis('off')
plt.show()
plt.savefig('gnuplot_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='cubehelix')
plt.axis('off')
plt.show()
plt.savefig('cubehelix_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='gist_ncar')
plt.axis('off')
plt.show()
plt.savefig('gist_ncar_me.png')

ya = plt.imread('KateY.png')[:, :, :-1]
plt.imshow(ya.mean(2), cmap='rainbow')
plt.axis('off')
plt.show()
plt.savefig('rainbow_me.png')


# Task 1. Применить 5 фильтров к своей фотке (15 баллов)
img = Image.open('Kate_start.PNG') #.convert('L')
data = np.array(img)[:, :, :-1]
img.show()

# plt.imshow(data)
# plt.axis('off')
# plt.show()

def convolve(img, kernel):
    """
    Make primitive convolution of img with kernel, assuming
    stride is equal to 1
    :param img: 2d np.array
    :param kernel: 2d 3 x 3 np.array
    :return:
    """
    # Assuming kernel is 3 x 3 and stride equals to 1
    modified = np.zeros_like(img)
    for row in range(1, img.shape[0] - 2):
        for col in range(1, img.shape[1] - 2):
            modified[row, col] = (img[row:row + 3, col:col + 3] * kernel).sum()
    return modified

# 1
kernel = np.array([ [-1, 1, -1],
                    [0, 1, 0],
                    [-1, 1, -1]])
modified = convolve(data, kernel)
plt.imshow(modified)#, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_1.png')

# 2
kernel = np.array([ [-1, 0, 1],
                    [0, 1, 0],
                    [1, 0, -1]])
modified = convolve(data, kernel)
plt.imshow(modified)#, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_2.png')

# 3
kernel = np.array([ [0, -1/2, 0],
                    [1/2, 1/2, 1/2],
                    [0, -1/2, 0]])
modified = convolve(data, kernel)
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_3.png')

# 4
kernel = np.array([ [0, -1/2, 0],
                    [0, 0, 0],
                    [0, -1/2, 0]])
modified = convolve(data, kernel)
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_4.png')

# for 5x5
def convolve_five(img, kernel):
    """
    Make primitive convolution of img with kernel, assuming
    stride is equal to 1
    :param img: 2d np.array
    :param kernel: 2d 5 x 5 np.array
    :return:
    """
    # Assuming kernel is 5 x 5 and stride equals to 1
    modified = np.zeros_like(img)
    for row in range(2, img.shape[0] - 4):
        for col in range(2, img.shape[1] - 4):
            modified[row, col] = (img[row:row + 5, col:col + 5] * kernel).mean()
    return modified


# 5
kernel = np.array([ [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 1],
                    [-1, 0, 0, 0, 1],
                    [-1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1]])
kernel = kernel.reshape((5, 5, 1))
modified = convolve_five(data, kernel)
plt.imshow(modified)#, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_5.png')

def convolve_mean(img, kernel):
    """
    Make primitive convolution of img with kernel, assuming
    stride is equal to 1
    :param img: 2d np.array
    :param kernel: 2d 3 x 3 np.array
    :return:
    """
    # Assuming kernel is 3 x 3 and stride equals to 1
    modified = np.zeros_like(img)
    for row in range(1, img.shape[0] - 2):
        for col in range(1, img.shape[1] - 2):
            modified[row, col] = (img[row:row + 3, col:col + 3] * kernel).mean()
    return modified

# 6
kernel = np.array([ [-1, 0, 1/2],
                    [0, -1, 0],
                    [1/2, 0, -1]])
modified = convolve_mean(data, kernel)
plt.imshow(modified)#, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_6.png')

# 7
kernel = np.array([ [1, 1, -1/2],
                    [0, 0, 0],
                    [-1/2, 1, 1]])
modified = convolve_mean(data, kernel)
plt.imshow(modified)#, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_7.png')

# 8
kernel = np.array([ [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, 0, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1]])
kernel = kernel.reshape((5, 5, 1))
modified = convolve_five(data, kernel)
plt.imshow(modified, cmap='plasma')
plt.axis('off')
plt.show()
plt.savefig('Task_1_kernel_8.png')

# Task 2. Сделать фильтры 3 x 3 и 5 x 5, ищущие кружочки, применить их (10 баллов)
rings = Image.open('rings.PNG')
rings.show()
data = np.array(rings)[:, :, :-1]
data

#3x3
kernel_ring = np.array([ [0, -1, 0],
                    [-1, 10, -1],
                    [0, -1, 0]])
modified = convolve(data, kernel_ring)
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_2_rings_1.png')

#5x5
kernel_ring2 = np.array([[-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, 26, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1]])
kernel_ring2 = kernel_ring2.reshape((5, 5, 1))
modified = convolve_five(data, kernel_ring2)
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_2_rings_2.png')


#5x5
kernel_ring2 = np.array([[-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, 0, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1]])
kernel_ring2 = kernel_ring2.reshape((5, 5, 1))
modified = convolve_five(data, kernel_ring2)
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_2_rings_3.png')

#5x5
kernel_ring3 = np.array([[0, 0, -1, 0, 0],
                        [0, -1, -1, -1, 0],
                       [-1, -1, 11, -1, -1],
                        [0, -1, -1, -1, 0],
                        [0, 0, -1, 0, 0]])
kernel_ring3 = kernel_ring3.reshape((5, 5, 1))
modified = convolve_five(data, kernel_ring2)
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('Task_2_rings_4.png')