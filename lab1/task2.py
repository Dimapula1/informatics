from math import cos, log, exp, sin
x=float(input("Введите значение пременной x: "))
y=float(input("Введите значение пременной y: "))
z=float(input("Введите значение пременной z: "))
a=(x**3/2)**(1/2)-sin(y)
b=exp(2)/3-cos(y)+z+log(y)
print(f"Получено значение функции a={a}")
