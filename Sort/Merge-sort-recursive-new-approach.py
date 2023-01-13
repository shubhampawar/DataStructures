def merge(L,R):
    i=j=0
    result = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j += 1

    while(i<len(L)):
        result.append(L[i])
        i += 1
    while(j<len(R)):
        result.append(R[j])
        j += 1
    return result




def mergesort(arr):
    if len(arr)<=1:
        return arr

    else:
        mid = len(arr)//2
        L = mergesort(arr[:mid])
        R = mergesort(arr[mid:])
        return merge(L,R)


print(mergesort([7,5,3,1,3,2,1,9]))

assert mergesort([7,5,3,1,3,2,1,9]) == sorted([7,5,3,1,3,2,1,9])