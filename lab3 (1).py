from math import *
import matplotlib.pyplot as plt
from pyparsing import White
import numpy as np



def task1():
    '''Определить, оканчивается ли число на четную цифру
     определить, является ли число положительным
     создать бесконечную программу которая проверяет числа'''

    def evenlast(a):
        return abs(a)%10%2 == 0

    def positivenum(a):
        return a > 0

    while True:
        a = float(input("Введите число "))
        #if evenlast(a) == True:
        if evenlast(a):
            print("Последняя цифра числа четная")
        else:
            print("Последняя цифра числа не четная")
        if positivenum(a):
            print("Число положительное")
        else:
            print("Число не положительное")

#task1()

def task2():
    '''Написать функцию, которая вычисляет f для заданного x'''
    #pip install matplotlib в терминале

    a = float(input("Введите левую границу a "))
    b = float(input("Введите правую границу b "))
    n = int(input("Введите количество точек n "))
    X = []
    Y = []

    for x in np.linspace (a,b,n):  # pip install numpy
        if x >= 0:
            f = 2*x**3 - 2
        else:
            f = -10*sin(x)

        X.append(x)
        Y.append(f)

    def znach(A):
        print(f"Значение " ,end='')
        for a in A:
            print(f'{a:.4f} ', end='')
        print()
    znach(X)
    znach(Y)

    plt.plot(X, Y)
    plt.grid(1)  # сетка
    plt.show()

#task2()

def task5():
    '''Написать программу, которая вычисляет произведение отрицательных
    чисел, из 4 заданных, и сообщает о знаке произведения'''
    def proizved():

        A = []

        for a in range (4):
            A.append(float(input("Введите число ")))
        print(f'Заданные числа = {A}')

        B = [a for a in A if a < 0]
        print(f'Отрицательные числа = {B}')

        prod = 1
        for b in B:
            prod = prod*b

        return prod

    result = proizved()
    print(f'Произведение отрицательных чисел = {result:.4f}')

    if result < 0:
        print("Произведение отрицательное")
    else:
        print("Произведение не положительное")

#task5()

def task6():
    '''Написать функцию, которая считает число
    первых 12 членов ряда Фибоначчи'''

    sum = 0
    quan1, quan2 = 1, 1

    for i in range(12):
        sum += quan1
        quan1, quan2 = quan2, quan1 + quan2

    print(f'Число кроликов через год = {sum}')

#task6()

def task8():
    '''Посчитать сумму первых n членов ряда
    провести проверку вводных данных
     посчитать сумму членов ряда с точностью E'''

    x = float(input('Введите х '))

    EPS = 1e-6

    while True:
        n = int(input('Введите число членов n '))
        if n >= 0:
            break

    sum = 0
    i = 0

    while x**i/factorial(i) > EPS:
        sum += x**i/factorial(i)
        i += 1

    print(f"{sum:.4f}")

task8()

def task11():

    while True:
        x = float(input('Введите x '))
        if x%(pi/2) != 0:
            break

    EPS = 1e-6
    sum = pi/2
    c = 1
    znach = 0
    i = 0

    while True:
        znach = (1/((2*i+1)*(x**(2*i+1))))*((-1)**(i+1))
        sum = sum + znach
        print(sum)
        i += 1
        if abs(atan(x) + sum) <= EPS:
            break
    print(f"{sum:.4f}")

#task11()
