N, K = map(int,input().split())

nums = list(map(int,input().split()))

if max(nums) <= 0:
    print(0)
else:
    greater_than = nums[K-1]
    count = 0
    for i in range(len(nums)):
        if nums[i] >= greater_than and nums[i] > 0:
            count += 1
    print(count)
