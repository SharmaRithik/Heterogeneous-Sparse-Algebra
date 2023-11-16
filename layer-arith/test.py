import numpy as np
from csr_sparse_dense import read_mtx
matrix1 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc1_weight.mtx")
matrix2 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc2_weight.mtx")
matrix3 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc3_weight.mtx")
matrix4 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc4_weight.mtx")
matrix5 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc5_weight.mtx")
print(matrix1.shape)

def check_sparsity(matrix):
    # Calculate the total number of elements in the matrix
    total_elements = matrix.size

    # Count the number of zero elements
    zero_elements = np.count_nonzero(matrix == 0)

    # Calculate the sparsity as the ratio of zero elements to total elements
    sparsity = zero_elements / total_elements

    return sparsity

#Let's divide the matrix into four equal parts
matrix1_p1 = matrix1[0:256,0:1536]
matrix1_p2 = matrix1[0:256,1536:3072]
matrix1_p3 = matrix1[256:512,0:1536]
matrix1_p4 = matrix1[256:512,1536:3072]

#Set block size for matrix, this will be used for checking sparsity and decomposing it - 70%

def divide_into_blocks(matrix, row, column):
    # check if row and column size is divisible by the shape
    if(matrix.shape[0]%row) == 0:
        print("Possible row size")
    if(matrix.shape[1]%column ==0):
        print("Possible column size")

print(matrix1_p1.shape)
print(matrix1_p2.shape)
print(matrix1_p3.shape)
print(matrix1_p4.shape)

print(check_sparsity(matrix1_p1))
print(check_sparsity(matrix1_p2))
print(check_sparsity(matrix1_p3))
print(check_sparsity(matrix1_p4))
print(check_sparsity(matrix2))
print(check_sparsity(matrix3))
print(check_sparsity(matrix4))
print(check_sparsity(matrix5))


print(divide_into_blocks(matrix1_p1, 4, 4))
