#a* x**2 + b*x + c = 0
import numpy as np

a = float(input('введите коэффицент: '))
b = float(input('введите коэффицент: '))
c = float(input('введите коэффицент: '))

print()
print(f'{a}*x**2 + {b}*x + {c} = 0')
print()
D = b**2 - 4*a*c
print(f' D = {b}**2 - 4 *{a}*{c} \n D = {D}')

while D==0:
  print('один корень уравнения')

if D>0: 
  print(' два корня уравнения')

if D<0:
  print('ответ: нет корней')  
  raise SystemExit

print()

x1 = b/-1 + D**0.5 / 2*a
print(f'x1 = {b}/-1 + {D}**0.5 // 2*{a} \n x1 = {x1}')

print()

x2 = b/-1 - D**0.5 / 2*a
print(f'x2 = {b}/-1 - {D}**0.5 // 2*{a} \n x2 = {x2}')

print(f'ответ: {x1}  {x2} ')





