def get_all_set_bit_val(arr, num):
    count = 0
    ret = []
    while num:
        if num & 1:
            ret.append(arr[count])
        num >>= 1
        count += 1
    return ret


def get_all_set(arr):
    len_arr = len(arr)
    final_set = []
    for i in range(1, 2 ** len_arr):
        final_set.append(get_all_set_bit_val(arr, i))
    return final_set


def get_all_set_rec(arr, index):
    ret_set = []
    if index < 0:
        ret_set.append(set())
        return ret_set
    this_set = get_all_set_rec(arr, index - 1)
    for s in this_set:
        ret_set.append(s)
        update_set = s.copy()  # don't forget to copy.. ever.. for mutable date types list or set.
        update_set.add(arr[index])
        ret_set.append(update_set)
    return ret_set


ar = [1, 2, 3]
# print(get_all_set(ar))
print(get_all_set_rec(ar, len(ar) - 1))
