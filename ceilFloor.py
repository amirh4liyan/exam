x = int(input())

li = [3, 5, 11, 7, 9]
li.sort()

floor = 0
ceil = 0

if x in li:
    ceil = x
    floor = x
elif x > li[-1]:
    ceil = -1
    floor = [-1]
elif x < li[0]:
    ceil = li[0]
    floor = -1
else:
    L = 0
    R = len(li)-1
    capture = []
    while (L <= R):
        mid = int((L + R)/2)
        item = li[mid]
        if x > item:
            L = mid+1
            ceil = li[L]
            floor = item
        elif x < item:
            ceil = item
            floor = li[R]
            R = mid-1

print("ceil: ", ceil)            
print("floor: ", floor)

