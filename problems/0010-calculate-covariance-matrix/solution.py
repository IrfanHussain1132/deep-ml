import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    a=np.array(vectors)
    res=np.cov(a,rowvar=True)
    return res