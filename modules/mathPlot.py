import numpy as np
def polynomial_fit(indipendent_array, dipendent_array):
    polynomial = np.polyfit(indipendent_array, dipendent_array, 3)
    polynomial_class = np.poly1d(polynomial)
    return polynomial_class
