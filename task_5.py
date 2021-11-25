a = int(input('введите целое число: '))
c = int(input('введите еще одно целое число: '))

if a % c == 0 and a != 0:
    print(a % c, '- остаток')
elif a == 0:
  print(a // c, 'делитель равен нулю')
else: 
  print( a % c, 'не делится')