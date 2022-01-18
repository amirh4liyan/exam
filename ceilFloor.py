x = int(input())

li = [3, 7, 5, 11, 7, 9]
li.sort()

floor = 0
ceil = 0

if x in li:
    print("floor: ", x)
    print("ceil: ", x)
else:
    L = 0
    R = len(li)-1
    while (L <= R):
        mid = int((L + R)/2)
        item = li[mid]
        if x > item:
            L = mid+1
        elif x < item:
            R = mid-1
    if x < li[mid]:
        ceil = li[mid]
        floor = li[mid-1]
    else:
        ceil = li[mid-1]
        floor = li[mid]
    print("floor: ", floor)
    print("ceil: ", ceil)
