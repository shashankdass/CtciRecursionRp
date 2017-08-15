def perm(arr, count):
    ret = []
    if count == len(arr) - 1:
        ret.append(arr[:])
        return ret
    for i in range(count, len(arr)):
        print(i, count)
        arr[i], arr[count] = arr[count], arr[i]  # swap each element with all the other elements
        ret.extend(perm(arr, count + 1))  # recurse for this arr arrangement
        arr[i], arr[count] = arr[count], arr[i]  # swap back each element
    return ret


arr = [1, 2, 3]
print(perm(arr, 0))
