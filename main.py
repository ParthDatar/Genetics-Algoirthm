import robby 
rw = robby.World(10, 10)
import random as rn

# rw.demo(rw.strategyM)

class organism:
	def __init__(self):
		self.genome = [rn.randint(0, 6) for x in xrange(243)]
		self.score = 0



