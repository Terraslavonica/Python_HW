import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import argparse
import os


# Task 3. Сделать приложение по применению фильтров (то есть с интерфейсом) (15 баллов)
# kernels
line3_1 = np.array([ [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0]])
line3_2 = np.array([ [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
line5_1 = np.array([[1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1]])
line5_2 = np.array([[1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1]])
ring3 = np.array([ [0, -1, 0],
                    [-1, 2, -1],
                    [0, -1, 0]])
ring5 = np.array([[0, 0, -1, 0, 0],
                 [0, -1, -1, -1, 0],
                 [-1, -1, 11, -1, -1],
                 [0, -1, -1, -1, 0],
                 [0, 0, -1, 0, 0]])
filters = {'line3_1' : line3_1, 'line3_2' : line3_2, 'line5_1' : line5_1, 'line5_2' : line5_2, 'ring3' : ring3, 'ring5' : ring5}

# Argparse part
parser = argparse.ArgumentParser(prog='filter_app', description='app help to improve your photo')
parser.add_argument('img', type=str, metavar='photo_file_name', help='name of the file with your photo')
parser.add_argument('-p', '--path', default = '', type=str, metavar='path_to_photo', help='path to the directory with your photo')
parser.add_argument('-k', '--kernel', default = 'line3_1', type=str, metavar='matrix',
                    help='matrix that is a filter: '
                         'line3_1 (default) - 3x3, search the vertical lines, '
                         'line3_2 - 3x3, search the lines like \, '
                         'line5_1 - 5x5, search the vertical lines, '
                         'line5_2 - 5x5, search the lines like \, '
                         'ring3 - 3x3, search the circles, '
                         'ring5 - 5x5, search the circles')

args = parser.parse_args()
args = args.__dict__
# print(args)

def convolve(img, path, kernel):
    """
    Make convolution of img with kernel, assuming stride is equal to 1
    :param img: path to file with photo
    :param kernel: 2d n x n np.array
    :return: filtered photo
    """
    img = os.path.join(path, img)
    kernel = filters[kernel]
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

modified = convolve(args['img'], args['path'], args['kernel'])
plt.imshow(modified, cmap='gray')
plt.axis('off')
new_name = 'new_' + args["img"]
new_img = os.path.join(args['path'], new_name)
plt.savefig(new_img)
print(f'новое фото сохранено в файл {new_img}')
