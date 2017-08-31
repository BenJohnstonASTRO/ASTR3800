import numpy as np
import matplotlib.pyplot as plt 

heads = 1
tails = 0
number_tosses = 10 #Set the total number of tosses
seed = 100 #Set the initial seed
np.random.seed(seed) #Generate the seed
generate = np.random.uniform(low=0, high=1, size=number_tosses) #Generate the 10 numbers between 0 and 1
total_tosses = []
for number in generate:
	if number < 0.5: #Based on the random number, categorize the heads or tails.
		total_tosses.append('Heads: {}'.format(heads))
	if number >= 0.5:
		total_tosses.append('Tails: {}'.format(tails))
print total_tosses