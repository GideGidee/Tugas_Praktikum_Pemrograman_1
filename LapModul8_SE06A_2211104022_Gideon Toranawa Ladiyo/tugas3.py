def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data

def binary_search(keyword, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right)//2
        if data[mid] > keyword:
            right = mid - 1
        elif data[mid] < keyword:
            left = mid + 1
        else:
            print(f"Keyword {keyword} has found in index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
keyword = int(input("Masukkan angka yang dicari: "))
data.sort()
result = binary_search(keyword, data)
