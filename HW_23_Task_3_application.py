import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import argparse


# Task 3. Сделать приложение по применению фильтров (то есть с интерфейсом) (15 баллов)

# Argparse part
parser = argparse.ArgumentParser(prog='filter_app', description='app help to improve your photo')
parser.add_argument('img', type=str, metavar='path_to_photo', help='file with your photo')
parser.add_argument('kernel', type=np.array, metavar='matrix', help='matrix that is a filter')

args = parser.parse_args()
args = args.__dict__
# print(args)

def convolve(img, kernel):
    """
    Make convolution of img with kernel, assuming stride is equal to 1
    :param img: path to file with photo
    :param kernel: 2d n x n np.array
    :return: filtered photo
    """
    img = Image.open(img)
    data = np.array(img)[:, :, 0:3]
    n = kernel.shape[0]
    kernel = kernel.reshape((n, n, 1))

    # Assuming kernel is n x n and stride equals to 1
    modified = np.zeros_like(data)
    for row in range(n//2, data.shape[0] - (n-1)):
        for col in range(n//2, data.shape[1] - (n-1)):
            modified[row, col] = (data[row:row + n, col:col + n] * kernel).sum()
    return modified

modified = convolve(args['img'], args['kernel'])
plt.imshow(modified, cmap='gray')
plt.axis('off')
plt.show()
plt.savefig(f'new_{img}.png')