class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        zip_b = zip(*other.values)
        zip_b = list(zip_b)
        return Matrix([[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                 for col_b in zip_b] for row_a in self.values])

    def __rmatmul__(self, other):
        zip_b = zip(*other.values)
        zip_b = list(zip_b)
        return Matrix([[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                 for col_b in zip_b] for row_a in self.values])

    def __imatmul__(self, other):
        zip_b = zip(*other.values)
        zip_b = list(zip_b)
        return Matrix([[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                 for col_b in zip_b] for row_a in self.values])


mat1 = Matrix([[1, 2], [3, 4]])
mat2 = Matrix([[11, 12], [13, 14]])
mat3 = mat1 @ mat2

print(mat3)