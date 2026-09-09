import sys
sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")
length_of_new_array = int(input())

new_spots = list(map(int,input().split()))

ids_cows = list(input().split())

new_shuffle = [""] * length_of_new_array

for k in range(3):
    new_shuffle = [""] * length_of_new_array
    for i in range(len(ids_cows)):
        new_spot = new_spots[i] 
        old_spot = new_spots.index(new_spot)# index 3 goes to 1  
        new_shuffle[old_spot] = ids_cows[(new_spot-1)]
    ids_cows = new_shuffle.copy()
    



for i in range(len(new_shuffle)):
    print(new_shuffle[i])
