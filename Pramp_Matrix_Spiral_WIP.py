inputMatrix  = [ [1,    2,   3,  4,  5],
                [6,    7,   8,  9,   10],
                [11,  12,  13,  14,  15],
                [16,  17,  18,  19,  20] ]

def spiral_copy(inputMatrix):
    output = []
    traversed = []
    row_forward_counter = 0
    column_right_counter = len(inputMatrix[0]) - 1
    row_backward_counter = len(inputMatrix) - 1
    column_left_counter = 0

    iterator = 1


    while row_forward_counter <= len(inputMatrix)//2 and \
            column_right_counter >= len(inputMatrix[0]) // 2 and \
            row_backward_counter >= len(inputMatrix) // 2 and \
            column_left_counter <= len(inputMatrix[0]) // 2:
        for i in inputMatrix[row_forward_counter]:
            output.append(i)
        row_forward_counter += 1

        for index in range(len(inputMatrix)):
            output.append(inputMatrix[index][column_right_counter])
        column_right_counter -= 1

        matrix_slice = inputMatrix[row_backward_counter]
        for i in reversed(matrix_slice):
            output.append(i)
        row_backward_counter -= 1

        for index in reversed(range(len(inputMatrix))):
            output.append(inputMatrix[index][column_left_counter])
        column_left_counter += 1
        iterator += 1
    return output

print(spiral_copy(inputMatrix))