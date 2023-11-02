from scipy import sparse
import numpy as np

def dense_csc_multiplication(matrix_sparse, matrix_dense):

    # Using Sscipy to convert sparse matrix to scipy csc matrix
    matrix_csc = sparse.csc_matrix(matrix_sparse)
   
    # Defining the resultant matrix and initializing it to zero.
    resultant_matrix = [[0 for x in range(len(matrix_dense))] for y in range(matrix_csc.shape[1])] 

    # row x column - traversing the rows of dense matrix
    for i in range (len(matrix_dense)):
        # traversing columns of the csc matrix
        for j in range((matrix_csc.shape[1])):
            # traversing in each column and row from ranges in the number of elements
            for k in range(matrix_csc.indptr[i],matrix_csc.indptr[i+1]):
                # adding the results into the resultant matrix
                resultant_matrix[j][i] += matrix_dense[j][matrix_csc.indices[k]] * matrix_csc.data[k]

    return (check_results(resultant_matrix, matrix_csc, matrix_dense))

def check_results(resultant_matrix, matrix_csc, matrix_dense):
    scipy_result = matrix_dense * matrix_csc
    scipy_result = scipy_result.tolist()

    return (scipy_result == resultant_matrix)

def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append(list(map(float, line.strip().split())))
    return np.array(matrix)
