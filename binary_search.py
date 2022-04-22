sorted_list = []
def binary_search(sorted_list, item):
    ctr = 0
    low, high = 0, len(sorted_list)-1
    while low <= high:
        mid = (low + high) // 2
        result = sorted_list[mid]
        if result == item:
            print(ctr)
            return 'Элемент найден'
        elif result < item:
            low = mid + 1
        elif result > item:
            high = mid -1
        ctr += 1
    print(ctr)
    return 'Элемент не найден'

for i in range(1, 257):
    sorted_list.append(i)

assert binary_search(sorted_list, 0) == 'Элемент не найден'
