import math

class Matrix:
    """A class represents a mathematical matrix defined by m columns and n rows"""
    def __init__(self, content=[], rows=0, columns=0):
        self.content = content
        self.rows = rows 
        self.columns = columns

    def is_vector(self):
        return self.rows >= 1 and self.columns == 1
    def get_rows(self):
        return self.rows
    def get_columns(self):
        return self.columns
    def get_content(self):
        return self.content
    def get_norm(self, n: int = 2):
        sum = 0
        for i in range(len(self.content)):
            sum += pow(self.content[i],n)
        return math.pow(sum, 1/n)
    def normalize_vector(self):
        if not self.is_vector():
            raise ValueError(f"Can not normalize a non-vector object")
        new_content = []
        for i in range(len(self.content)):
            new_content.append(self.content[i] / self.get_norm())

        return Matrix(new_content, self.get_rows(), self.get_columns())
    def get_column_content(self, no: int):
        if no>=self.columns:
            raise ValueError(f"Column number is not valid")
        return[self.get_content()[i*self.columns + no] for i in range(self.get_rows())]
    
    def get_row_content(self, no: int):
        if no>=self.rows:
            raise ValueError(f"Row number is not valid")
        return[self.get_content()[no*self.columns + i] for i in range(self.get_columns())]
    def is_valid(self):
        """Return a Boolean to confirm validity of a matrix"""
        if (len(self.content) % self.columns) != 0 or (len(self.content) // self.columns) != self.rows:
            raise ValueError("Matrix's total entries does not fit into dimensions (m x n) attributes associated")
    def is_square(self):
        return self.columns == self.rows
    def is_upper_triangular(self):
        upper = True
        for i in range(1, self.rows):
            for j in range(self.columns*i, self.columns*i + i):
                if self.content[j] > 1e-10:
                    upper = False
        return upper
    
    def is_lower_triangular(self):
        lower = True
        for i in range(0, self.rows-1):
            for j in range(i+1, self.columns - 1):
                if self.content[j] > 1e-10:
                    lower = False
        return lower

    def __len__(self):
        """Total entries of the matrix"""
        return len(self.content)
    def __str__(self):
        final = f"{self.rows} x {self.columns} Matrix\n ["
        content = self.content
        for i in range(self.rows):
            for j in range(self.columns):
                final+=str(content[self.columns * i + j])
                final+='   '
            if i <self.rows-1:
                final+='\n'
                final+='  '
        final += ']'
        return final
    
def identity(n: int):

    return Matrix(
        content = [1 if i == (i % n)*n + (i % n) else 0 for i in range(n**2)], rows = n, 
        columns = n)


upper_triangular_matrix = Matrix(
    content=[
        2, 3, 4,
        0, 5, 6,
        0, 0, 7
    ],
    rows=3,
    columns=3
)

print(upper_triangular_matrix.is_upper_triangular())
            



