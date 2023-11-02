from scipy import sparse
import time
import numpy as np

# using this function to generate all possible block sizes
def get_block_sizes(matrix_sparse):
    main_matrix = []
    sub_matrix = []
    row = len(matrix_sparse)
    column = len(matrix_sparse[0])
    for i in range(1,row):
        for j in range(1,column):
            if(row % i == 0):
                if(column % j == 0):
                    sub_matrix.append([i,j])
    # main_matrix contains list of all possible block sizes
    main_matrix.append(sub_matrix)

    return main_matrix

# using this function to create different matrix, and perform multiplication
def get_matrix(matrix_sparse, matrix_dense):
    #main_matrix = get_block_sizes(matrix_sparse)
    bsr_matrix_multiplication(10, 10, matrix_sparse, matrix_dense)

    #for i in range(len(main_matrix[0])):
        #row = main_matrix[0][i][0]
        #column = main_matrix[0][i][1]
        #bsr_matrix_multiplication(row, column, matrix_sparse, matrix_dense)

def bsr_matrix_multiplication(row, column, matrix_sparse, matrix_dense):
    bsr_matrix = sparse.bsr_matrix(matrix_sparse, blocksize = (row,column))
    resultant_matrix = [[0 for x in range(len(matrix_dense[0]))] for y in range(bsr_matrix.shape[0])]
    indptr = bsr_matrix.indptr
    indices = bsr_matrix.indices

    for i in range(indptr.shape[0] - 1):
        row_start = indptr[i]
        row_end = indptr[i+1]
        for j in range(row_start, row_end):
            col = indices[j]
            for r in range(row):
                for c in range(column):
                    for d in range(len(matrix_dense[0])):
                        resultant_matrix[i*row+r][d] += bsr_matrix.data[j][r][c] * matrix_dense[col*column+c][d]

    print(check_results(resultant_matrix, bsr_matrix, matrix_dense))

def check_results(resultant_matrix, bsr_matrix, matrix_dense):
    scipy_result = bsr_matrix * matrix_dense
    scipy_result = scipy_result.tolist()

    return (scipy_result == resultant_matrix)
    
def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append(list(map(float, line.strip().split())))
    return np.array(matrix)
