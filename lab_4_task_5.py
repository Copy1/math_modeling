#Создать функцию, определяющую площади круга, прямоугольника и треугольника по соответствующим параметрам, в зависимости от того, какую фигуру выберет пользователь.
import numpy as np
def xxx(figura, xxy):
    if figura == 'квадрат':
        a,b = xxy
        otvet = a*b
    elif figura == 'круг':
        print(xxy[0])
        otvet = np.pi*(xxy[0]**2)
    elif figura == 'треугольник':
        a,b = xxy
        otvet = (a*b)//2
    else:
      print('вы ввели дичь, все нормально')
      input('начните сначала')
     
    return f' Площадь {figura} = {otvet}'
    
figura = input('фигура :  ')
xxy = [ float(i) for i in input('данные (через пробел) :  ').split()]
print(xxx(figura, xxy))


