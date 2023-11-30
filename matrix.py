#Реализуйте класс Matrix, представляющий матрицу. Класс должен иметь следующие методы:
#- __init__(self, rows, cols): конструктор класса, инициализирует атрибуты rows (количество строк в матрице) и cols (количество столбцов в матрице).
#- set_element(self, row, col, value): устанавливает значение элемента матрицы с индексами row и col на значение value.
#- get_element(self, row, col): возвращает значение элемента матрицы с индексами row и col.
#- get_rows(self): возвращает количество строк в матрице.
#- get_cols(self): возвращает количество столбцов в матрице.


class Matrix:
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        self.matrix={}

    def set_element(self,row,col,value):
        self.matrix[row,col] = value

    def get_element(self, row,col):
        return self.matrix[row,col]
    def get_rows(self):
        return self.rows
    def get_cols(self):
        return self.cols
    
matrix = Matrix(2, 3)
matrix.set_element(0, 0, 1)
matrix.set_element(0, 1, 2)
matrix.set_element(0, 2, 3)
matrix.set_element(1, 0, 4)
matrix.set_element(1, 1, 5)
matrix.set_element(1, 2, 6)
print(matrix.get_element(0, 0))
print(matrix.get_element(1, 2))    
print(matrix.get_rows())           
print(matrix.get_cols())   
