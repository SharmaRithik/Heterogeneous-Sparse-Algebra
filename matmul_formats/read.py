import numpy as np

def read_dense_matrix_from_mtx(path):
    with open(path, 'r') as file:
        # Skip header and comments
        for line in file:
            if line.startswith('%'):
                continue
            else:
                # Read the matrix dimensions from the first non-comment line
                dimensions = list(map(int, line.strip().split()))
                break
        
        # Read the matrix data, assuming it's written in column-major format
        data = []
        for line in file:
            data.append(float(line.strip()))
    
    # Convert the list of data to a NumPy array with the correct shape
    return np.array(data).reshape((dimensions[1], dimensions[0])).T

# Example usage:
# Replace '/path/to/matrix.mtx' with the actual file path
matrix = read_dense_matrix_from_mtx("/home/riksharm/Heterogeneous-Sparse-Algebra/cifar_tensors/fc1_weight.mtx")
print(matrix)

