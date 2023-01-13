'''
25

0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25

'''


def root(num):
    s = 0
    e = num
    mid = s + (e - s) // 2

    while (s <= e):
        # print(f"start {s},end {e}, mid {mid}")
        # print(mid)
        if mid * mid == num:
            return mid

        elif mid * mid < num:
            ans = mid
            s = mid + 1
            # print("start",s)
        else:
            e = mid - 1

        mid = s + (e - s) // 2
    return ans


def root_decimal(num, int_num, precision):
    factor = 10
    for _ in range(precision):
        for i in range(10):
            i/=factor
            int_num+=i
            print(int_num*int_num)
            if int_num*int_num > num:
                pass
            else:
                ans = int_num
        factor*=10
    print(ans)


num = 37

int_num = (root(num))
print("int_val", int_num)
root_decimal(num, int_num, 3)
