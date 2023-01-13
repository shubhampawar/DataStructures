def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] + quick_sort([e for e in l[1:] if e > l[0]])

        # print([e for e in l[1:] if e <= l[0]], "----", [l[0]], "-----", [e for e in l[1:] if e > l[0]])
        # print([e for e in l[1:] if e <= l[0]] + [l[0]] + [e for e in l[1:] if e > l[0]])
        # return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] + quick_sort([e for e in l[1:] if e > l[0]])


print(quick_sort([4, 1, 2, 7, 6, 9, 8,1,1,1,14,4,4,4,5,5,5,5,6,6,6]))
