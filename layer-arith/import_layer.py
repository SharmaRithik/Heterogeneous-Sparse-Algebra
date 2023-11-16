from csr_sparse_dense import read_mtx
matrix1 = read_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc1_weight.mtx")
print(matrix1.shape)
