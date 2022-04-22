def quicksearch(list):
	if len(list) < 2:
		return list
	pivot = list[0]
	left = [i for i in list[1:] if pivot >= i]
	right = [i for i in list[1:] if pivot < i]
	return quicksearch(left) + [pivot] + quicksearch(right)

print(quicksearch([2,3,1,10,-100,1]))