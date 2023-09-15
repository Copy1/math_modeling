
m_str = int(input())
print(m_str.split())

def m_str(seq):
   s=0
   for a in seq:
       if a>0:
           s+=a
   return s

s = 0
 
while m_str > 0:
    digit = m_str % 10
    s = s + digit
    m_str = m_str // 10
 
print("Сумма:", s)

a = int(input())
b= int(input())
if a > b:
    for i in range(a, b, 2):
        print(i, end = '')

N = int(input())
def delit(N) :
    res = 1
    i = 2
    while i * i < N + 1 and res < N:
        if N % i == 0 :
            res += i + N // i * (i*i != N)
        i += 1
    return res < N 
 
print()

