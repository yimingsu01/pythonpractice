'''
因为超过2/n个的数，所以多数为A 其他数为B。
公式如下就满足题意 A - B > 1
所以遍历数组，如果是A就count++,如果是B就count--。
如果count为0，就说明不是多数就将当前的值设置成多数，并重新去count++。
这样遍历完成后的数一定是多数
'''
nums = [3,2,3]
count = 0
mostnum = nums[0]
i = 0
while (i < len(nums)):
    if (nums[i] == mostnum):
        count += 1
    else:
        count -= 1
        if (count == 0):
            mostnum = nums[i]
            count += 1
    i += 1
print(mostnum)