import os

def calculate_sparsity(matrix):
    """
    Calculate the sparsity of a matrix.
    :param matrix: 2D list representing the matrix
    :return: sparsity percentage of the matrix
    """
    total_elements = len(matrix) * len(matrix[0])
    zero_elements = sum(row.count(0) for row in matrix)
    sparsity = (zero_elements / total_elements) * 100
    return sparsity

def read_matrix_from_file(filename):
    """
    Read a matrix from a file.
    :param filename: name of the file
    :return: 2D list representing the matrix
    """
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.strip().split())) for line in f.readlines()]
    return matrix

if __name__ == '__main__':
    folder_path = 'sparse_data'
    folder_path_dense = 'dense_data'
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found.")
        exit()

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Ensure that we're only looking at files (not subdirectories)
        if os.path.isfile(file_path):
            matrix = read_matrix_from_file(file_path)
            sparsity = calculate_sparsity(matrix)
            print(f"Filename: {filename}, Sparsity: {sparsity:.2f}%")

    # Check if the folder exists
    if not os.path.exists(folder_path_dense):
        print(f"Folder {folder_path_dense} not found.")
        exit()

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path_dense):
        file_path = os.path.join(folder_path_dense, filename)

        # Ensure that we're only looking at files (not subdirectories)
        if os.path.isfile(file_path):
            matrix = read_matrix_from_file(file_path)
            sparsity = calculate_sparsity(matrix)
            print(f"Filename: {filename}, Sparsity: {sparsity:.2f}%")
