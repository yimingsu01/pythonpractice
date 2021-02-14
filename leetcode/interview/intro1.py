nums = [2,2,1]
i = 0
num = 0
while (i < len(nums)) :
    num ^= nums[i]
    print(num)
    i += 1
# 一个数字与0异或等于本身，一个数字与本身异或等于0；把所有数字进行异或就能得到结果。
