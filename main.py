from __future__ import print_function

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
                global rw
		fs = [0 for x in range(iterations)]
		for i in range(iterations):
                        # reset cans and robby position
			rw.distributeCans()
			rw.goto(0,0)
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
	def __init__(self, genome_size, size, steps, crossover, mutation, generation_limit):
		self.orgs = [organism(genome_size, crossover, mutation) for x in range(size)]
		self.size = size
		self.steps = steps
		# self.mutation = mutation
		# self.crossover = crossover
		self.generation_limit = generation_limit
		self.generation = 0
	
	def sort_by_fitness(self): 
		tuples = [(o.fitness(100, self.steps), o) for o in self.orgs] 
		tuples.sort() 
		sorted_fitness_values = [f for (f, o) in tuples] 
		sorted_orgs = [o for (f, o) in tuples] 
		return (sorted_orgs, sorted_fitness_values)

	def mating(self):
                global output
		if(self.generation < self.generation_limit):
			(sorting, sorted_fitness) = self.sort_by_fitness()
			# Every 10 generations, print generation data
			if (self.generation % 10 == 9):
                                print(self.generation, end=' ', file=output) # generation number
                                print(sum(sorted_fitness) / len(sorted_fitness), end=' ', file=output) # average fitness
                                print(sorted_fitness[len(sorted_fitness)-1], end=' ', file=output) # fitness of best organism
                                print(''.join([str(elem) for elem in sorting[0].genome]), end='\n', file=output) # best organism
                                
			print('Now mating for generation ', self.generation)
			
			probs = [float(i)/self.size for i in range(1, self.size+1)]
			chances = [rn.random() for x in range(self.size)]
			parents = [sorting[i] if (chances[i] <= probs[i]) else None for i in range(self.size)]
			parents = filter(lambda x: x != None, parents)
			if(len(parents) % 2 == 1):
				parents.pop(0)
			pairs = [(parents[i], parents[i+1]) for i in range(0, len(parents) - 2, 2)]
			pairs = pairs[::-1]

			children = []
			
			for (mom, dad) in pairs:
				(son, daughter) = mom.reproduce(dad)
				children.append(son)
				children.append(daughter)
				
			num_children = len(children)

			while(num_children < self.size):
				new_probs = [float(i)/len(parents) for i in range(1, len(parents)+1)]
				new_chances = [rn.random() for x in range(len(parents))]
				new_parents = [sorting[i] if (chances[i] <= probs[i]) else None for i in range(len(parents))]
				new_parents = filter(lambda x: x != None, new_parents)
				new_pairs = [(new_parents[i], new_parents[i+1]) for i in range(0, len(new_parents) - 2, 2)]
				new_pairs = new_pairs[::-1]
				
				for (mom, dad) in new_pairs:
					if(num_children >= self.size):
						break
					(son, daughter) = mom.reproduce(dad)
					num_children += 2
					children.append(son)
					children.append(daughter)
			
			if(num_children > self.size):
				children[self.size:] = []
			# increment generation
			self.orgs = children
			self.generation = self.generation + 1
			

def main():
        global rw, output
        rw = robby.World(10, 10) # Robby code expects a single global world, otherwise it keeps making new windows
        output = open('GAoutput.txt', 'w')
        generations = 20
        pop_size = 100
        steps = 20
        pop = population(243, pop_size, steps, -1, -1, generations)
        # Turn off graphics
        rw.graphicsOff()
        # Run algorithm for given generations
        for i in range(generations):
                pop.mating()
        print('Genetic algorithm completed!')

# Call main
main()
