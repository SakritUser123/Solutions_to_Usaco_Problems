# Source: https://usaco.guide/general/io
import sys 
sys.stdin = open("mowing.in", "r")
sys.stdout = open("mowing.out", "w")
N = int(input())

directions = []

for i in range(N):
    direction , number = input().split()
    number = int(number)
    directions.append((direction,number))




org_coor = [0,0]

history = [org_coor]

for i in range(len(directions)):
    if directions[i][0] == 'N':
        for j in range(1,(directions[i][1]+1)):
            history.append([org_coor[0],org_coor[1] + j ])
        
    if directions[i][0] == 'E':
        for j in range(1,(directions[i][1]+1)):
            history.append([org_coor[0] + j ,org_coor[1]])
        
    if directions[i][0] == 'S':
        for j in range(directions[i][1]):
            history.append([org_coor[0],org_coor[1]-(j+1)])
        
    if directions[i][0] == 'W':
        for j in range(directions[i][1]):
            history.append([org_coor[0] - (j+1),org_coor[1]])
        
    org_coor = history[-1]



items = {}

for item in range(len(history)):
    key = tuple(history[item])
    items[key] = []

for item in range(len(history)):
    key = tuple(history[item])
    items[key].append(item)

values = []
for item in items.values():
    if len(item)>2:
        values.append(item[-1]-item[-2])
    if len(item) == 2:
        values.append(item[1]-item[0])

if len(values) == 0:
    print(-1)
else:
    print(min(values))


