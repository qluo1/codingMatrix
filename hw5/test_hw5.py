from hw5 import *

def test_swap():
    """ """
    S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
    A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
    z = list2vec([0,2,1,1])
    T,o = swap(S, A, z)
    print(T)
    print(o)
    print( Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0}))
    assert o == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})

def test_morph():
    """ """
    S = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
    B = [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
    o = morph(S, B)
    # assert o == [(Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 1, 1: 0, 2: 0})), (Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0})), (Vec({0, 1, 2},{0: 1, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}))]
    for k,v in o:
        print("inj",k)
        print("ej",v)
        print()

test_morph()