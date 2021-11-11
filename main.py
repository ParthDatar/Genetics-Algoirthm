import robby 
import random as rn

# rw.demo(rw.strategyM)

class organism:
	def __init__(self, genome_size, crossover_rate, mutation_rate):
		self.genome = [rn.randint(0, 6) for x in range(genome_size)]
		self.fit = 0
		self.crossover_rate = crossover_rate
		self.mutation_rate = mutation_rate
		self.genome_size = genome_size
	
	def fitness(self, iterations, steps):
		fs = [0 for x in range(iterations)]
		for i in range(iterations):
			rw = robby.World(10, 10)
			for j in range(steps):
				perc = rw.getPerceptCode()
				reward = rw.performAction(robby.POSSIBLE_ACTIONS[self.genome[perc]])
				fs[i] += reward
		return sum(fs)/iterations
	
	def reproduce(self, partner):
		point = rn.randint(0, self.genome_size-1)
		chance = [rn.random() for x in range(self.genome_size)]
		son = organism(self.genome_size, self.crossover_rate, self.mutation_rate)
		daughter = organism(self.genome_size, self.crossover_rate, self.mutation_rate)
		
		for i in range(point):
			if(chance[i] <= self.crossover_rate):
				son.genome[i] = self.genome[i]
				daughter.genome[i] = partner.genome[i]
			else:
				son.genome[i] = partner.genome[i]
				daughter.genome[i] = self.genome[i]
		for j in range(point, self.genome_size):
			if(chance[j] <= self.crossover_rate):
				son.genome[j] = partner.genome[j]
				daughter.genome[j] = self.genome[j]
			else:
				son.genome[j] = self.genome[j]
				daughter.genome[j] = partner.genome[j]
		
		mut_chance = [rn.random() for x in range(self.genome_size)]
		son.genome = [son.genome[i] if (mut_chance[i] > self.mutation_rate) else rn.randint(0, 6) for i in range(self.genome_size)]
		daughter.genome = [daughter.genome[i] if (mut_chance[i] > self.mutation_rate) else rn.randint(0, 6) for i in range(self.genome_size)]

		return (son, daughter)

			

class population:
	def __init__(self, genome_size, size, steps, crossover, mutation, generations):
		self.orgs = [organism(genome_size, crossover, mutation) for x in range(size)]
		self.size = size
		self.steps = steps
		# self.mutation = mutation
		# self.crossover = crossover
		self.generations = generations
	
	def sortByFitness(self): 
		tuples = [(o.fitness(100, self.steps), o) for o in self.orgs] 
		tuples.sort() 
		sortedFitnessValues = [f for (f, o) in tuples] 
		sortedOrgs = [o for (f, o) in tuples] 
		return sortedOrgs, sortedFitnessValues



