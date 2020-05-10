import matplotlib.pyplot as plt


# К этим заданиям нужен код и результаты)

# Task 1. Применить 5 фильтров к своей фотке (15 баллов)
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


# Task 2. Сделать фильтры 3 x 3 и 5 x 5, ищущие кружочки, применить их (10 баллов)



# Task 3. Сделать приложение по применению фильтров (то есть с интерфейсом) (15 баллов)