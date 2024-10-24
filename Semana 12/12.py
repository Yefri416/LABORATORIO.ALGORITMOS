def insertion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i-1
        while j>=0 and arr[j] < clave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = clave
        
nombres = ["Yefri", "Sebastian", "Diego", "Paolo", "Fernando"]
insertion_sort(nombres)
print("Con insertion sort: ",nombres)