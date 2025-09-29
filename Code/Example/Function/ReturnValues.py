def sumGeometric(a, r, n):

    if r == 1:
        return a * n
    s = a * (1 - try1(r, n)) / (1 - r)

    print(s) 
    

def try1(r, n):
    s = r ** n
    return s

sumGeometric(2, 3, 10)
