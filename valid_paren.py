def valid_paren(right, left, cur, ret):
    # Base condition: if both are empty .. we reach a valid combo
    if right == 0 and left == 0:
        ret.append(''.join(cur[:]))
        return

    # add left parenthesis till we have them
    if left > 0:
        cur.append('(')
        valid_paren(right, left - 1, cur, ret)
        cur.pop()  # don't forget to pop

    # add right parenthesis till it is valid
    if right > left and right > 0:
        cur.append(')')
        valid_paren(right - 1, left, cur, ret)
        cur.pop()  # don't forget to pop

    return


ret = []
valid_paren(4, 4, [], ret)
print(ret)
