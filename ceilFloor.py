x = int(input())

li = [3, 5, 11, 7, 9]
li.sort()


if x in li:
    ceil = floor = x
else:
    L = 0
    R = len(li)-1
    while (L <= R):
        mid = (L + R)//2
        item = li[mid]
        if x >= item:
            L = mid+1
        elif x < item:
            R = mid-1

    if item - x < 0:
        if mid+1 > len(li)-1:
            ceil = -1
        else:
            ceil = li[mid+1]
        floor = li[mid]
    elif item - x > 0:
        ceil = li[mid]
        if mid-1 < 0:
            floor = -1
        else:
            floor = li[mid-1]

print("ceil: ", ceil)            
print("floor: ", floor)

