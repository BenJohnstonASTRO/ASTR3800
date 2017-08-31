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
class GENERATOR:
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
seed_4 = GENERATOR(967615).seed_new
np.random.seed(seed_4)
random_4 = np.random.uniform(low=0, high=1, size=1000)*1e6
seed_5 = GENERATOR(seed_4).seed_new
np.random.seed(seed_5)
random_5 = np.random.uniform(low=0, high=1, size=1000)*1e6
seed_6 = GENERATOR(seed_5).seed_new
np.random.seed(seed_6)
random_6 = np.random.uniform(low=0, high=1, size=1000)*1e6

plt.plot(random_1, 'k.')
plt.plot(random_2, 'r.')
plt.plot(random_3, 'b.')
plt.plot(random_4, 'y.')
plt.plot(random_5, 'c.')
plt.plot(random_6, 'g.')
plt.show()

