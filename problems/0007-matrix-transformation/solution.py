import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    if np.linalg.det(S)==0:
        return -1
    inv=np.linalg.inv(T)
    k=np.matmul(A,S)
    res=np.matmul(inv,k)
    return res