def binary_serch(list, item):
	low = 0
	high = len(list)-1

	while low <= high:
		mid = (low + high)//2
		guess = list[mid]
		# print(low)
		# print(high)
		# print(mid)
		print(guess)
		if guess == item:
			return guess
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	print(i)
	return None

my_list = [1, 3, 5, 7, 9]
print(binary_serch(my_list, 9))

# print("---")
# var = (1 + 1)//2
# print(var)
