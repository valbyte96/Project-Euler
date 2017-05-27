'''PROJECT EULER PROBLEMS

AUTHOR: VAL MCCULLOCH

PROBLEM 48:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

SOLUTION: 9110846700

'''


def main():

    s=0 #initialize sum

    for i in range(1,1001):
        s=s+i**i

    s=str(s) #convert to string
    print(s[-10:]) #string slicing 




main()
