#!/usr/bin/python

#PROJECT 1:
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 
from scipy.stats import chisquare
import random
class RANDOM_PLOT: #Plots 3 random number graphs per figure (or page).
	def __init__(self, low_limit, high_limit, size, sd1, random, lb1, title, save):
		plt.figure(figsize=(18,12))
		plt.title('Random Number graphs')
		plt.plot(random, label=lb1)
		plt.legend()
		plt.title(title)
		plt.xlabel('X values')
		plt.ylabel('Y values')
		plt.savefig(save, dpi=300)
		# plt.show()
class RANDOM_JVN_PLOT: #Plots the John von Nuemann method for random numbers, starting with a different seed for every loop
	def __init__(self, seed_input, random_input, title, xlabel, ylabel, label, save):
		plt.figure(figsize=(18,12))
		plt.plot(random_input, label=label)
		plt.legend()
		plt.title(title)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.savefig(save, dpi=300)
		# plt.show()
class RANDOM_HIST: #plots the histograms of each random number set
	def __init__(self, rand1, color1, bins, title_str, lb1, save):
		plt.figure(figsize=(18,12))
		plt.title(title_str)
		plt.hist(rand1, color=color1, bins=bins, label=lb1)
		plt.legend()
		plt.xlabel('Random Numbers')
		plt.ylabel('Frequency')
		plt.savefig(save, dpi=300)
		# plt.show()

class RANDOM_UNIFORM_ALL:
	def __init__(self, set1, set2, set3, name, title, lb1, lb2, lb3, bin_input):
		plt.figure(figsize=(18,12))
		plt.title(title)
		plt.hist(set1, zorder=3, label=lb1, bins=bin_input)
		plt.hist(set2, zorder=1, label=lb2, bins=bin_input)
		plt.hist(set3, zorder=2, label=lb3, bins=bin_input)
		plt.ylabel('Frequency')
		plt.xlabel('Random numbers')
		plt.legend()
		plt.savefig(name, dpi=300)
class RANDOM_JVN_ALL:
	def __init__(self, set1, set2, set3, name, title, lb1, lb2, lb3, bin_input):
		plt.figure(figsize=(18,12))
		plt.title(title)
		plt.hist(set1, zorder=3, label=lb1, bins=bin_input)
		plt.hist(set2, zorder=1, label=lb2, bins=bin_input)
		plt.hist(set3, zorder=2, label=lb3, bins=bin_input)
		plt.ylabel('Frequency')
		plt.xlabel('Random numbers')
		plt.legend()
		plt.savefig(name, dpi=300)
class CHI:
	def __init__(self, obs, exp):
		chi2, p_value = chisquare(obs, exp)
		print 'Chi-Square value: {}'.format(chi2)
		print 'P value: {}'.format(p_value)
		if p_value < 0.05:
			print 'The p-value is below 0.05.'
		if p_value >= 0.05:
			print 'The null hypothesis is accepted with %d%% certainty.' % (p_value*100)
class CHI2:
	def __init__(self, bin_array, expected, upper_lim, lower_lim, array_name):
		for i in range(lower_lim, upper_lim):
			chi = np.sum(((bin_array[i]-expected)**2/expected))
		print '\n Chi square comparison for {}:'.format(array_name)
		print chi

class GENERATOR: #Generates a new seed using the John von Nuemann method
	def __init__(self, sd):
		sq = sd**2
		self.sq = str(sq)
		cut = []
		for item in self.sq:
			cut.append(item)
		new = len(cut)/2
		seed_new = cut[new-3:new+3]
		self.seed_new = ''.join(seed_new)
		self.seed_new = int(self.seed_new)
class RANDOM_JVN_NUMBER:
	def __init__(self, seed_input):
		seed = seed_input
		self.random_JvN = np.zeros(1000)
		for i in range(0,1000):
			sd1 = GENERATOR(seed).seed_new
			while sd1 in self.random_JvN:
				sd1 = GENERATOR(np.random.random_integers(1e5, 999999)).seed_new
			self.random_JvN[i] = sd1
			seed = sd1
		while True:
			while len(str(seed)) < 6 or seed in self.random_JvN:
				if len(str(seed)) < 6:
					seed = GENERATOR(np.random.random_integers(1e5, 999999)).seed_new
				if seed in self.random_JvN:
					seed = GENERATOR(np.random.random_integers(1e5, 999999)).seed_new
			seed = sd1
			break

		self.random_JvN /= 1e6
		if len(self.random_JvN) != len(set(self.random_JvN)):
		    print "There are duplicates in your random number set. Try a different seed."
		else:
			print 'There are no duplicates in your random number set.'
		if len(self.random_JvN) != len(set(self.random_JvN)):
			print 'A seed in the 1000-element JvN array is repeating'
		else:
			print 'There are no repeating numbers in the 1000-element JvN array'

