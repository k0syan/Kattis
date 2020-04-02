nums = [int(x) for x in input().split()]
sNums = sorted(nums)
while True:
    for i in range(4):
        c = nums[i]
        n = nums[i + 1]
        if c > n:
            nums[i] = n
            nums[i + 1] = c
            print(" ".join(str(x) for x in nums))
    if nums == sNums:
        break
