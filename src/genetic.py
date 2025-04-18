#This file was used for Genetic based comparison

import random

class GeneticStrandsSolver:
    def __init__(self, candidates, grid_rows, grid_cols, population_size=100, generations=1000, mutation_rate=0.1):
        self.grid_size = grid_rows * grid_cols
        self.candidates = [c for c in candidates if len(c) == 3]
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def fitness(self, chromosome):
        used_cells = set()
        score = 0
        for idx in chromosome:
            word, positions, s = self.candidates[idx]
            if any(p in used_cells for p in positions):
                return 0 
            used_cells.update(positions)
            score += s
        if len(used_cells) != self.grid_size:
            return 0
        return score

    def mutate(self, chromosome):
        if not chromosome:
            return chromosome 
        new_chrom = chromosome[:]
        if random.random() < self.mutation_rate:
            i = random.randint(0, len(new_chrom) - 1) if len(new_chrom) > 0 else 0 
            j = random.randint(0, len(self.candidates) - 1) if len(self.candidates) > 0 else 0  
            new_chrom[i] = j
        return new_chrom


    def crossover(self, parent1, parent2):
        if len(parent1) > 1 and len(parent2) > 1:
            cut = random.randint(1, min(len(parent1), len(parent2)) - 1)
            child = parent1[:cut] + [i for i in parent2 if i not in parent1[:cut]]
        else:
            child = parent1[:]
        return child


    def initial_population(self):
        population = []
        for _ in range(self.population_size):
            chrom = []
            used = set()
            random.shuffle(self.candidates)
            for i, (word, positions, s) in enumerate(self.candidates):
                if not any(p in used for p in positions):
                    chrom.append(i)
                    used.update(positions)
            population.append(chrom)
        return population

    def solve(self):
        population = self.initial_population()
        best_solution = []
        best_score = 0

        for gen in range(self.generations):
            scored_population = [(chrom, self.fitness(chrom)) for chrom in population]
            scored_population.sort(key=lambda x: -x[1])

            if scored_population[0][1] > best_score:
                best_solution = scored_population[0][0]
                best_score = scored_population[0][1]

            next_gen = [scored_population[0][0]]  
            while len(next_gen) < self.population_size:
                parents = random.choices(scored_population[:20], k=2)
                child = self.crossover(parents[0][0], parents[1][0])
                child = self.mutate(child)
                next_gen.append(child)

            population = next_gen

        return [self.candidates[i] for i in best_solution]
