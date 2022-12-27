import random
import math
import matplotlib.pyplot as plt

# Safety values to start with (proposed by Clerc and Kennedy in 2003):
w = 0.792
c1 = 1.4944
c2 = 1.4944

pop_size = 50
pop_v = []  # velocities of particles
pop_pos = []  # positions of particles
pbest = [{
    "x": 0,
    "y": 0
} for i in range(pop_size)]  # personal best (position) of each particle
Nbest = {
    "x": 0,
    "y": 0
}  # neighbourhood best (position)
optimum = -1.0316285  # true global minimum
optimum_found = False
avg_fitness_arr = []  # records the avg fitness for each iteration
best_fitness_arr = []  # records the best fitness for each iteration

def equals_optimum(arg_fitness):
    # return abs(arg_fitness-optimum) <= abs(optimum) * 0.0001
    return round(arg_fitness, 7) == optimum

def fitness(arg_position):
    x = arg_position["x"]
    y = arg_position["y"]
    return (4 - 2.1*pow(x, 2) + pow(x, 4)/3)*pow(x, 2) + x*y + (-4 + 4*pow(y, 2))*pow(y, 2)


def initialize():
    # 1. Initialize particles in the population
    i = 0
    while i < pop_size:
        v_initial = {
            "x": 0,
            "y": 0
        }  # Initialized as a small value
        p_initial = {
            "x": random.randint(-5, 5),
            "y": random.randint(-5, 5)
        }  # Initialized randomly in the range
        pop_v.append(v_initial)
        pop_pos.append(p_initial)
        i += 1
    # print(len(pop_pos), pop_pos)


def next_v(arg_particle_idx):
    v_next = {
        "x": 0,
        "y": 0
    }
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)
    idx = arg_particle_idx
    v_dir_x = w * pop_v[idx]["x"] + \
              c1 * r1 * (pbest[idx]["x"] - pop_pos[idx]["x"]) + \
              c2 * r2 * (Nbest["x"] - pop_pos[idx]["x"])
    v_dir_y = w * pop_v[idx]["y"] + \
              c1 * r1 * (pbest[idx]["y"] - pop_pos[idx]["y"]) + \
              c2 * r2 * (Nbest["y"] - pop_pos[idx]["y"])
    max_v = math.sqrt(2)
    if (v_dir_x > max_v):
        v_dir_x = max_v
    elif (v_dir_x < -max_v):
        v_dir_x = -max_v
    if (v_dir_y > max_v):
        v_dir_y = max_v
    elif (v_dir_y < -max_v):
        v_dir_y = -max_v
    return {
        "x": v_dir_x,
        "y": v_dir_y
    }


def next_pos(arg_particle_idx):
    idx = arg_particle_idx
    pos_x = pop_pos[idx]["x"] + pop_v[idx]["x"]
    pos_y = pop_pos[idx]["y"] + pop_v[idx]["y"]
    if (pos_x > 5):
        pos_x = 5
    elif (pos_x < -5):
        pos_x = -5
    if (pos_y > 5):
        pos_y = 5
    elif (pos_y < -5):
        pos_y = -5
    return {
        "x": pos_x,
        "y": pos_y
    }


def search_for_optimum():
    initialize()
    global optimum_found, Nbest
    i = 0
    max_iterations = 100
    while i < max_iterations and optimum_found is False:
        fitness_arr = []
        print(i)
        # Use async update mode to take advantage of the newest info:
        j = 0
        # For each particle:
        while j < pop_size:
            pop_v[j] = next_v(j)  # updates the velocity
            pop_pos[j] = next_pos(j)  # updates the position
            curr_fitness = fitness(pop_pos[j])
            if equals_optimum(curr_fitness):
                print("Optimum found in Iteration", i, "at", pop_pos[j])
                optimum_found = True
            # Update the pbest (position):
            if curr_fitness < fitness(pbest[j]):
                pbest[j] = pop_pos[j].copy()
            # Update the Nbest (position):
            if curr_fitness < fitness(Nbest):
                Nbest = pop_pos[j].copy()
            # Collect all fitness values for this iteration (for plotting):
            fitness_arr.append(curr_fitness)
            j += 1
        avg_fitness_arr.append(sum(fitness_arr)/len(fitness_arr))
        best_fitness_arr.append(min(fitness_arr))
        i += 1
    # print("Best value found:", min(fitness_arr))
    fig, axs = plt.subplots(2)
    axs[0].plot(range(1, i+1), avg_fitness_arr)
    axs[0].set_title("Average fitness")
    axs[1].plot(range(1, i+1), best_fitness_arr)
    axs[1].set_title("Best fitness")
    plt.show()

search_for_optimum()