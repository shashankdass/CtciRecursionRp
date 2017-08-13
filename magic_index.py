def find_magic_index(arr, start, end):
    def find_next(val, index, forward=True):
        if forward:
            while index < len(arr) and arr[index] == val:
                index += 1
        else:
            while index >= 0 and arr[index] == val:
                index -= 1
        return index

    if start > end:
        return None
    mid = start + (end - start) // 2
    if mid == arr[mid]:
        return mid
    elif mid > arr[mid]:
        index = find_next(arr[mid], mid)
        return find_magic_index(arr, index, end)
    else:
        index = find_next(arr[mid], mid, forward=False)
        return find_magic_index(arr, start, index)


arr = [-2, -1, 0, 0, 4]
print(find_magic_index(arr, 0, len(arr) - 1))
