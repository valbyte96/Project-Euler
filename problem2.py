'''PROJECT EULER PROBLEMS

AUTHOR: VAL MCCULLOCH

PROBLEM 2:
Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do
not exceed four million, find the sum of the even-valued terms.

SOLUTION: 4613732

'''


def main():
    #initialize variables
    fib1 = 1
    fib2 = 2
    #initialize sum at 2
    fibSum = 2

    while(True):
        fib = fib1+fib2
        #reestablish values
        fib1 = fib2
        fib2 = fib
        if fib >= 4000000: #break when number exceeds 4 mil
            break
        #if even add to sum
        elif fib%2==0:
            fibSum+=fib

    #print final answer
    print(fibSum)




main()
