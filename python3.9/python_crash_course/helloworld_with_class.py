class hello_class():
	"""Простой класс с одним методом"""

	def hello_method():
		"""Метод возвращает текст"""
		return 'hello world!!!'

def main():
	"""Основная функция main, которая вызывает класс hello_class и метод hello_method"""
	out_list = hello_class.hello_method()
	print(out_list.title())

if __name__ == "__main__":
	main()
