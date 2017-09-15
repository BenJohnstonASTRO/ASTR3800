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
			print 'The null hypothesis is accepted with 0.95 certainty.'
class CHI2:
	def __init__(self, bin_array, expected, upper_lim, lower_lim, array_name):
		for i in range(lower_lim, upper_lim):
			chi = np.sum(((bin_array[i]-expected)**2/expected))
		print '\n Chi square comparison for {}:'.format(array_name)
		print chi


#PROJECT 2:
