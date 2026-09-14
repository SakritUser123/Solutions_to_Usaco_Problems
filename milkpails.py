import sys
sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")
X , Y , M = map(int, input().split())
largest_sum = 0

total_sum = 0
for i in range(1,2000):
    for j in range(1,2000):
            
    
        total_sum = (X * i) + (Y*j)
        if total_sum > largest_sum and total_sum <= M:
            largest_sum = total_sum
print(largest_sum)
