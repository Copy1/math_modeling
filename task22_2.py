for n in range(3,10000+1):    
    s = '5' + '2' * n 
    while ('52 in s') or ('1122 in s') or ('2222 in n'):
        s = s.replace('52', '11', 1)
        s = s.replace('1122', '5', 1)
        s = s.replace('2222', '25', 1)
    if 
