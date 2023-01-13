def selectionSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n-1):
        for j in range(i+1,n):
            print(arr[i],arr[j],arr)
            if arr[i]> arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                continue
    print(arr)


selectionSort([8,4,2,1,3,9],6)