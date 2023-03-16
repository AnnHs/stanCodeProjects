"""
File: anagram.py
Name: Ann
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        s = input(str('Find anagrams for: '))
        start = time.time()
        if s == EXIT:
            break
        else:
            print('Searching...')
            anagrams = find_anagrams(s)
            print(f'{len(anagrams)} anagrams: {anagrams}')
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(file):
    dictionary = set()
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip('\n')
            dictionary.add(word)
    return dictionary


def find_anagrams(s):
    """
    :param s:str
    :return: list, anagrams of s
    """
    current_lst = []
    dictionary = read_dictionary(FILE)
    find_anagrams_helper(s, '', current_lst, dictionary, [])
    return current_lst


def find_anagrams_helper(s, current_s, current_lst, dictionary, index_lst):
    if len(s) == len(current_s) and (current_s in dictionary):
        print(f"Fond: {current_s}")
        current_lst.append(current_s)
        print('Searching...')
    else:
        for i in range(len(s)):
            if i not in index_lst:
                al = s[i]

                # choose
                current_s += al
                index_lst.append(i)

                # explore
                if has_prefix(current_s, dictionary) and current_s+al not in current_lst:
                    find_anagrams_helper(s, current_s, current_lst, dictionary, index_lst)

                # un-choose
                current_s = current_s[:-1]
                index_lst.pop()


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: str, trial of potential anagrams
    :param dictionary: list, dictionary
    :return: boolean, return True if sub_s is in dictionary
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False








if __name__ == '__main__':
    main()
