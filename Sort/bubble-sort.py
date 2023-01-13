def bubble(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)


bubble([6,4,3,2,7,9],6)