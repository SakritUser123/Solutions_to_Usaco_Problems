import sys 
sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")
N = int(input())
barn= []
for i in range(N):
    barn.append(int(input()))
distances = []
for j in range(len(barn)):
    door_minimum_position = (j + 1)
    min_distance = 0
    for i in range((len(barn))):

        if((i+1)) > door_minimum_position:
            min_distance += ((i+1)-door_minimum_position) * barn[i]
        elif (i+1) == door_minimum_position:
            min_distance += 0
        else:
            min_distance += ((len(barn)-door_minimum_position) + (i+1) )* barn[i]

    
    distances.append(min_distance)

print(min(distances))
