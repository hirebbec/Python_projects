import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw 
import matplotlib.animation as animation
import random

def curvature(phi, phasa):
    counter = 0
    curv = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            if (phi[i][j] == phasa).all():
                for x in range ((i-b), (i+b+1)):
                    for y in range((j-b), (j+b+1)):
                        if x < n and y < (m-b):
                            if (phi[x][y] == 0).all():
                                counter += 1
                        if x >= n and y < (m-b):
                            x = x-n
                            if (phi[x][y] == 0).all():
                                counter += 1
                        if y >= (m-b) and x < n:
                            y = y-m
                            if (phi[x][y] == 0).all():
                                counter += 1
                        if x >= n and y >= (m-b):
                            x = x-n
                            y = y-m
                            if (phi[x][y] == 0).all():
                                counter += 1
            curv[i][j] = counter
            counter = 0
    return curv

def cycle(phi):
    print(phi)
    
    curvsol = curvature(phi, 255)

    max_list = []
    maximum = max(map(max, curvsol))

    for i in range(n):
        for j in range(m):
            if curvsol[i][j] == maximum:
                max_i = i
                max_j = j
                max_list.append([max_i,max_j])
    max_random_str = random.choice(max_list)
    max_i = max_random_str[0]
    max_j = max_random_str[1]
    phi[max_i][max_j] = 0
    print(phi)
    print()

    curvfl = curvature(phi, 0)

    min_list = []
    
    for i in range(n):
        for j in range(m):
            if curvfl[i][j] == 0:
                curvfl[i][j] = b**2

    minimum = min(map(min, curvfl))

    for i in range(n):
        for j in range(m):
            if curvfl[i][j] == minimum:
                min_i = i
                min_j = j
                min_list.append([min_i,min_j])
    min_random_str = random.choice(min_list)
    min_i = min_random_str[0]
    min_j = min_random_str[1]
    phi[min_i][min_j] = 255

    return phi

image = Image.open("kotenok.jpg")

draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

im = Image.new('RGBA', (width, height), (0, 255, 0, 0))
draw1 = ImageDraw.Draw(im) 

factor = int(100)
for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = a + b + c
		if (S > (((255 + factor) // 2) * 3)):
			a, b, c = 255, 255, 255
		else:
			a, b, c = 0, 0, 0
		draw1.point((i, j), (a, b, c))
im.show()
im.save("newkotenok.png")

arr = np.array(Image.open("newkotenok.png"))
n = arr.shape[0]
m = arr.shape[1]
l = arr.shape[2]

phi = np.zeros((n, m), dtype=int)
			
for i in range(n):
	for j in range(m):
		for k in range(l):
			phi[i][j] = arr[i][j][0]

b = 5
b = int((b-1)/2)

curvfl = np.zeros((n, m), dtype=int)
curvsol = np.zeros((n, m), dtype=int)

fig = plt.figure()
ax = fig.add_subplot(111)
tx = ax.set_title('0 cycle')
im = ax.imshow(phi) 

def anim(i):
    result = cycle(phi)
    im = ax.imshow(result)
    tx.set_text('{0} cycle'.format(i+1))
    
ani = animation.FuncAnimation(fig, anim, repeat = True, interval = 100)

plt.show()

