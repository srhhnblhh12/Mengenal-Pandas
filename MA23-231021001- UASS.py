import random
import string
import time

start_time = time.time()

target = "PEMROGRAMAN LANJUTAN"
population_size = 100
mutation_rate = 0.04
generations = 10000
elite_size = 20
top_parents_size = 2  # Jumlah individu teratas yang akan dipertimbangkan sebagai orang tua

def initialize_population(size, length):
    return [''.join(random.choices(string.ascii_uppercase + " ", k=length)) for _ in range(size)]

def calculate_fitness(individual):
    return sum(1 for i, j in zip(individual, target) if i == j)

def selection(population, top_size):
    # Mengambil individu dengan fitness tertinggi
    top_individuals = population[:top_size]
    # Memilih dua orang tua secara acak dari individu dengan fitness tertinggi
    return random.sample(top_individuals, 2)

def crossover(parent1, parent2):
    length = len(parent1)
    
    crossover_points = sorted(random.sample(range(1, length), 4))
    
    child1 = (parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] +
              parent1[crossover_points[1]:crossover_points[2]] + parent2[crossover_points[2]:crossover_points[3]] +
              parent1[crossover_points[3]:])
    
    child2 = (parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] +
              parent2[crossover_points[1]:crossover_points[2]] + parent1[crossover_points[2]:crossover_points[3]] +
              parent2[crossover_points[3]:])
    
    child3 = (parent1[:crossover_points[1]] + parent2[crossover_points[1]:crossover_points[2]] +
              parent1[crossover_points[2]:crossover_points[3]] + parent2[crossover_points[3]:])
    
    child4 = (parent2[:crossover_points[1]] + parent1[crossover_points[1]:crossover_points[2]] +
              parent2[crossover_points[2]:crossover_points[3]] + parent1[crossover_points[3]:])
    
    child5 = (parent1[:crossover_points[2]] + parent2[crossover_points[2]:crossover_points[3]] +
              parent1[crossover_points[3]:])
    
    return child1, child2, child3, child4, child5

def mutate(individual, mutation_rate):
    return ''.join(
        char if random.random() > mutation_rate else random.choice(string.ascii_uppercase + " ")
        for char in individual
    )

def genetic_algorithm():
    population = initialize_population(population_size, len(target))
    for generation in range(generations):
        population = sorted(population, key=calculate_fitness, reverse=True)
        best_individual = population[0]
        best_fitness = calculate_fitness(best_individual)
        
        print(f"Generation {generation + 1}: Best fitness = {best_fitness}, Best individual = {best_individual}")
        
        if best_fitness == len(target):
            break
        
        next_population = population[:elite_size]  # Elitism: keep top individuals
        
        while len(next_population) < population_size:
            parent1, parent2 = selection(population, top_parents_size)  # Seleksi orang tua dari individu teratas
            child1, child2, child3, child4, child5 = crossover(parent1, parent2)
            next_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate), 
                                    mutate(child3, mutation_rate), mutate(child4, mutation_rate), 
                                    mutate(child5, mutation_rate)])
            next_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate), 
                                    mutate(child3, mutation_rate), mutate(child4, mutation_rate), 
                                    mutate(child5, mutation_rate)])                                         
        
        population = next_population[:population_size]
    
    return best_individual

# Running the genetic algorithm
best_individual = genetic_algorithm()
print(f"Best individual: {best_individual}")
print(f'\nWaktu komputasi: {time.time()- start_time}')
waktu = time.time() - start_time
print('Kecepatan Running: ', round((generations+1)/waktu), 'generasi/detik\n') 