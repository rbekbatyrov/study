#Переменные: список (массив) и загадываемое число
my_list = [1, 4, 3, 2, 5]
guess_number = 5

def func_find_list(list, number):
	"""Функция для возвращения индекса, под которым находится цифра"""
	list.sort()
	for i in list:
		if number == list[i]:
			return i
	# return list, number

def main():
	"""Основная функция main. Вызывает функцию func_find_list и передает ей спсиок и загадываемое число"""
	out_list = func_find_list(my_list, guess_number)
	print(out_list)

if __name__ == '__main__':
	main()
