import numpy as np

# computing the fibonacci sequence using exponentiation
def fibonacci_matrix(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    F = np.array([[1, 1],
                   [1, 0]], dtype=object)
    return np.linalg.matrix_power(F, n - 1)[0, 0]

# main execution, computing a specified fibonacci
# number in pace n in the set of fibonacci numbers
print(fibonacci_matrix(100))