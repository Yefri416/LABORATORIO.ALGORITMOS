def merge_sort(tuplas):
    if len(tuplas) > 1:
        mid = len(tuplas) // 2
        L = tuplas[:mid]
        R = tuplas[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1] or (L[i][1] == R[j][1] and L[i][0] < R[j][0]):
                tuplas[k] = L[i]
                i += 1
            else:
                tuplas[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tuplas[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tuplas[k] = R[j]
            j += 1
            k += 1

personas = [("Juan", 30), ("Ana", 25), ("Luis", 20)]
merge_sort(personas)
print(personas)