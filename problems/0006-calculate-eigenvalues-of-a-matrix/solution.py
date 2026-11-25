import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    eigenvalues=[]
    a=float((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))
    b=(float(matrix[0][0]+matrix[1][1]))
    coeff=[1,-b,a]
    eigenvalues=np.roots(coeff)
    return eigenvalues
