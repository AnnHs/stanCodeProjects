"""
File: coin_flip_runs.py
Name: Ann
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	user decide number of runs.
	shows the process of coin flips.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	run = 0
	trial = ''
	i = 0
	while run != num_run:
		trial += r.choice('HT')
		i += 1
		if i > 2:
			if trial[i-1] == trial[i-2] != trial[i-3]:
				run += 1
		if i == 2:
			if trial[i-1] == trial[i-2] :
				run += 1
	print(trial)



# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
