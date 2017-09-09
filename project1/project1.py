#!/usr/bin/python

#LAB PROJECT 1: HOW RANDOM IS RANDOM?


#PART A: CREATE RANDOM NUMBER SEQUENCES:

#A-i:
import Ben_Johnston_Classes as MY
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 
from scipy.stats import chisquare
import random

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
class RANDOM_JVN_NUMBER:
	def __init__(self, seed_input):
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

Random_JvN_1_seedarray = RANDOM_JVN_NUMBER(101011).random_JvN
Random_JvN_2_seedarray = RANDOM_JVN_NUMBER(676767).random_JvN
Random_JvN_3_seedarray = RANDOM_JVN_NUMBER(989812).random_JvN

# if len(str(Random_JvN_1_seedarray)) != 6: #Testing to see if the code breaks. If so, it will be fixed in A-iii.
# 	print "There are less than 6 digits in one of your seeds."
# 	for number in Random_JvN_1_seedarray:
# 		number = 123456
# if len(Random_JvN_1_seedarray) != len(set(Random_JvN_1_seedarray)):
#     print "There are duplicates in your random number set. Try a different seed."



#PART B: TEST RANDOM NUMBER SEQUENCES:

#B-i:
MY.RANDOM_PLOT(0,1,1000, seed_1, random_1, 'A', 'Plot A of random numbers (np.random.uniform)', 'Random_uniform_1.png')
MY.RANDOM_PLOT(0,1,1000, seed_2, random_2, 'B', 'Plot B of random numbers (np.random.uniform)', 'Random_uniform_2.png')
MY.RANDOM_PLOT(0,1,1000, seed_3, random_3, 'C', 'Plot C of random numbers (np.random.uniform)', 'Random_uniform_3.png')
Random_JvN_1 = MY.RANDOM_JVN_PLOT(101011, Random_JvN_1_seedarray, 'Plot D, using JvN', 'X Values', 'Y Values', 'D', 'Random_JvN_1.png')
Random_JvN_2 = MY.RANDOM_JVN_PLOT(676767, Random_JvN_2_seedarray, 'Plot E, using JvN', 'X Values', 'Y Values', 'E', 'Random_JvN_2.png')
Random_JvN_3 = MY.RANDOM_JVN_PLOT(989812, Random_JvN_3_seedarray, 'Plot F, using JvN', 'X Values', 'Y Values', 'F', 'Random_JvN_3.png')


#B-ii:
cl_hist = ['k', 'r', 'b', 'y', 'c', 'g', 3, 10, 45, 89, 65, 50]

MY.RANDOM_HIST(random_1, cl_hist[0], 0.1, 'Plot A,rwidth=0.1', 'A', 'Random_uniform_hist_1.png')
MY.RANDOM_HIST(random_1, cl_hist[1], 0.025, 'Plot A,rwidth=0.025', 'A', 'Random_uniform_hist_2.png')
MY.RANDOM_HIST(random_2, cl_hist[0], 0.1, 'Plot B,rwidth=0.1', 'B', 'Random_uniform_hist_3.png')
MY.RANDOM_HIST(random_2, cl_hist[1], 0.025, 'Plot B,rwidth=0.025', 'B', 'Random_uniform_hist_4.png')
MY.RANDOM_HIST(random_3, cl_hist[0], 0.1, 'Plot C,rwidth=0.1', 'C', 'Random_uniform_hist_5.png')
MY.RANDOM_HIST(random_3, cl_hist[1], 0.025, 'Plot C,rwidth=0.025', 'C', 'Random_uniform_hist_6.png')

MY.RANDOM_HIST(Random_JvN_1_seedarray, cl_hist[0], 0.1, 'Plot D,rwidth=0.1', 'D', 'Random_JvN_hist_1.png')
MY.RANDOM_HIST(Random_JvN_1_seedarray, cl_hist[3], 0.025, 'Plot D,rwidth=0.025', 'D', 'Random_JvN_hist_2.png')
MY.RANDOM_HIST(Random_JvN_2_seedarray, cl_hist[0], 0.1, 'Plot F,rwidth=0.1', 'E', 'Random_JvN_hist_3.png')
MY.RANDOM_HIST(Random_JvN_2_seedarray, cl_hist[3], 0.025, 'Plot F,rwidth=0.025', 'E', 'Random_JvN_hist_4.png')
MY.RANDOM_HIST(Random_JvN_3_seedarray, cl_hist[0], 0.1, 'Plot G,rwidth=0.1', 'F', 'Random_JvN_hist_5.png')
MY.RANDOM_HIST(Random_JvN_3_seedarray, cl_hist[3], 0.025, 'Plot G,rwidth=0.025', 'F', 'Random_JvN_hist_6.png')


