import time

from csr_sparse_dense import csr_mul
from csr_sparse_dense import read_matrix 
from csr_sparse_dense import read_mtx 
from csr_sparse_dense import check_results 
from dense_dense_matmul import matrix_multiply
from dense_dense_matmul import check_result 
from csc_dense_sparse import dense_csc_multiplication
from csc_dense_sparse import read_matrix 
from bsr_matmul import get_matrix
from bsr_matmul import read_matrix

def calculate_sparsity(matrix):
    """
    Calculate the sparsity of a matrix.
    :param matrix: 2D list representing the matrix
    :return: sparsity percentage of the matrix
    """
    total_elements = len(matrix) * len(matrix[0])
    zero_elements = sum(row.count(0) for row in matrix)
    sparsity = (zero_elements / total_elements) * 100
    print(Sparsity)
    return sparsity

#matrix1 = read_matrix("/home/riksharm/Heterogeneous-Sparse-Algebra/sparse_data/sparse_matrix_small90")
#matrix2 = read_matrix("/home/riksharm/Heterogeneous-Sparse-Algebra/dense_data/dense_matrix_small100")

# Read condensa cifar-10 matrices
matrix1 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc1_weight.mtx")
matrix2 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc2_weight.mtx")

# Slice the matrices 50-50
matrix1 = matrix1[:256, :512]
#matrix1_part1 = matrix1[:128, :256]
matrix1_part1 = matrix1[:128, :512]
matrix1_part2 = matrix1[128:256, 256:512]
print(matrix1_part2.shape)

#matrix2_part1 = matrix2[:256, :128]
matrix2_part1 = matrix2[128:256, :512]
matrix2_part1 = matrix2_part1.transpose
matrix2_part2 = matrix2[256:512, :256]

# Now this should be callable and return the correct shape
print("Matrix Mul three loops - Part1")
start_time = time.time()
result = matrix_multiply(matrix1_part1, matrix2_part1)
end_time = time.time()
#print(result)
check_result(matrix1_part1, matrix2_part1, result)
print(end_time - start_time, "seconds")


print(matrix1_part1.shape)
print(matrix2_part1.shape)
print("Matrix Mul three loops - Part2")
start_time = time.time()
#result = matrix_multiply(matrix1_part2, matrix2_part2)
end_time = time.time()
#print(result)
#check_result(matrix1_part2, matrix2_part2, result)
print(end_time - start_time, "seconds")


print("Matrix Mul CSR - Part1")
start_time = time.time()
result = csr_mul(matrix1_part1, matrix2_part1)
end_time = time.time()
#print(result)
check_result(result, matrix1_part1, matrix2_part1)
print(end_time - start_time, "seconds")



# Sparse * Dense multiplication
#result = matrix_multiply(matrix1, matrix2)
#result = csr_dense_multiplication(matrix1, matrix2)
#result = dense_csc_multiplication(matrix2, matrix1)
#result = get_matrix(matrix1, matrix2)
#print(result)
