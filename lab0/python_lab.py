## Task 1
minutes_in_week = 7 * 24 * 60

## Task 2
remainder_without_mod = 2304811 - 2304811//47 * 47

## Task 3
divisible_by_3 = (673 + 909) % 3 == 0

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares ={ int(x**(0.5)) for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets output nine element
X1 = { 2, 3, 4 }
Y1 = { 5, 6, 7 }

## Task 8: enter in the two new setsm five element
X2 = { 0,1,2 }
Y2 = { 3,3,5 }

## Task 9
base = 10
digits = list(range(base))
three_digits_set = {x*base**0 + y*base**1+z*base**2 for x in digits for y in digits for z in digits}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { i for i in S if i in T }

## Task 11
L_average = sum([20, 10, 15, 75])/len([20, 10, 15, 75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum =  sum([sum(i) for i in LofL]) # use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [(x,y) for x in ['A','B','C'] for y in {1,2,3}] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list =  [(x,y,z) for x in S for y in S for z in S if x+y+z ==0]

## Task 15
exclude_zero_list = [(x,y,z) for x in S for y in S for z in S if x+y+z ==0 and (x,y,z) != (0,0,0)]

## Task 16
first_of_tuples_list = [(x,y,z) for x in S for y in S for z in S if x+y+z ==0 and (x,y,z) != (0,0,0)][0]

## Task 17
L1 = [1,2,3,1] # <-- want len(L1) != len(list(set(L1)))
L2 = ['a','b','c'] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {x for x in range(100) if x%2 != 0}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(len(L)),L))

## Task 20
list_sum_zip = [sum(i) for i in zip([10,25,40],[1,15,20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [i[k] for i in dlist]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [i.get(k,'NOT PRESENT') for i in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [i.get(k,'NOT PRESENT') for i in dlist] # <-- as you do here

## Task 23
square_dict = {k: k**(0.5) for k in range(99)}

## Task 24
D = {'red','white','blue'}
identity_dict = {k: k for k in D}

## Task 25
base = 10
digits = set(range(base))
# representation_dict = {k:v for (k,v) in zip(range(base**3),[(x,y,z) for x in digits for y in digits for z in digits])}
# representation_dict = {x*base**0+y*base**1+z*base**2 : (x,y,z) for x in digits for y in digits for z in digits}
representation_dict = {x*base**2+y*base**1+z*base**0 : (x,y,z) for x in digits for y in digits for z in digits}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {name: d[names.index(name)] for name in names if name and names.index(name) in d}

## Task 27
def nextInts(L): return [ i+1 for i in L]

## Task 28
def cubes(L): return [i**3 for i in L]

## Task 29
def dict2list(dct, keylist): return [ dct[i] for i in keylist]

## Task 30
def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist,L)}

