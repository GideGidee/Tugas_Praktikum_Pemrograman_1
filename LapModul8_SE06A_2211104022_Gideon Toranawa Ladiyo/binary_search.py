def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def binary_search(keyword, data):
    sort_data = bubble_sort(data)
    print(f"data sorted = {sort_data}")
    left = 0
    right = len(sort_data) - 1
    while left <= right:
        mid = (left + right)//2
        str_data = sort_data[mid]
        if str_data > keyword:
            right = mid - 1
        elif str_data < keyword:
            left = mid + 1
        else:
            print(f"keyword {keyword} has been found at index {mid}")
            return mid

    print(f"keyword {keyword} not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
keyword = int(input("Input keyword: "))
binary_search(keyword, data)
