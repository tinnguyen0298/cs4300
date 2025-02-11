import numpy as np

def matrix_multiplication(A, B): # performs matrix multiplication of two 2D lists.
    A = np.array(A)
    B = np.array(B)
    return np.matmul(A, B).tolist()

def test_square_matrices():
    A = [[2, 4], [1, 3]]
    B = [[5, 6], [7, 8]]
    expected_result = [[38, 44], [26, 30]]
    assert matrix_multiplication(A, B) == expected_result

def test_rectangular_matrix():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    expected_result = [[58, 64], [139, 154]]  # 2x3 * 3x2 = 2x2 matrix
    assert matrix_multiplication(A, B) == expected_result

def test_single_element_matrices():
    A = [[3]]
    B = [[7]]
    expected_result = [[21]]
    assert matrix_multiplication(A, B) == expected_result
