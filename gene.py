import random
import numpy as np

target_sentence = "Hello, how are you!"
gene_pool = " ,!?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

population_size = 10


def generate_chromosome(length):
    genes = []
    while len(genes) < length:
        genes.append(gene_pool[random.randrange(0,len(gene_pool))])
    return ''.join(genes)


def calculate_fitness(chromosome):
    fitness = 0
    ctr = 0
    for i in chromosome:
        if i  == target_sentence[ctr]:
            fitness += 1
        ctr += 1
    return fitness


def mutate(chromosome):
    index_to_mutate = random.randrange(0, len(chromosome))
    gene = list(chromosome)
    mutated_gene = gene_pool[random.randrange(0, len(gene_pool))]
    gene[index_to_mutate] = mutated_gene
    return ''.join(gene)


def crossover(chromosome1, chromosome2):
    # Random Crossover
    gene1 = list(chromosome1)
    gene2 = list(chromosome2)
    for i in range(len(chromosome1)):
        if random.randint(0, 1) == 0:
            gene1[i], gene2[i] = gene2[i], gene1[i]
    return ''.join(gene1), ''.join(gene2)


population = []
for i in range(population_size):
    population.append(generate_chromosome(len(target_sentence)))

population_fitness = []
for chromosome in population:
    population_fitness.append(calculate_fitness(chromosome))

for generation in range(10000):
    # crossover
    if random.randint(0, 4) == 0:
        candidates = np.argpartition(population_fitness, -4)[-4:]
        chromosome1_index = candidates[random.randint(0, 3)]
        chromosome2_index = candidates[random.randint(0, 3)]
        print("Before Crossover", population[chromosome1_index], population[chromosome2_index])
        chromosome1, chromosome2 = crossover(population[chromosome1_index], population[chromosome2_index])
        population[chromosome1_index] = chromosome1
        population[chromosome2_index] = chromosome2
        print("After Crossover", population[chromosome1_index], population[chromosome2_index])

    # most of the time, only the worst change?
    parent_index = population_fitness.index(max(population_fitness))
    parent = population[parent_index]
    child = mutate(parent)

    print("Parent:", parent)
    print("Child:", child)

    child_fitness = calculate_fitness(child)
    print("Child Fitness", child_fitness)
    print("Current Fitness", population_fitness)

    index_to_delete = population_fitness.index(min(population_fitness))
    del population[index_to_delete]
    del population_fitness[index_to_delete]
    population.append(child)
    population_fitness.append(child_fitness)

    if child == target_sentence:
        print("Solution found at Generation:", generation)
        break
    # if child_fitness > len(target_sentence) - 5:
    #     print("Solution found at Generation:", generation)
    #     break


