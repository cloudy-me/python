class Cell:

    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell >= other.cell:
            return self.cell - other.cell
        else:
            return f'Subtraction is not possible'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return int(self.cell / other.cell)

    def make_order(self, num):
        rows_int = int(self.cell / num)
        rows_rem = int(self.cell % num)
        i = 1
        row_final = ''
        while rows_int > i:
            row_final += f'{"*" * num}\\n'
            i += 1
        row_final += f'{"*" * rows_rem}\\n' if rows_rem > 0 else ''
        return row_final


a = Cell(30)
b = Cell(4)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))
print(b.make_order(5))
