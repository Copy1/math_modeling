import numpy as np
numeral = int(input())
answ=''
def roman_numeral(num):
    roman_numeral = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I':1}
    r_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    for l in roman_numeral.keys:
        while numeral >= roman_numeral[l]:
            numeral=numeral - roman_numeral[l]
            answ= answ + l 


        
        