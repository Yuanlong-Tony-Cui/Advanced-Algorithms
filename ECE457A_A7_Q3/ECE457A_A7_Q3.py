import pandas as pd
import math
import random
import matplotlib.pyplot as plt

city_coordinates = pd.read_csv('A7-city-coordinates.csv').to_dict()
x_coords = city_coordinates["X-coord."]
y_coords = city_coordinates["Y-coord."]
# print(x_coords)  # keys: 0 ~ 28

distances = [[-1]*29 for i in range(29)]  # a 29x29 2D array of -1's
pheromone_levels = [[1]*29 for i in range(29)]  # a 29x29 2D array of 1's
population = 100
evaporation_rate = 0.2  # 20% of pheromone is evaporated in each iteration.
Q = 10

shortest_path = []
shortest_distance = 9291.35255  # Optimum given by http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/bays29.opt.tour
shortest_distance_arr = []
avg_distance_arr = []
distances_in_one_iteration = []
best_solution_found = False


def initialize():
    # 1. Initialize the distance 2D array:
    i = 0
    while i < 29:
        j = i
        while j < 29:
            distances[i][j] = math.sqrt(
                pow(x_coords[i] - x_coords[j], 2) +
                pow(y_coords[i] - y_coords[j], 2)
            )
            j += 1
        i += 1
    # print(distances)


def pheromone_density(arg_curr_city, arg_city_option):
    if arg_curr_city < arg_city_option:
        return pheromone_levels[arg_curr_city][arg_city_option]/distances[arg_curr_city][arg_city_option]
    elif arg_curr_city > arg_city_option:
        return pheromone_levels[arg_city_option][arg_curr_city]/distances[arg_city_option][arg_curr_city]
    else:
        print("Wrong params passed into pheromone_density()!")
        return -1


def select_next_city(arg_pheromone_densities):
    # Simulate a pointer sliding on a probability bar to select:
    pointer_val = random.uniform(0, sum(arg_pheromone_densities))
    i = 0
    bar_val = 0
    while i < 29:
        bar_val += arg_pheromone_densities[i]
        if pointer_val <= bar_val:  # i.e. "pointer within this probability segment"
            # print("select_next_city()", i, pointer_val, bar_val)
            return i
        i += 1


def get_visited_cities():
    # Provides an educated path for a single ant based on pheromone levels
    visited_cities = [0]  # Always start from City 1 (index 0)
    while len(visited_cities) < 29:
        curr_city = visited_cities[-1]
        candidate_city = 0
        # 1) Collect pheromone density values from current city to all cities:
        pheromone_densities = []
        while candidate_city < 29:
            if candidate_city not in visited_cities:
                pheromone_densities.append(pheromone_density(curr_city, candidate_city))
            else:
                pheromone_densities.append(0)
            candidate_city += 1
        # print(curr_city, pheromone_densities)
        # 2) Select the next city (probability-based random selection):
        next_city = select_next_city(pheromone_densities)
        visited_cities.append(next_city)
    # print("visited_cities:", visited_cities)
    return visited_cities


def get_pheromone_increments(arg_pheromone_increments):
    # Updates an empty 2D array to simulate the accumulation of pheromone given by one ant.
    global best_solution_found, shortest_path, shortest_distance
    visited_cities = get_visited_cities()
    distance = calculate_total_distance(visited_cities)
    print(distance, "vs.", 9291.35255)
    if distance < shortest_distance:
        best_solution_found = True
        shortest_distance = distance
        shortest_path = visited_cities.copy()
        print("Best solution found!")
        print("shortest_path:", shortest_path)
    # Collect distances for the current iteration:
    distances_in_one_iteration.append(distance)

    # Calculate to see which edges should have their pheromone accumulated.
    i = 0
    while i < len(visited_cities):
        if i == len(visited_cities)-1:  # Last city needs to return to City 0.
            arg_pheromone_increments[0][visited_cities[-1]] += Q/distances[0][visited_cities[i]]
            break
        curr_city = visited_cities[i]
        next_city = visited_cities[i+1]
        if curr_city < next_city:
            arg_pheromone_increments[curr_city][next_city] += Q/distances[curr_city][next_city]
        elif curr_city > next_city:
            arg_pheromone_increments[next_city][curr_city] += Q/distances[next_city][curr_city]
        else:
            print("Error when modifying pheromone_increments!")
        i += 1
    # print("arg_pheromone_increments:", arg_pheromone_increments)
    return arg_pheromone_increments


def construct_ant_solutions():
    # Constructs all ant solutions in one iteration

    # 1. Evaporate pheromone on all the edges:
    global pheromone_levels
    i = 0
    while i < 29:
        j = i
        while j < 29:
            pheromone_levels[i][j] = (1-evaporation_rate)*pheromone_levels[i][j]
            j += 1
        i += 1

    # 2. Accumulate pheromone:
    pheromone_increments = [[0] * 29 for i in range(29)]  # 2D array
    ph_inc_arr = []  # An array used to collect 2D arrays.
    # 1) Collect the pheromone_increments given by all the ants in one iteration
    i = 0
    while i < population:
        ph_inc_arr.append(get_pheromone_increments(pheromone_increments))
        i += 1
    # 2) Update the pheromone_levels for all the edges
    i = 0
    while i < len(ph_inc_arr):
        j = 0
        while j < 29:
            k = j
            while k < 29:
                # ph_inc_arr[i][j][k] gives the pheromone increment on the j-to-k edge provided by ant i
                pheromone_levels[j][k] += ph_inc_arr[i][j][k]
                k += 1
            j += 1
        i += 1
    # print("pheromone_levels:", pheromone_levels)


def calculate_total_distance(arg_path):
    distance = 0
    i = 0
    while i < len(arg_path):
        if i == len(arg_path)-1:  # Last city needs to return to City 0
            distance += distances[0][arg_path[i]]
            break
        if arg_path[i] < arg_path[i+1]:
            distance += distances[arg_path[i]][arg_path[i+1]]
        elif arg_path[i] > arg_path[i+1]:
            distance += distances[arg_path[i+1]][arg_path[i]]
        else:
            print("Error when incrementing distance!")
        i += 1
    return distance


def find_solution():
    global distances_in_one_iteration
    initialize()

    # Repeat till the max iteration:
    i = 0
    max_iterations = 5000

    '''
    # Optimal solution:
    # Given by: http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/bays29.opt.tour
    optimal_solution = calculate_total_distance([
        0, 27, 5, 11, 8, 4, 25, 28, 2, 1,
        19, 9, 3, 14, 17, 16, 13, 21, 10, 18,
        24, 6, 22, 26, 7, 23, 15, 12, 20
    ])  # Gives 9291.352548891347
    # print("optimal_solution:", optimal_solution)
    '''

    while i < max_iterations:  # and best_solution_found is False:
        distances_in_one_iteration = []  # Resets for each iteration
        print("Iteration", i)
        construct_ant_solutions()
        # Append one value to these array to represent one iteration:
        print("distances_in_one_iteration:", distances_in_one_iteration)
        shortest_distance_arr.append(min(distances_in_one_iteration))
        avg_distance_arr.append(sum(distances_in_one_iteration)/len(distances_in_one_iteration))
        i += 1
    print("shortest_distance:", shortest_distance)
    print("shortest_path", shortest_path)
    plt.plot(range(0, i), shortest_distance_arr)
    plt.plot(range(0, i), avg_distance_arr)
    plt.legend(["Best fitness", "Average fitness"])
    plt.show()


# construct_ant_solutions()
find_solution()
