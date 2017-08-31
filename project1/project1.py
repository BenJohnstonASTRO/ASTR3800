#LAB PROJECT 1: HOW RANDOM IS RANDOM?

#PART A:

#A-i:
import numpy as np
import matplotlib.pyplot as plt

seed_1 = 468
np.random.seed(seed_1)
random_1 = np.random.uniform(low=0, high=1, size=1000)
seed_2 = 498
np.random.seed(seed_2)
random_2 = np.random.uniform(low=0, high=1, size=1000)
seed_3 = 984
np.random.seed(seed_3)
random_3 = np.random.uniform(low=0, high=1, size=1000)

#A-ii:
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

class RANDOM_PLOT: #Plots a random number vs. number
	def __init__(self, low_limit, high_limit, size, seed_input, color):
		np.random.seed(seed_input)		
		random = np.random.uniform(low=low_limit, high=high_limit, size=size)
		colors = ['k.', 'r.', 'b.', 'y.', 'c.', 'g.', 'm.', ]
		color = colors[color]
		plt.figure()
		plt.plot(random, color)
		plt.show()


sd1 = GENERATOR(101011).seed_new
np.random.seed(sd1)
random_JvN1 = np.random.uniform(low=0, high=1e6, size=1000)
sd2 = GENERATOR(sd1).seed_new
np.random.seed(sd2)
random_JvN2 = np.random.uniform(low=0, high=1e6, size=1000)
sd3 = GENERATOR(sd2).seed_new
np.random.seed(sd3)
random_JvN3 = np.random.uniform(low=0, high=1e6, size=1000)


#A-iii:


#A-iv:
seed1 = 9713451
np.random.seed(seed1)
rand1 = np.random.uniform(low=0, high=64, size=1000)


plt.plot(ran
