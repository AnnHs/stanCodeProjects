"""
File: boggle.py
Name:Ann
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# constants
ROWS = 4
COLS = 4


def main():
	"""
	TODO:
	"""
	board = []
	for i in range(4):
		row = str(input(str(i + 1) + ' row of letters: ')).lower()
		if row[1] != ' ' or row[3] != ' ' or row[5] != ' ' and len(row) == 7:
			print('Illegal input')
			break
		row = row.split()
		board.append(row)
	dictionary = read_dictionary()
	start = time.time()
	####################
	found_word = set()
	visited = set()
	current_s = ''
	for i in range(ROWS):
		for j in range(COLS):
			find_words(i, j, board, current_s, visited, found_word, dictionary)
	count = len(found_word)
	print(f'There are {count} words in total')


	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = set()
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip('\n')
			dictionary.add(word)
	return dictionary


def find_words(r, c, board, current_s, visited, found_word, dictionary):
	if (current_s in dictionary) and (current_s not in found_word) and (len(current_s) >= 4):
		found_word.add(current_s)
		print(f'Found "{current_s}"')
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				new_r = i+r
				new_c = j+c
				if 0 <= new_r < 4 and 0 <= new_c < 4 and (new_r, new_c) not in visited:
					# choose
					current_s += board[new_r][new_c]
					visited.add((new_r, new_c))
					# explore
					if has_prefix(current_s, dictionary):
						find_words(new_r, new_c, board, current_s, visited, found_word, dictionary)
					# un-choose
					current_s = current_s[:-1]
					visited.remove((new_r, new_c))
		return found_word





	# else:
	# 	for i in range(-1, 2):
	# 		if 0 <= (r+i) < 4:
	# 			r += i
	# 			for j in range(-1, 2):
	# 				if 0 <= (c+j) < 4:
	# 					c += j
	# 					if (r, c) not in visited:
	# 						# choose
	# 						current_s += board[r][c]
	# 						visited.add((r, c))
	#
	# 						# explore
	# 						if has_prefix(current_s, dictionary):
	# 							find_words(r, c, board, current_s, visited, found_word, dictionary)
	#
	# 						# un-choose
	# 						current_s = current_s[:-1]
	# 						visited.remove((r, c))
	#return found_word


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: list, dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
