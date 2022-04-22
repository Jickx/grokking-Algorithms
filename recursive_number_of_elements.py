def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

assert count([0,2,3,-4,'a',6,7]) == 7