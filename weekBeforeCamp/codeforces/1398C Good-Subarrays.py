t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    nums = [0]* n
    for i in range(n):
        nums[i] = int(s[i])
    count = 0
    prefixSum = 0
    d = {0: 1}  
    for i in range(n):
            num = int(nums[i])
            prefixSum += num
            if prefixSum-(i+1) in d:
                count += d[prefixSum-(i+1)]
            if prefixSum-(i+1) in d:
                d[prefixSum-(i+1)] += 1
            else:
                d[prefixSum-(i+1)] = 1

    print(count)