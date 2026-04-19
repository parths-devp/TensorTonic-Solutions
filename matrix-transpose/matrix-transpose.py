import numpy as np
def matrix_transpose(a):
    a = np.asarray(a)
    b = np.zeros((a.shape[1], a.shape[0]))
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            b[j,i] = a[i,j]
    return b
