a = float(input('введите катет 1: '))
b = float(input('введите катет 2: '))
c = float(input('введите катет 3: '))

#if a < b + c and b < a + c and c < b + a:
  #print('Ваш треугольник существует')
if a==b and a!=c :
   print('равнобедренный')
elif a!=b and a!=c and b!=c :   
   print('разносторонний')
elif a==b and a==c and c==b :
   print('равносторонний')
else:
   print('такой треугольника не может существовать, попробуй еще раз')
   

#f'{a} > {b} + {c} or {b} > {a} + {c} or {c} > {b} + {a}'
#if True:
 # if True:
  #  print('2 if')
  #print('1 if')
