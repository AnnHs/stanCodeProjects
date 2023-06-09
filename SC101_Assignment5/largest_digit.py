"""
File: largest_digit.py
Name: Ann
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: int, the biggest digit
	"""
	if n < 0:
		n = -n
	last_digit = n % 10
	second_last_digit = (n//10) % 10

	if second_last_digit == 0:
		return last_digit
	elif second_last_digit >= last_digit:
		return find_largest_digit(n//10)
	else:
		return find_largest_digit(n//10 - second_last_digit + last_digit)


if __name__ == '__main__':
	main()
