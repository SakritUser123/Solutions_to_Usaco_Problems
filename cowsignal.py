import sys
sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")
rows, columns, scale_factor = map(int, input().split())
matrix = []
for i in range(rows):
    matrix.append(input())
    


new_matrix = [""] * len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        new_matrix[i] += (scale_factor*matrix[i][j])



newest_matrix = []
for i in range(len(new_matrix)):
    for j in range(scale_factor):
        newest_matrix.append(new_matrix[i])



for i in range(len(newest_matrix)):
    print(newest_matrix[i])
