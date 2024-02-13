def matrix_div(matrix, div):
    div_result = []
    for row in matrix:
        column = []
        for element in row:
            column.append(round(element / div, 2))
        div_result.append(column)
    return div_result
    
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]
result = matrix_div(matrix, 6)
print(result)