class COUNTER:
	def __init__(self, seed_array):
		self.n1_n2_bin_1 = 0
		self.n1_n2_bin_2 = 0
		self.n1_n2_bin_3 = 0
		self.n1_n2_bin_4 = 0
		self.n1_n2_bin_5 = 0
		self.n1_n2_bin_6 = 0
		self.n1_n2_bin_7 = 0
		self.n1_n2_bin_8 = 0
		self.n1_n2_bin_9 = 0
		self.n1_n2_bin_10 = 0
		n = 999
		counter = []
		for i in range(0,n):
			counter.append(tuple(seed_array[0+i:2+i]))
		counter = np.array(counter)
		for (n1,n2) in counter:
			if (n1 >= 0 and n1 <= 0.1) and (n2 >= 0 and n2 <= 0.1):
				self.n1_n2_bin_1 += 1
			if (n1 >= 0.1 and n1 <= 0.2) and (n2 >= 0.1 and n2 <= 0.2):
				self.n1_n2_bin_2 += 1
			if (n1 >= 0.2 and n1 <= 0.3) and (n2 >= 0.2 and n2 <= 0.3):
				self.n1_n2_bin_3 += 1
			if (n1 >= 0.3 and n1 <= 0.4) and (n2 >= 0.3 and n2 <= 0.4):
				self.n1_n2_bin_4 += 1
			if (n1 >= 0.4 and n1 <= 0.5) and (n2 >= 0.4 and n2 <= 0.6):
				self.n1_n2_bin_5 += 1
			if (n1 >= 0.5 and n1 <= 0.6) and (n2 >= 0.5 and n2 <= 0.6):
				self.n1_n2_bin_6 += 1
			if (n1 >= 0.6 and n1 <= 0.7) and (n2 >= 0.6 and n2 <= 0.7):
				self.n1_n2_bin_7 += 1
			if (n1 >= 0.7 and n1 <= 0.8) and (n2 >= 0.7 and n2 <= 0.8):
				self.n1_n2_bin_8 += 1
			if (n1 >= 0.8 and n1 <= 0.9) and (n2 >= 0.8 and n2 <= 0.9):
				self.n1_n2_bin_9 += 1
			if (n1 >= 0.9 and n1 <= 1.0) and (n2 >= 0.9 and n2 <= 1.0):
				self.n1_n2_bin_10 += 1
			if (n1 >= 0 and n1 <= 0.1) and (n2 >= 0.1 and n2 <= 0.2):
				self.n1_n2_bin_1 += 1
			if (n1 >= 0.1 and n1 <= 0.2) and (n2 >= 0.2 and n2 <= 0.3):
				self.n1_n2_bin_2 += 1
			if (n1 >= 0.2 and n1 <= 0.3) and (n2 >= 0.3 and n2 <= 0.4):
				self.n1_n2_bin_3 += 1
			if (n1 >= 0.3 and n1 <= 0.4) and (n2 >= 0.4 and n2 <= 0.5):
				self.n1_n2_bin_4 += 1
			if (n1 >= 0.4 and n1 <= 0.5) and (n2 >= 0.5 and n2 <= 0.6):
				self.n1_n2_bin_5 += 1
			if (n1 >= 0.5 and n1 <= 0.6) and (n2 >= 0.6 and n2 <= 0.7):
				self.n1_n2_bin_6 += 1
			if (n1 >= 0.6 and n1 <= 0.7) and (n2 >= 0.7 and n2 <= 0.8):
				self.n1_n2_bin_7 += 1
			if (n1 >= 0.7 and n1 <= 0.8) and (n2 >= 0.8 and n2 <= 0.9):
				self.n1_n2_bin_8 += 1
			if (n1 >= 0.8 and n1 <= 0.9) and (n2 >= 0.9 and n2 <= 1.0):
				self.n1_n2_bin_9 += 1
			if (n1 >= 0.9 and n1 <= 1.0) and (n2 >= 0.9 and n2 <= 1.0):
				self.n1_n2_bin_10 += 1
		print 'n1 and n2 are bin 1: {}'.format(self.n1_n2_bin_1)
		print 'n1 and n2 are bin 2: {}'.format(self.n1_n2_bin_2)
		print 'n1 and n2 are bin 3: {}'.format(self.n1_n2_bin_3)
		print 'n1 and n2 are bin 4: {}'.format(self.n1_n2_bin_4)
		print 'n1 and n2 are bin 5: {}'.format(self.n1_n2_bin_5)
		print 'n1 and n2 are bin 6: {}'.format(self.n1_n2_bin_6)
		print 'n1 and n2 are bin 7: {}'.format(self.n1_n2_bin_7)
		print 'n1 and n2 are bin 8: {}'.format(self.n1_n2_bin_8)
		print 'n1 and n2 are bin 9: {}'.format(self.n1_n2_bin_9)
		print 'n1 and n2 are bin 10: {}'.format(self.n1_n2_bin_10)
		self.total = self.n1_n2_bin_1, self.n1_n2_bin_2, self.n1_n2_bin_3, self.n1_n2_bin_4, self.n1_n2_bin_5, self.n1_n2_bin_6, self.n1_n2_bin_7, self.n1_n2_bin_8, self.n1_n2_bin_9, self.n1_n2_bin_10
		expected = 100
		label = 'Bin_1', 'Bin_2', 'Bin_3', 'Bin_4', 'Bin_5', 'Bin_6', 'Bin_7', 'Bin_8', 'Bin_9', 'Bin_10'
		for i in range(0,10):
			print label[i]  
			print np.sum(((self.total[i]-expected)**2)/expected)

			

#PROJECT 2:
