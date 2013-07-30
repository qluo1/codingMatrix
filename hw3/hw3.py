# version code 829
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec



## Problem 1
# Please represent your solutions as lists.
vector_matrix_product_1 = (Mat(({0,1},{'a','b'}),{(0,'a'):1,(0,'b'):1,(1,'a'):1,(1,'b'):-1}) * Vec({'a','b'},{'a':0.5,'b':0.5})).tolist()
vector_matrix_product_2 = (Mat(({0,1},{'a','b'}),{(1,'b'):1}) * Vec({'a','b'},{'a':1.2,'b':4.44})).tolist()
vector_matrix_product_3 = (Mat(({0,1,2},{0,1,2}),{(0,0):1,(0,1):2,(0,2):3, (1,0):2,(1,1):3,(1,2):4,(2,0):3,(2,1):4,(2,2):5}) * Vec({0,1,2},{0:1,1:2,2:3})).tolist()


## Problem 2
# Represent your solution as a list of rows.
# For example, the identity matrix would be [[1,0],[0,1]].

M_swap_two_vector = [[0,1],[1,0]]



## Problem 3
three_by_three_matrix = [[1,0,1],[0,1,0],[1,0,0]] # Represent with a list of rows lists.



## Problem 4
multiplied_matrix = [[2,0,0],[0,4,0],[0,0,3]] # Represent with a list of row lists.



## Problem 5
# Please enter a boolean representing if the multiplication is valid.
# If it is not valid, please enter None for the dimensions.

part_1_valid = None # True or False
part_1_number_rows = None # Integer or None
part_1_number_cols = None # Integer or None

part_2_valid = None
part_2_number_rows = None
part_2_number_cols = None

part_3_valid = None
part_3_number_rows = None
part_3_number_cols = None

part_4_valid = None
part_4_number_rows = None
part_4_number_cols = None

part_5_valid = None
part_5_number_rows = None
part_5_number_cols = None

part_6_valid = None
part_6_number_rows = None
part_6_number_cols = None

part_7_valid = None
part_7_number_rows = None
part_7_number_cols = None




## Problem 6
# Please represent your answer as a list of row lists.

small_mat_mult_1 = None
small_mat_mult_2 = None
small_mat_mult_3 = None
small_mat_mult_4 = None
small_mat_mult_5 = None
small_mat_mult_6 = None



## Problem 7
# Please represent your solution as a list of row lists.

part_1_AB = None
part_1_BA = None

part_2_AB = None
part_2_BA = None

part_3_AB = None
part_3_BA = None



## Problem 8
# Please represent your answer as a list of row lists.
# Please represent the variables a and b as strings.
# Represent multiplication of the variables, make them one string.
# For example, the sum of 'a' and 'b' would be 'a+b'.

matrix_matrix_mult_1    = None
matrix_matrix_mult_2_A2 = None
matrix_matrix_mult_2_A3 = None

# Use the string 'n' to represent variable the n in A^n.
matrix_matrix_mult_2_An = None



## Problem 9
# Please represent your answer as a list of row lists.

your_answer_a_AB = None
your_answer_a_BA = None

your_answer_b_AB = None
your_answer_b_BA = None

your_answer_c_AB = None
your_answer_c_BA = None

your_answer_d_AB = None
your_answer_d_BA = None

your_answer_e_AB = None
your_answer_e_BA = None

your_answer_f_AB = None
your_answer_f_BA = None



## Problem 10
column_row_vector_multiplication1 = Vec({0, 1}, {None})

column_row_vector_multiplication2 = Vec({0, 1, 2}, {None})

column_row_vector_multiplication3 = Vec({0, 1, 2, 3}, {None})

column_row_vector_multiplication4 = Vec({0,1}, {None})

column_row_vector_multiplication5 = Vec({0, 1, 2}, {None})



## Problem 11
def lin_comb_mat_vec_mult(M, v):
    assert(M.D[1] == v.D)
    pass



## Problem 12
def lin_comb_vec_mat_mult(v, M):
    assert(v.D == M.D[0])
    pass



## Problem 13
def dot_product_mat_vec_mult(M, v):
    assert(M.D[1] == v.D)
    pass



## Problem 14
def dot_product_vec_mat_mult(v, M):
    assert(v.D == M.D[0])
    pass



## Problem 15
def Mv_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## Problem 16
def vM_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## Problem 17
def dot_prod_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## Problem 18
solving_systems_x1 = None
solving_systems_x2 = None
solving_systems_y1 = None
solving_systems_y2 = None
solving_systems_m = Mat(({0, 1}, {0, 1}), {None})
solving_systems_a = Mat(({0, 1}, {0, 1}), {None})
solving_systems_a_times_m = Mat(({0, 1}, {0, 1}), {None})
solving_systems_m_times_a = Mat(({0, 1}, {0, 1}), {None})



## Problem 19
# Please write your solutions as booleans (True or False)

are_inverses1 = None
are_inverses2 = None
are_inverses3 = None
are_inverses4 = None

