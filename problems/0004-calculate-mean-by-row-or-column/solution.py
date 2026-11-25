import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    arr=np.array(matrix)

    if mode=='column':
        means=np.mean(arr,axis=0)
    else:
        means=np.mean(arr,axis=1)

    return means