import numpy as np
from vec import Vec
from mat import Mat
def solver(a,b):
	if isinstance(a,Vec):
		a_v = a.tolist()
	elif isinstance(a,Mat):
		a_v = a.to_row_list()
	else:
		assert(type(a) ==list)
		a_v = a

	if isinstance(b,Vec):
		b_v = b.tolist()
	elif isinstance(b,Mat):
		b_v = b.to_row_list()
	else:
		assert(type(b) == list)
		b_v = b

	a_v = np.array(a_v)
	b_v = np.array(b_v)
	x = np.linalg.solve(a_v,b_v)

	return x.tolist()
