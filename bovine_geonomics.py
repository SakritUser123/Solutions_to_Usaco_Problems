# Source: https://usaco.guide/general/io
import sys 
sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

N , M = map(int, input().split())

spotty_cows = []
for i in range(N):
    spotty_cows.append(list(input()))

plain_cows = []
for i in range(N):
    plain_cows.append(list(input()))




number = 0
for i in range(M):
    spotty_cows_curr = []
    plain_cows_curr = []
    for j in range(N):

        spotty_cows_curr.append(spotty_cows[j][i])

    

    for j in range(N):
        plain_cows_curr.append(plain_cows[j][i])
    
   

    unique = False
    for k in range(len(plain_cows_curr)):
        if plain_cows_curr[k] in spotty_cows_curr:
            unique = False
            break
        else:
            unique= True
    
    if unique == True:
        number += 1

print(number)
