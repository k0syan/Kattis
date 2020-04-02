n = int(input())
nums = list()
while n != 0:
    nums.append(int(input()))
    n -= 1
nums.sort()
missingNums = []
maxim = nums[len(nums) - 1]
numsToBe = [x for x in range(1, maxim)]
ans = list(set(numsToBe) - set(nums))
ans.sort()

if len(ans) == 0:
    print("good job")
else:
    print("\n".join(str(x) for x in ans))