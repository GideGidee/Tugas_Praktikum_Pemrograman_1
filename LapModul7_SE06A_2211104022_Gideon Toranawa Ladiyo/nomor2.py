def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

anggota = ['Zhafira', 'Nirmala', 'Aksara', 'Nalendra', 'Cakra', 'Sastra', 'Agni', 'Bagas', 'Jerome', 'Kiara']
print("Before :", anggota)
anggota_sort = selection_sort(anggota)
print("After :", anggota_sort)