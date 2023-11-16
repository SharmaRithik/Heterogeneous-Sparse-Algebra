from scipy import sparse
import numpy as np

def csr_mul(matrix_sparse, matrix_dense):

    # Using Sscipy to convert sparse matrix to scipy csr matrix
    matrix_csr = sparse.csr_matrix(matrix_sparse)

    # Defining the resultant matrix and initializing it to zero.
    resultant_matrix = [[0 for x in range(matrix_csr.shape[0])] for y in range(len(matrix_dense[0]))]

    # row x column - traversing the rows of csr matrix
    for i in range (len(matrix_csr.indptr) - 1):
        # traversing columns of the dense matrix
        for j in range (len(matrix_dense[0])):
            # traversing in each column and row from ranges in the number of elements
            for k in range(matrix_csr.indptr[i],matrix_csr.indptr[i+1]):
                # adding the results into the resultant matrix
                resultant_matrix[i][j] += (matrix_csr.data)[k] * (matrix_dense[matrix_csr.indices[k]][j])

    return (check_results(resultant_matrix, matrix_csr, matrix_dense))

def check_results(resultant_matrix, matrix_csr, matrix_dense):
    scipy_result = matrix_csr * matrix_dense
    scipy_result = scipy_result.tolist()

    return (scipy_result == resultant_matrix)

def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append(list(map(float, line.strip().split())))
    return np.array(matrix)

def read_mtx(path):
    with open(path, 'r') as file:
        for line in file:
            if line.startswith('%'):
                continue
            else:
                dimensions = list(map(int, line.strip().split()))
                break

        data = []
        for line in file:
            data.append(float(line.strip()))

    return np.array(data).reshape((dimensions[1], dimensions[0])).T

def dense_dense_pipeline(matrix1, matrix2):
    matrix1=read_matrix(matrix1)
    matrix2=read_matrix(matrix2)
    matrix_multiply(A, B)
    print(result)
