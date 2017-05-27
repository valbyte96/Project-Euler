'''PROJECT EULER PROBLEMS

AUTHOR: VAL MCCULLOCH

PROBLEM 4:
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

SOLUTION: 906609

'''
#function determines if integer is palindrome
def isPal(num):
    num = str(num) #cast to string
    if num == num[ : : -1 ]: #if the num forward is same as reversed
        return True

    return False
    


def main():
    
    lProd = 0 #init largest prod
    cProd = 0 #init current prod
        
    for i in range(100,1000):
        for j in range(100,1000):
            cProd = i * j
            if cProd > lProd and isPal(cProd):
                lProd = cProd
                
    print(lProd) #prints solution
        
    



main()
