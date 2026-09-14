
N , U = map(int,input().split()) # N means NxN matrix

# U is number of instructions 

canvas = []

for i in range(N):
    canvas.append(list(input()))




for operation in range(U):
    i , j = map(int,input().split())
    i -= 1
    j -= 1
    if canvas[i][j] == '.':
        canvas[i][j] = '#'

    if canvas[i][j] == '#':
        canvas[i][j] = '.'

    # check if reflecting
    quadrant_length = int(N/2)  # subtract 1 to keep indexes consistent.

    top_left_mat = []
    top_right_mat = []
    bottom_left_mat = []
    bottom_right_mat = []
    full_length = 2 * quadrant_length
    for i in range(full_length):
        if (i+1) == 
        current_row = canvas[i]
        top_left_mat.append([current_row[0:quadrant_length]])
        top_right_mat.append([current_row[quadrant_length: len(canvas[i])+1 ]])

    for k in range(quadrant_length):

print(top_left_mat) 
print(top_right_mat)
