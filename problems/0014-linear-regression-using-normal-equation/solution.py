import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X=np.array(X)
    xtra=np.transpose(X)
    xinv=np.linalg.inv(np.matmul(xtra,X))
    theta=np.matmul(np.matmul(xinv,xtra),y)
    return theta