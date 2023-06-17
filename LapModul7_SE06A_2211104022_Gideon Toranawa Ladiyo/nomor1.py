def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

ips = [3.8, 2.9, 3.3, 4.0, 2.7]
print("List sebelum diurutkan :", ips)
ips_sort = bubble_sort(ips)
print("LIst setelah diurutkan :", ips_sort)