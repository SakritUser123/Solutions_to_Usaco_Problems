
import sys 
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")
import itertools
K, N = map(int,input().split())

nums = [i for i in range(1,N+1)]

iterable_list = list(itertools.permutations(nums,2))


values_list = {}

for i in range (len(iterable_list)):
    values_list[iterable_list[i]] = True

for i in range(K):
    curr_line = list(map(int,input().split()))
    for j in range(len(iterable_list)):
        if curr_line.index(iterable_list[j][0]) > curr_line.index(iterable_list[j][1]):

            #it is consistent so far
            if iterable_list[j] in values_list.keys():
                values_list[iterable_list[j]] = True
            else:
                pass
        else:
            values_list[iterable_list[j]] = False
            
    values_list = {key: value for key,value in values_list.items() if value is not False}
    

print(len(values_list))

