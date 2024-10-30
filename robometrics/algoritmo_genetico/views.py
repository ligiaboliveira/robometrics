# algoritmo_genetico/views.py

from django.shortcuts import render
from .genetic_algorithm import genetic_algorithm

# Lista de indivíduos com seus parâmetros e tempos
population = [
    {'P': 2, 'I': 0.25, 'D': 3, 'time': '2:30'},
    {'P': 2, 'I': 0.30, 'D': 1, 'time': '2:45'},
    {'P': 3, 'I': 0.35, 'D': 2, 'time': '2:15'}
]

def run_genetic_algorithm(request, population):
    best_children = genetic_algorithm(population)
    print(best_children)
    context = {
        'best_children': best_children
    }
    return render(request, 'algoritmo_genetico/result.html', context)