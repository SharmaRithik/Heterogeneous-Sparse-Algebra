from csr_sparse_dense import csr_dense_multiplication
from csr_sparse_dense import read_matrix 
from dense_dense_matmul import matrix_multiply
from csc_dense_sparse import dense_csc_multiplication
from csc_dense_sparse import read_matrix 


matrix1 = read_matrix("/home/riksharm/Heterogeneous-Sparse-Algebra/sparse_data/sparse_matrix_small90")
matrix2 = read_matrix("/home/riksharm/Heterogeneous-Sparse-Algebra/dense_data/dense_matrix_small100")

# Sparse * Dense multiplication
#result = matrix_multiply(matrix1, matrix2)
#result = csr_dense_multiplication(matrix1, matrix2)
result = dense_csc_multiplication(matrix2, matrix1)
print(result)
