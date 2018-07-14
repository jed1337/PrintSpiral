from Direction import Context

width  = int(input("Enter the width: "))
height = int(input("Enter the height: "))

# 0 is a place holder for empty
# We assume that a non-0 value refers to a cell that has already been filled
matrix = [[0 for i in range(width)] for j in range(height)]

context = Context(matrix)
context.fill_matrix()