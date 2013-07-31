from vec import Vec
from itertools import chain

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f.get(k,0)

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    if val:
        M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    keys = chain(A.f.keys(),B.f.keys())
    return Mat(A.D, {k: A[k] + B[k] for k in keys})

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    return Mat(M.D,{k: alpha * M[k] for k in M.f.keys()})

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    keys = chain(A.f.keys(),B.f.keys())
    ret = True
    for k in keys:
        if A[k] != B[k]:
            ret = False
            break
    return ret

def transpose(M):
    "Returns the transpose of M"
    return Mat((M.D[1],M.D[0]),{(k[1],k[0]): M[k] for k in M.f.keys() })

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    # col vector
    col_vec =[(c,Vec(v.D,{r: M[r,c] for r in M.D[0]})) for c in M.D[1]]

    # vec * col_vec
    return Vec(M.D[1], {c: v*vec for (c,vec) in col_vec})

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    # row vec
    row_vec = [(r,Vec(v.D,{c: M[r,c] for c in M.D[1]})) for r in M.D[0]]
    
    return Vec(M.D[0], {r: v*vec for (r,vec) in row_vec})

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    a_row_vec = [(r,Vec(A.D[1],{c: A[r,c] for c in A.D[1]})) for r in A.D[0]]

    b_col_vec = [(c,Vec(B.D[0],{r: B[r,c] for r in B.D[0]})) for c in B.D[1]]

    return Mat((A.D[0],B.D[1]), { (r,c): a*b for (r,a) in a_row_vec for (c,b) in b_col_vec if a*b !=0 })

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        # handle python2
        elif isinstance(other,Mat):
            return matrix_matrix_mul(self,other)
        elif isinstance(other,Vec):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        # handle python 2
        elif isinstance(other,Vec):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"

    # enhancement
    def to_row_list(self):
        """ """
        assert(self.D and self.f)

        return [[self[r,c] for c in self.D[1]] for r in self.D[0]]
    def to_col_list(self):
        """ """
        assert(self.D and self.f)
        return [ [self[r,c] for r in self.D[0]] for c in self.D[1]]
