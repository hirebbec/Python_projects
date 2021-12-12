import matplotlib.pyplot as plt
from random import randint
import numpy as np
import matplotlib.animation as animation
from numpy.core.fromnumeric import repeat

#живая клетка - 1, мертвая - 0

fig = plt.figure()
n = 7 ## размер клеточного автомата

def matrix(A):
    prevA = A
    for i in range(n): 
        for j in range(n):
            if prevA[i][j] == 0: #определяем число единичных соседей если клетка равна 0
                t = 0
                if j == (n-1) and i != (n-1):
                    if prevA[i-1][0] == 1:
                        t += 1
                    if prevA[i][0] == 1:
                        t += 1
                    if prevA[i+1][0] == 1:
                        t += 1
                if j != (n-1) and i != (n-1):
                    if prevA[i-1][j+1] == 1:
                        t += 1
                    if prevA[i][j+1] == 1:
                        t += 1
                    if prevA[i+1][j+1] == 1:
                        t += 1
                    if prevA[i+1][j-1] == 1:
                        t += 1
                    if prevA[i+1][j] == 1:
                        t += 1
                if i == (n-1) and j != (n-1):
                    if prevA[0][j-1] == 1:
                        t += 1
                    if prevA[0][j] == 1:
                        t += 1
                    if prevA[0][j+1] == 1:
                        t += 1
                if i == (n-1) and j == (n-1):
                    if prevA[0][j-1] == 1:
                        t += 1
                    if prevA[0][j] == 1:
                        t += 1
                    if prevA[0][0] == 1:
                        t += 1
                    if prevA[i][0] == 1:
                        t += 1
                    if prevA[i-1][0] == 1:
                        t += 1
                if prevA[i-1][j-1] == 1:
                    t += 1
                if prevA[i-1][j] == 1:
                    t += 1
                if prevA[i][j-1] == 1:
                    t += 1
                
                if t == 3: #клетка становится живой если имеет 3 живых соседей
                    A[i][j] = 1
                else: #клетка остается мертвой 
                    A[i][j] = 0
        
            
            if prevA[i][j] == 1: #определяем число живых соседей для живой клетки
                t = 0
                if j == (n-1) and i != (n-1):
                    if prevA[i-1][0] == 1:
                        t += 1
                    if prevA[i][0] == 1:
                        t += 1
                    if prevA[i+1][0] == 1:
                        t += 1
                if j != (n-1) and i != (n-1):
                    if prevA[i-1][j+1] == 1:
                        t += 1
                    if prevA[i][j+1] == 1:
                        t += 1
                    if prevA[i+1][j+1] == 1:
                        t += 1
                if i == (n-1) and j != (n-1):
                    if prevA[0][j-1] == 1:
                        t += 1
                    if prevA[0][j] == 1:
                        t += 1
                    if prevA[0][j+1] == 1:
                        t += 1
                if i != (n-1) and j != (n-1):
                    if prevA[i+1][j-1] == 1:
                        t += 1
                    if prevA[i+1][j] == 1:
                        t += 1
                if i == (n-1) and j == (n-1):
                    if prevA[0][j-1] == 1:
                        t += 1
                    if prevA[0][j] == 1:
                        t += 1
                    if prevA[0][0] == 1:
                        t += 1
                    if prevA[i][0] == 1:
                        t += 1
                    if prevA[i-1][0] == 1:
                        t += 1
                if prevA[i-1][j-1] == 1:
                    t += 1
                if prevA[i-1][j] == 1:
                    t += 1
                if prevA[i][j-1] == 1:
                    t += 1

                if t == 2 or t == 3: #клетка остается живой если имеет 2-3 живых соседей
                    A[i][j] = 1
                else: #клетка погибает от недостатка или переизбытка живых соседей
                    A[i][j] = 0

    prevA = A #обновляем матрицу
    print(prevA)

    return prevA


ax = fig.add_subplot(111) #сетка для графика
A = np.random.randint(low=0, high=2, size=(n,n)) #генерируем рандомную матрицу из 0 и 1
mx = matrix(A)
tx = ax.set_title('1 day')
im = ax.imshow(mx) #вывод первой версии матрицы А

def anim(i): #анимация последующих дней
    mx = matrix(A)
    im = ax.imshow(mx)
    tx.set_text('{0} day'.format(i+2))
    
ani = animation.FuncAnimation(fig, anim, repeat = True, interval = 100)

plt.show()


