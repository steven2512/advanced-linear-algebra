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
            



