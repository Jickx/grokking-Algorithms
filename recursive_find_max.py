def find_max(list):
    if len(list) == 1:
        return list[0]
    else:
        max_item = find_max(list[1:])
        return max_item if max_item > list[0] else list[0]

assert find_max([1,2,300,4,5,6,7,8]) == 300
assert find_max([1,2,-300,4,50,6,7,8]) == 50