def func_a(num):
    return num + 1

def funception(func_a, start):
    def func_b(stop):
        x = start
        if x < 0:
            return None
        elif x > stop:
            ans = func_a(x)
            return ans
        else:
            ans = 1
            while x < stop:
                ans *= func_a(x)
                x += 1
            return ans
    return func_b
a = funception(func_a, 5)
print(a(4))