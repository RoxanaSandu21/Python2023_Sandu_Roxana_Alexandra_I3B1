class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.data = [[0] * m for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def matrix_multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply(self, transform):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = transform(self.data[i][j])

    def iterate(self):
        elements = []
        for i in range(self.rows):
            for j in range(self.cols):
                elements.append(self.data[i][j])
        return elements

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Original Matrix:")
print(matrix)

transform_function = lambda x: x * 2
matrix.apply(transform_function)

print("\nMatrix After Transformation:")
print(matrix)

print("\nIterating Through Elements:")
for element in matrix.iterate():
    print(element)

transposed_matrix = matrix.transpose()
print("\nTransposed Matrix:")
print(transposed_matrix)

matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 2)
matrix2.set(0, 1, 3)
matrix2.set(1, 0, 4)
matrix2.set(1, 1, 5)
matrix2.set(2, 0, 6)
matrix2.set(2, 1, 7)

product = matrix.matrix_multiply(matrix2)
print("\nMatrix Multiplication Result:")
print(product)
