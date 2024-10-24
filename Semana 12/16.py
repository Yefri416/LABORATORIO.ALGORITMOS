def bubble_sort(arr):
    n = len(arr) -1
    for i in range(0, n):
        print(f"Pasada # {i+1}")
        
        for j in range(0, n):
            print(f"Comparacion: {arr[j]} > {arr[j+1]}.")
            
            if arr[j] > arr[j+1]:
                print(f"Intercambiar {arr[j]} x {arr[j+1]}.")
                
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
        print(f"Lista: {arr}")
        
    return arr
numeros = [23,45,54,25,90]
bubble_sort(numeros)
print(numeros)