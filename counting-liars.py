
N = int(input())
info = []
for i in range(N):
    lett , num =  input().split()
    num = int(num)
    info.append([lett,num])


nums = []

for i in range(len(info)):
    nums.append(info[i][1]-1)
    nums.append(info[i][1]+1)
    nums.append(info[i][1])



lies = []
for i in range(len(nums)):
    lie = 0
    for j in range(len(info)):
        if info[j][0] == 'G':
            if nums[i] < info[j][1]:
                lie += 1
        if info[j][0] == 'L':
            if nums[i] > info[j][1]:
                lie += 1
    lies.append(lie)

numbers = []
for i in range(len(info)):
    numbers.append(info[i][1])

if min(numbers) == max(numbers):
    print(0)
    exit()
print(min(lies))
