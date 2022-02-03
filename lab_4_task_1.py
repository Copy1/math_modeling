

def zoi_funс(L):
  
  S = 0
  for i in range(len(L)):
    S = S + L[i]
  return S/len(L)


L = [1, 7, 9, 90]
print(zoi_funс(L))

