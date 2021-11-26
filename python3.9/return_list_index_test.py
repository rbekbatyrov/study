import unittest

def func_find_list(list, number):
	list.sort()
	for i in list:
		if number == list[i]:
			return i
	# return list, number

my_list = [1, 4, 3, 2, 5]
guess_number = 5

class test_1(unittest.TestCase):
	"""docstring for test_1"""
	def test(self):
		self.assertEqual(func_find_list(my_list, guess_number), 4)
		

if __name__ == '__main__':
    unittest.main()
# out_list = func_find_list(my_list, guess_number)
# print(out_list)
