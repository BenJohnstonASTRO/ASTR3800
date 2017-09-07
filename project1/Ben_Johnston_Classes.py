#!/usr/bin/python

#PROJECT 1:
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 
from scipy.stats import chisquare
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
class RANDOM_JVN_PLOT: #Plots the 1000 John von Nuemann seeds, starting with a different seed for every loop
	def __init__(self, seed_input, random_input, title, xlabel, ylabel, label, save):
		plt.figure(figsize=(18,12))
		plt.plot(random_input, label=label)
		plt.legend()
		plt.title(title)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.savefig(save, dpi=300)
		# plt.show()
class RANDOM_HIST: #Plots 4 random number histograms per figure (or page).
	def __init__(self, rand1, color1, rwidth, title_str, lb1, save):
		plt.figure(figsize=(18,12))
		plt.title(title_str)
		plt.hist(rand1, color=color1, rwidth=rwidth, label=lb1)
		plt.legend()
		plt.xlabel('Random Numbers')
		plt.ylabel('Frequency')
		plt.savefig(save, dpi=300)
		# plt.show()
class CHI:
	def __init__(self, obs, exp):
		chi2, p_value = chisquare(obs, exp)
		print 'Chi-Square value: {}'.format(chi2)
		print 'P value: {}'.format(p_value)


#PROJECT 2:
