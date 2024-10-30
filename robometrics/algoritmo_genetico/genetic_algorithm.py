# algoritmo_genetico/genetic_algorithm.py

import random

from django.db.backends import sqlite3


# Função para converter tempo em segundos
def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

# Função para avaliar indivíduos
def evaluate(individual):
    return time_to_seconds(individual['time'])

# Função de crossover uniforme
def uniform_crossover(parent1, parent2):
    child1 = {}
    child2 = {}
    for key in ['P', 'I', 'D']:
        if random.random() > 0.5:
            child1[key], child2[key] = parent1[key], parent2[key]
        else:
            child1[key], child2[key] = parent2[key], parent1[key]
    return child1, child2

# Função para encontrar os dois melhores indivíduos
# Função para encontrar os dois melhores indivíduos
def get_best_individual(population):
    # Ordenar a população pelo tempo (do menor para o maior)
    sorted_population = sorted(population, key=evaluate)
    # Retornar os dois melhores indivíduos
    return sorted_population[:2]

# Função para extrair a população do banco de dados
def get_population_from_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT P, I, D, time FROM corridas")
    rows = cursor.fetchall()
    population = [{'P': row[0], 'I': row[1], 'D': row[2], 'time': row[3]} for row in rows]
    conn.close()
    return population

def genetic_algorithm(population):
    # Avaliar a população inicial
    best_individual = get_best_individual(population)
    print(f'Best initial individual: {best_individual}')

    # Selecionar os dois melhores indivíduos
    sorted_population = sorted(population, key=evaluate)
    parent1 = sorted_population[0]
    parent2 = sorted_population[1]

    # Aplicar crossover uniforme
    child1, child2 = uniform_crossover(parent1, parent2)

    # Avaliar os filhos gerados
    children = [child1, child2]
    for child in children:
        print(f'Child: {child}')

    return children
