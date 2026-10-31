import numpy as np

A_T = A.T
A_T_A = np.dot(A_T, A)
A_T_b = np.dot(A_T, b)
A_T_A_inv = np.linalg.inv(A_T_A)
x = np.dot(A_T_A_inv, A_T_b)
error = np.linalg.norm(np.dot(A, x) - b)
