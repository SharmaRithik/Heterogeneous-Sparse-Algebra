import random

def generate_matrix(size, fill_percent):
    """
    Generate a matrix of given size and fill percentage.
    :param size: tuple of (rows, columns) for matrix dimensions
    :param fill_percent: percentage of non-zero elements (e.g., 50 for 50% fill)
    :return: a 2D list representing the matrix
    """
    rows, cols = size
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    num_elements = int((rows * cols) * (fill_percent / 100))

    for _ in range(num_elements):
        while True:
            row = random.randint(0, rows-1)
            col = random.randint(0, cols-1)
            if matrix[row][col] == 0:
                matrix[row][col] = random.randint(1, 10)
                break

    return matrix


def save_to_file(filename, matrix):
    """
    Save a matrix to a file.
    :param filename: name of the file
    :param matrix: the matrix to save
    """
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

if __name__ == '__main__':
    matrix_size = (3000, 3000)
    
    # Generate and save sparse matrices
    for sparsity in [50, 60, 70, 80, 90, 100]:
        print(f"Generating sparse matrix with {sparsity}% sparsity...")
        matrix = generate_matrix(matrix_size, 100 - sparsity)
        filename = f"sparse_matrix_{sparsity}"
        save_to_file(filename, matrix)
        print(f"Saved to {filename}")

    # Generate and save dense matrices
    for density in [50, 60, 70, 80, 90, 100]:
        print(f"Generating dense matrix with {density}% denseness...")
        matrix = generate_matrix(matrix_size, density)
        filename = f"dense_matrix_{density}"
        save_to_file(filename, matrix)
        print(f"Saved to {filename}")

