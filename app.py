def formula(x):
    ans = (1) / (x**2)
    return ans

Sum = 0
for i in range(1, 10+1):
    Sum += formula(i)

print(Sum)
