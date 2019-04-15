class Matrix(object):
    def __init__(self, matrix_string):
        if "\n" in matrix_string:
            rows_temp = matrix_string.split("\n")
        else:
            rows_temp = matrix_string

        self.rows = []
        for row in rows_temp:
            row_temp = []
            for i in row.split(" "):
                row_temp.append(int(i))
            self.rows.append(row_temp)

        column_count = len(self.rows[0])

        self.columns = []
        count = 0
        for i in range(column_count):
            column_temp = []
            for row in self.rows:
                column_temp.append(row[count])
            self.columns.append(column_temp)
            count+=1

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
