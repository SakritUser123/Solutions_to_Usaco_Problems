import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")
N = int(input())
points_for_first_case = 0
points_for_second_case = 0
points_for_third_case = 0
shell_arrangment = [1,2,3]
for i in range(N):
    
    first_shell , second_shell , guess = map(int, input().split())
    
    first_shell_index = first_shell-1
    second_shell_index = second_shell-1
    shell_arrangment[first_shell_index] , shell_arrangment[second_shell_index] = shell_arrangment[second_shell_index], shell_arrangment[first_shell_index]
    if(shell_arrangment[guess-1]==1):
        points_for_first_case += 1
    if(shell_arrangment[guess-1]==2):
        points_for_second_case += 1
    if(shell_arrangment[guess-1]==3):
        points_for_third_case += 1

print(max(points_for_first_case,points_for_second_case,points_for_third_case))
