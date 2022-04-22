def recursive_sum(item_list):
    if item_list == []:
        return 0
    return item_list[0] + recursive_sum(item_list[1:])


assert recursive_sum([1,2,3,4,5]) == 15
assert recursive_sum([2,3,4,-5]) == 4

        