import robby 
import random as rn

# rw.demo(rw.strategyM)

class organism:
	def __init__(self, genes):
		self.genome = [rn.randint(0, 6) for x in xrange(genes)]
		self.fit = 0
	def fitness(self):
		fs = [0 for x in xrange(100)]
		for i in xrange(100):
			rw = robby.World(10, 10)
			for j in xrange(steps):
				perc = rw.getPerceptCode()
				reward = rw.performAction(robby.POSSIBLE_ACTIONS[self.genome[perc]])
				fs[i] += reward
		return sum(fs)/100
			

class population:
	def __init__(self, size, steps, crossover, mutation, generations):
		self.orgs = [organism(243) for x in xrange(size)]
		self.size = size
		self.steps = steps
		self.mutation = mutation
		self.crossover = crossover
		self.generations = generations
	
	def sortByFitness(self): 
		tuples = [(o.fitness(), o) for o in orgs] 
		tuples.sort() 
		sortedFitnessValues = [f for (f, o) in tuples] 
		sortedOrgs = [o for (f, o) in tuples] 
		return sortedOrgs, sortedFitnessValues



