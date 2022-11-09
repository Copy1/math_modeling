#Найти максимальный элемент каждого столбца массива, вводимой с клавиатуры. Размерность массива также задается с клавиатуры.

list1 = []
n = int(input('размер массива: '))
for i in range(0, n):
  list1.append(int(input('введите элемент:')))

for i in range (0, n):
  print(list1[i])
  
#def large(arr):
 # maax  = arr[0]
  #for ele in arr:
   # if ele > maax:
    #  maax = ele
  #return maax


#result = large(list1)
#print(result)

maax = max(list1)
print('наибольший элемент: ', maax)