from math import *
def task1():
    """Произвести по формуле рассчет функции
    a=(3+e**2)/(1+x**2*ABS(y-tan(z))),b=1+ABS(y-x)+(y-x)**2/2+(x-y)**2/3"""

    x = float(input("Введите число x "))
    y = float(input("Введите число y "))
    z = float(input("Введите число z "))
    if z%(pi/2)==0:
        #проверка
        return ("тангенса при заданном z не существует")
    a = (3 + exp(2)) / (1 + x ** 2 * abs(y - tan(z)))
    b = 1 + abs(y - x) + (y - x) ** 2 / 2 + (x - y) ** 2 / 3
    print ("a=",a,"b=",b)
#task1()
def task2():
    """Произвести по формуле рассчет функции"""

    # ввод переменных
    x = float(input("Введите число x "))

    # константы
    a = -2
    b = 5
    c = 3

    f = (b*x + a)**2/(c + x**3) + x**4

    print ("f(x)=",f)
#task2()
def task3():
    """Произвести по формуле рассчет функции"""
    # ввод переменных
    x = float(input("Введите число x "))

    if cos(x**2) <= 0:
        return ("Введите другое значение")

    f = abs(log(cos(x**2)))/sin(x**2+sqrt(x))

    print("f(x)=",f)
#task3()
def task4():
    '''вычислить длину h, опущенную на гипотинузу треугольника с катетами a,b'''
    a = float(input("Введите катет a "))
    b = float(input("Введите катет b "))

    if a <= 0 or b <= 0:     #проверка
        return ("Введите другое значение")

    #S=0.5*a*b or S=0.5*h*gip => h=a*b/gip; gip получим из теоремы пифагора
    gip = (a**2 + b**2)**(1/2)
    h = a*b/gip

    print ("Высота треугольника =",h)
#task4()
def task5():
    '''Вычислите, какое наибольшее количество шаров радиуса r
    можно разместить в равностороннем треугольнике со стороной а'''
    a = float(input("Введите сторону треугольника "))
    r = float(input("Введите радиус шара "))

    if r >= a/2*3**(1/2)\
            or a <= 0\
            or r <= 0:  # проверка
        print('Введеные данные не подходят')
    else:
        hight = a*3**(0.5)/2
        m = hight - 3/2*r
        rows = ((m-3/2*r)//(2*r))+1 #число рядов шаров
        balls = (rows + 1)*rows/2 #количество шаров = сумма арифметической последовательности, тк в каждом ряду чимло шаров увеличивается на 1
        print ('%.4f' % balls)
task5()
def task6():
    '''Вычислить столрону правильного вписанного многоугольника
    с удвоенным числом сторон'''
    r = float(input("Введите радиус вписанной окружности "))
    a = float(input("Введите сторону многоугольника "))

    #выведем формулу для количества сторон
    #a=r*2tg(pi/n) => n=pi/(arctg(a/2r))
    n = int(pi/(atan(a/(2*r))))
    print("Количество сторон исходного многоугольника =",n)
    #рассчитаем сторону многоугольника, умножив n на 2
    side = float(r*2*tan(pi/(2*n)))
    print ("Сторона = ",side)
#task6()
def task7():
    '''задать 6 любых чисел и решить систему уравнений, воспользовавшись формулами '''
    def coff(znach):
        while True:
            a = float(input(f'Введите коэффицент {znach}: '))
            if a >= -10 and a <= 10: #проверяем входные значения
                return a

    A1 = coff('А1')
    B1 = coff('B1')
    C1 = coff('C1')
    A2 = coff('А2')
    B2 = coff('B2')
    C2 = coff('C2')

    D = A1*B2 - A2*B1
    x = (C1*B2 - C2*B1)/D
    y = (A1*C2 - A2*C1)/D

    print('x=',x,'y=',y)
    print('y=','%.4f' % y)  # определени точночти значения y
#task7()
def task8():
    '''перевести темпертуру из цельсии в фаренгейты; цельсия от 0 до 100;
    точность по фарентгейту до 4 цифр'''
    while True:
        Tc=float(input("Введите темпертуру в цельсия от 0 до 100: "))
        if Tc >= 0 and Tc <= 100: #проверяем входные значения
            break
    Tf = 1.8*Tc + 32 #переводим в фаренгейты
    T = '%.4f' % Tf #округляем до 4 знаков после запятой
    print (T)
#task8()
def task9():
    '''конвертер валюты из рублей в доллары с постоянной
    комиссией и корглением до 4 знаков'''
    COMISSION = 0.1
    RATE = 96.67
    while True:
        rubles = float(input("Введите сумму в рублях >0 : "))
        if rubles > 0:
            break
    dollars = rubles/RATE*(1 - COMISSION)
    money = '%.4f' % dollars
    print (money,'долларов')
#task9()
