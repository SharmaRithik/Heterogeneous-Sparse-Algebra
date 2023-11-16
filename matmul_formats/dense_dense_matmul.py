import numpy as np

def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append(list(map(float, line.strip().split())))
    return np.array(matrix)

def matrix_multiply(A, B):
    m, n = A.shape
    p = B.shape[1]
    
    if B.shape[0] != n:
        raise ValueError("Incompatible matrices. Number of columns of A must match number of rows of B.")

    # Initialize the resulting matrix C
    C = np.zeros((m, p))

    # Perform the matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Read the matrices
def dense_dense_pipeline(matrix1, matrix2):
    matrix1=read_matrix(matrix1)
    matrix2=read_matrix(matrix2)
    matrix_multiply(A, B)
    print(result)

def check_result(matrix1, matrix2, result):
    # Perform matrix multiplication to get the answer
    answer = np.dot(matrix1, matrix2)

    # Compare result and answer
    if np.array_equal(result, answer):
        print("Correct Answer")
    else:
        print("Incorrect Answer")

    # Save result and answer to files
    np.savetxt('result_matrix.txt', result)
    np.savetxt('answer_matrix.txt', answer)
#matrix1 = read_matrix("/home/riksharm/Heterogeneous-Sparse-Algebra/sparse_data/sparse_matrix_90")
#matrix2 = read_matrix("/home/riksharm/Heterogeneous-Sparse-Algebra/dense_data/dense_matrix_100")

# Multiply matrices
#result = matrix_multiply(matrix1, matrix2)
#print(result)