#B-iii-a-i:
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

n4_10, bins4_40, patches4_100 = plt.hist(Random_JvN_1_seedarray, bins=10)
n4_40, bins4_40, patches4_40 = plt.hist(Random_JvN_1_seedarray, bins=40)
n4_100, bins4_100, patches4_100 = plt.hist(Random_JvN_1_seedarray, bins=100)

n5_10, bins5_10, patches5_10 = plt.hist(Random_JvN_2_seedarray, bins=10)
n5_40, bins5_40, patches5_40 = plt.hist(Random_JvN_2_seedarray, bins=40)
n5_100, bins5_100, patches5_100 = plt.hist(Random_JvN_2_seedarray, bins=100)

n6_10, bins6_10, patches6_10 = plt.hist(Random_JvN_3_seedarray, bins=10)
n6_40, bins6_40, patches6_40 = plt.hist(Random_JvN_3_seedarray, bins=40)
n6_100, bins6_100, patches6_100 = plt.hist(Random_JvN_3_seedarray, bins=100)

print 'Chi, P value for random_1, bins=10:  {}'.format(MY.CHI(n1_10, 100))
print 'Chi, P value for random_1, bins=40:  {} \n'.format(MY.CHI(n1_40, 25))
print 'Chi, P value for random_1, bins=100:  {} \n'.format(MY.CHI(n1_100, 10))
print 'Chi, P value for random_2, bins=10:  {} \n'.format(MY.CHI(n2_10, 100))
print 'Chi, P value for random_2, bins=40:  {} \n'.format(MY.CHI(n2_40, 25))
print 'Chi, P value for random_2, bins=100:  {} \n'.format(MY.CHI(n2_100, 10))
print 'Chi, P value for random_3, bins=10:  {} \n'.format(MY.CHI(n3_10, 100))
print 'Chi, P value for random_3, bins=40:  {} \n'.format(MY.CHI(n3_40, 25))
print 'Chi, P value for random_3, bins=100:  {} \n'.format(MY.CHI(n3_100, 10))
print 'Chi, P value for random_1_JvN, bins=10:  {} \n'.format(MY.CHI(n4_10, 100))
print 'Chi, P value for random_1_JvN, bins=40:  {} \n'.format(MY.CHI(n4_40, 25))
print 'Chi, P value for random_1_JvN, bins=100:  {} \n'.format(MY.CHI(n4_100, 10))
print 'Chi, P value for random_2_JvN, bins=10:  {} \n'.format(MY.CHI(n5_10, 100))
print 'Chi, P value for random_2_JvN, bins=40:  {} \n'.format(MY.CHI(n5_40, 25))
print 'Chi, P value for random_2_JvN, bins=100:  {} \n'.format(MY.CHI(n5_100, 10))
print 'Chi, P value for random_3_JvN, bins=10:  {} \n'.format(MY.CHI(n6_10, 100))
print 'Chi, P value for random_3_JvN, bins=40:  {} \n'.format(MY.CHI(n6_40, 25))
print 'Chi, P value for random_3_JvN, bins=100:  {}'.format(MY.CHI(n6_100, 10))


#B-iii-a-ii:
#Discussed in write-up


