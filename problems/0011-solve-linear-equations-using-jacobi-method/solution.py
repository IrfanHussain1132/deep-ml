import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    res=[0.0]*len(b)
    x=[0.0]*len(b)
    for _ in range(n):
        for i in range(len(b)):
            diasum=sum(A[i][j]*x[j] for j in range(len(b)) if j!=i)
            res[i]=(1/A[i][i])*(b[i]-diasum)
        x=res.copy()
    
    return x