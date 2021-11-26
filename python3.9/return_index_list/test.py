import unittest
from return_list_index_test import *

class test_1(unittest.TestCase):
	"""Функция тестирования. Сверка возвращаемого индекса, под которым находится число в списке"""
	def test(self):
		self.assertEqual(func_find_list(my_list, guess_number), 4)

if __name__ == '__main__':
    unittest.main()
