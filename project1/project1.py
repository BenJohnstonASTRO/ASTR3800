#LAB PROJECT 1: HOW RANDOM IS RANDOM?

#PART A:

#A-i:
import numpy as np
import matplotlib.pyplot as plt

seed_1 = 46128
np.random.seed(seed_1)
random_1 = np.random.uniform(low=0, high=1, size=1000)
seed_2 = 4993
np.random.seed(seed_2)
random_2 = np.random.uniform(low=0, high=1, size=1000)
seed_3 = 98123411
np.random.seed(seed_3)
random_3 = np.random.uniform(low=0, high=1, size=1000)


#A-ii and A-iii:
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

class RANDOM_JVN: #Plots the 1000 John von Nuemann seeds, starting with a different seed for every loop
	def __init__(self, seed_input, title, xlabel, ylabel, label, save):
		seed = seed_input
		self.random_JvN = np.zeros(1000)
		for i in range(0,1000):
			sd1 = GENERATOR(seed).seed_new
			self.random_JvN[i] = sd1
			seed = sd1
		if len(str(seed)) != 6: #Testing to see if the code breaks. If so, it will be fixed in A-iii.
			print "There are less than 6 digits in one of your seeds."
		self.random_JvN /= 1e6
		if len(self.random_JvN) != len(set(self.random_JvN)):
		    print "There are duplicates in your random number set. Try a different seed."
		else:
			print 'There are no duplicates in your random number set.'
		plt.figure(figsize=(18,12))
		plt.plot(self.random_JvN, label=label)
		plt.legend()
		plt.title(title)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.savefig(save, dpi=300)
	def JvN_numbers(self):
		return self.random_JvN


#B-i:
Random_JvN_1 = RANDOM_JVN(111111, 'Plot D, using JvN', 'X Values', 'Y Values', 'D', 'test1.png')
Random_JvN_2 = RANDOM_JVN(131311, 'Plot E, using JvN', 'X Values', 'Y Values', 'E', 'test2.png')
Random_JvN_3 = RANDOM_JVN(121212, 'Plot F, using JvN', 'X Values', 'Y Values', 'F', 'test3.png')
RANDOM_PLOT(0,1,1000, seed_1, random_1, 'A', 'Plot A of random numbers (np.random.uniform)', 'test4.png')
RANDOM_PLOT(0,1,1000, seed_2, random_2, 'B', 'Plot B of random numbers (np.random.uniform)', 'test5.png')
RANDOM_PLOT(0,1,1000, seed_3, random_3, 'C', 'Plot C of random numbers (np.random.uniform)', 'test6.png')


#B-ii:
class RANDOM_HIST: #Plots 4 random number histograms per figure (or page).
	def __init__(self, rand1, color1, rwidth, title_str, lb1, save):
		plt.figure(figsize=(18,12))
		plt.title(title_str)
		plt.hist(rand1, color=color1, rwidth=rwidth, label=lb1)
		plt.legend()
		plt.xlabel('Random Numbers')
		plt.ylabel('Frequency')
		plt.savefig(save, dpi=300)
cl_hist = ['k', 'r', 'b', 'y', 'c', 'g', 3, 10, 45, 89, 65, 50]

RANDOM_HIST(random_1, cl_hist[0], 0.1, 'Plot A,rwidth=0.1', 'A', 'test7.png')
RANDOM_HIST(random_1, cl_hist[1], 0.025, 'Plot A,rwidth=0.025', 'A', 'test8.png')
RANDOM_HIST(random_2, cl_hist[0], 0.1, 'Plot B,rwidth=0.1', 'B', 'test9.png')
RANDOM_HIST(random_2, cl_hist[1], 0.025, 'Plot B,rwidth=0.025', 'B', 'test10.png')
RANDOM_HIST(random_3, cl_hist[0], 0.1, 'Plot C,rwidth=0.1', 'C', 'test11.png')
RANDOM_HIST(random_3, cl_hist[1], 0.025, 'Plot C,rwidth=0.025', 'C', 'test12.png')

