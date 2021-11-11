import robby 
import random as rn

# rw.demo(rw.strategyM)

class organism:
	def __init__(self, genes):
		self.genome = [rn.randint(0, 6) for x in xrange(genes)]

class population:
	def __init__(self, size, steps, crossover, mutation, generations):
		self.genomes = [organism(243) for x in xrange(size)]
		self.size = size
		self.steps = steps
		self.mutation = mutation
		self.crossover = crossover
		self.generations = generations


	def fitness(genome):
		rw = robby.World(10, 10)
		for i in xrange(steps):
			p = rw.getPerceptCode()
			rw.performAction(robby.POSSIBLE_ACTIONS[genome[p]])
			
	

	def sortByFitness(self): 
		tuples = [(fitness(g), g) for g in genomes] 
		tuples.sort() 
		sortedFitnessValues = [f for (f, g) in tuples] 
		sortedGenomes = [g for (f, g) in tuples] 
		return sortedGenomes, sortedFitnessValues



