# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [i for i in L if i%num !=0]



## Problem 2
def myLists(L): return  [ [j+1 for j in range(i)] for i in L]


## Problem 3
def myFunctionComposition(f, g): return {k: g[v] for (k,v) in f.items()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j 
complex_addition_b = 0 + 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = .001 + 9j

## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    cum = 0
    for i in L:
        cum += i
    return cum


## Problem 7
def myProduct(L):
    prod = 1
    for i in L:
        prod = prod * i
    return prod

## Problem 8
def myMin(L): 
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min


## Problem 9
def myConcat(L):
    out = ''
    for i in L:
        out += i
    return out


## Problem 10
def myUnion(L):
    out = set()
    for i in L:
        out = out | i
    return out