RANDOM_HIST(Random_JvN_1.JvN_numbers(), cl_hist[0], 0.1, 'Plot D,rwidth=0.1', 'D', 'test13.png')
RANDOM_HIST(Random_JvN_1.JvN_numbers(), cl_hist[3], 0.025, 'Plot D,rwidth=0.025', 'D', 'test14.png')
RANDOM_HIST(Random_JvN_2.JvN_numbers(), cl_hist[0], 0.1, 'Plot F,rwidth=0.1', 'E', 'test15.png')
RANDOM_HIST(Random_JvN_2.JvN_numbers(), cl_hist[3], 0.025, 'Plot F,rwidth=0.025', 'E', 'test16.png')
RANDOM_HIST(Random_JvN_3.JvN_numbers(), cl_hist[0], 0.1, 'Plot G,rwidth=0.1', 'F', 'test17.png')
RANDOM_HIST(Random_JvN_3.JvN_numbers(), cl_hist[3], 0.025, 'Plot G,rwidth=0.025', 'F', 'test18.png')


#B-iii:
#each variable named n{number} contains the value of the histogram, which is the observed value 
n1_10, bins1_10, patches1_10 = plt.hist(random_1, bins=10)
n1_40, bins1_40, patches1_40 = plt.hist(random_1, bins=40)
n1_100, bins1_100, patches1_100 = plt.hist(random_1, bins=100)

n2_10, bins2_10, patches2_10 = plt.hist(random_2, bins=10)
n2_40, bins2_40, patches2_40 = plt.hist(random_2, bins=40)
n2_100, bins2_100, patches2_100 = plt.hist(random_2, bins=100)

n3_10, bins3_10, patches3_10 = plt.hist(random_3, bins=10)
n3_40, bins3_40, patches3_40 = plt.hist(random_3, bins=40)
n3_100, bins3_100, patches3_100 = plt.hist(random_3, bins=100)

n4_10, bins4_10, patches4_10 = plt.hist(Random_JvN_1.JvN_numbers(), bins=10)
n4_40, bins4_40, patches4_40 = plt.hist(Random_JvN_1.JvN_numbers(), bins=40)
n4_100, bins4_100, patches4_100 = plt.hist(Random_JvN_1.JvN_numbers(), bins=100)

n5_10, bins5_10, patches5_10 = plt.hist(Random_JvN_2.JvN_numbers(), bins=10)
n5_40, bins5_40, patches5_40 = plt.hist(Random_JvN_2.JvN_numbers(), bins=40)
n5_100, bins5_100, patches5_100 = plt.hist(Random_JvN_2.JvN_numbers(), bins=100)

n6_10, bins6_10, patches6_10 = plt.hist(Random_JvN_3.JvN_numbers(), bins=10)
n6_40, bins6_40, patches6_40 = plt.hist(Random_JvN_3.JvN_numbers(), bins=40)
n6_100, bins6_100, patches6_100 = plt.hist(Random_JvN_3.JvN_numbers(), bins=100)

class CHI:
	def __init__(self, obs, exp):
		chi_square = np.sum(((obs-exp)**2/exp))
		print chi_square
chi_1_10 = CHI(n1_10, 100)
chi_1_40 = CHI(n1_40, 25)
chi_1_100 = CHI(n1_100, 10)
chi_2_10 = CHI(n2_10, 100)
chi_2_40 = CHI(n2_40, 25)
chi_2_100 = CHI(n2_100, 10)
chi_3_10 = CHI(n3_10, 100)
chi_3_40 = CHI(n3_40, 25)
chi_3_100 = CHI(n3_100, 10)
chi_4_10 = CHI(n4_10, 100)
chi_4_40 = CHI(n4_40, 25)
chi_4_100 = CHI(n4_100, 10)
chi_5_10 = CHI(n5_10, 100)
chi_5_40 = CHI(n5_40, 25)
chi_5_100 = CHI(n5_100, 10)
chi_6_10 = CHI(n6_10, 100)
chi_6_40 = CHI(n6_40, 25)
chi_6_100 = CHI(n6_100, 10)