#B-iii-b-i:
class COUNTER:
	def __init__(self, seed_array, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9, bin10):
		n1_n2_in_bin_1 = 0
		n1_n2_in_bin_2 = 0
		n1_n2_in_bin_3 = 0
		n1_n2_in_bin_4 = 0
		n1_n2_in_bin_5 = 0
		n1_n2_in_bin_6 = 0
		n1_n2_in_bin_7 = 0
		n1_n2_in_bin_8 = 0
		n1_n2_in_bin_9 = 0
		n1_n2_in_bin_10 = 0
		n=999
		counter = []
		for i in range(0,n):
			counter.append(tuple(seed_array[0+i:2+i]))
		counter = np.array(counter)
		for (n1,n2) in counter:
			if ((n1 >= bin2[0]) and (n1 <= bin2[1])) and ((n2 >= bin1[0]) and (n2 <= bin1[1])):
				n1_n2_in_bin_1 += 1
			if ((n1 >= bin2[0]) and (n1 <= bin2[1])) and ((n2 >= bin2[0]) and (n2 <= bin2[1])):
				n1_n2_in_bin_2 += 1
			if ((n1 >= bin3[0]) and (n1 <= bin3[1])) and ((n2 >= bin3[0]) and (n2 <= bin3[1])):
				n1_n2_in_bin_3 += 1
			if ((n1 >= bin4[0]) and (n1 <= bin4[1])) and ((n2 >= bin4[0]) and (n2 <= bin4[1])):
				n1_n2_in_bin_4 += 1
			if ((n1 >= bin5[0]) and (n1 <= bin5[1])) and ((n2 >= bin5[0]) and (n2 <= bin5[1])):
				n1_n2_in_bin_5 += 1
			if ((n1 >= bin6[0]) and (n1 <= bin6[1])) and ((n2 >= bin6[0]) and (n2 <= bin6[1])):
				n1_n2_in_bin_6 += 1
			if ((n1 >= bin7[0]) and (n1 <= bin7[1])) and ((n2 >= bin7[0]) and (n2 <= bin7[1])):
				n1_n2_in_bin_7 += 1
			if ((n1 >= bin8[0]) and (n1 <= bin8[1])) and ((n2 >= bin8[0]) and (n2 <= bin8[1])):
				n1_n2_in_bin_8 += 1
			if ((n1 >= bin9[0]) and (n1 <= bin9[1])) and ((n2 >= bin9[0]) and (n2 <= bin9[1])):
				n1_n2_in_bin_9 += 1
			if ((n1 >= bin2[0]) and (n1 <= bin10[1])) and ((n2 >= bin10[0]) and (n2 <= bin10[1])):
				n1_n2_in_bin_10 += 1
		print 'n1 and n2 are bin 1: {}'.format(n1_n2_in_bin_1)
		print 'n1 and n2 are bin 2: {}'.format(n1_n2_in_bin_2)
		print 'n1 and n2 are bin 3: {}'.format(n1_n2_in_bin_3)
		print 'n1 and n2 are bin 4: {}'.format(n1_n2_in_bin_4)
		print 'n1 and n2 are bin 5: {}'.format(n1_n2_in_bin_5)
		print 'n1 and n2 are bin 6: {}'.format(n1_n2_in_bin_6)
		print 'n1 and n2 are bin 7: {}'.format(n1_n2_in_bin_7)
		print 'n1 and n2 are bin 8: {}'.format(n1_n2_in_bin_8)
		print 'n1 and n2 are bin 9: {}'.format(n1_n2_in_bin_9)
		print 'n1 and n2 are bin 10: {}'.format(n1_n2_in_bin_10)
bin1 = 0.001997,  0.1017897
bin2 = 0.1017897, 0.2015824
bin3 = 0.2015824, 0.3013751
bin4 = 0.3013751, 0.4011678
bin5 = 0.4011678, 0.5009605
bin6 = 0.5009605, 0.6007532
bin7 = 0.6007532, 0.7005459
bin8 = 0.7005459, 0.8003386
bin9 = 0.8003386, 0.9001313
bin10 = 0.9001313, 0.999924

JvN_1_hist_01, bins1 = np.histogram(Random_JvN_1_seedarray, bins=10)
JvN_2_hist_02, bins2 = np.histogram(Random_JvN_2_seedarray, bins=10)
JvN_3_hist_03, bins3 = np.histogram(Random_JvN_3_seedarray, bins=10)
print 'JvN 100-element array #1: '
COUNTER(Random_JvN_1_seedarray, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9, bin10)
print '\n \n JvN 100-element array #2: '
COUNTER(Random_JvN_2_seedarray, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9, bin10)
print '\n \n JvN 100-element array #3: '
COUNTER(Random_JvN_3_seedarray, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9, bin10)


#B-iii-b-ii:
