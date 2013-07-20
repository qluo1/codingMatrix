# Please fill out this stencil and submit using the provided submission script.

from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [ v+u for (v,u) in zip(p1_v,p1_u)]
p1_v_minus_u = [v-u for (v,u) in zip(p1_v,p1_u)]
p1_three_v_minus_two_u = [3*v -2*u for (v,u) in zip(p1_v,p1_u)]


## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [v+u for (v,u) in zip(p2_v,p2_u)]
p2_v_minus_u = [v-u for (v,u) in zip(p2_v,p2_u)]
p2_two_v_minus_u = [2*v-u for (v,u) in zip(p2_v,p2_u)]
p2_v_plus_two_u = [v+2*u for (v,u) in zip(p2_v,p2_u)]


## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [v+u for(v,u) in zip([0,one,one],[one,one,one])]
p3_vector_sum_2 = [v+u+u for(v,u) in zip([0,one,one],[one,one,one])]


## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

data_4 = {'a':[one,one,0,0,0,0,0],
		'b':[0,one,one,0,0,0,0],
		'c':[0,0, one,one,0,0,0,],
		'd':[0,0,0,one,one,0,0],
		'e':[0,0,0,0,one,one,0],
		'f':[0,0,0,0,0,one,one],
		}

from itertools import combinations
def search_item(data, item):
	print("search: %s"% item)
	for i in range(2,len(data.keys())):
		for j in combinations(data.keys(),i):
			# print(j, zip(*[data[k] for k in j]), [sum(i) for i in zip(*[data[k] for k in j])])
			if [sum(i) for i in zip(*[data[k] for k in j])] == item:
				print(j)
				# print([data[k] for k in j])
				# print([sum(i) for i in zip(*[data[k] for k in j])]) 
				return set(j)

	return set([])


u_0010010 = search_item(data_4,[0,0,one,0,0,one,0])
u_0100010 = search_item(data_4,[0,one,0,0,0,one,0])

## Problem 5
# Use the same format as the previous problem

data_5 = {'a':[one,one,one,0,0,0,0],
		'b':[0,one,one,one,0,0,0],
		'c':[0,0, one,one,one,0,0,],
		'd':[0,0,0,one,one,one,0],
		'e':[0,0,0,0,one,one,one],
		'f':[0,0,0,0,0,one,one],
		}


v_0010010 = search_item(data_5,[0,0,one,0,0,one,0])
v_0100010 = search_item(data_5,[0,one,0,0,0,one,0])

## Problem 6
uv_a = {}
uv_b = {}
uv_c = {}
uv_d = {}



## Problem 7
# use 'one' instead of '1'
x_gf2 = []



## Problem 8
v1 = []
v2 = []
v3 = []

