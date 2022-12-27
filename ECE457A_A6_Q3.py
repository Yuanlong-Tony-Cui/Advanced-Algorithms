import random

# x, y are two 14-bit-long binaries.
x = ""
y = ""
total_fitness = 0
pop_size = 20
population = []
avg_fitness_arr = []  # For plotting
best_ind_fitness_arr = [0]  # For plotting


def init_population():  # initializes the population randomly
    num_individuals = 0
    while num_individuals < pop_size:
        individual = ""
        i = 0
        while i < 28:
            individual += str(random.randint(0, 1))
            i += 1
        population.append(individual)
        num_individuals += 1
    # print(len(population))


def fitness(arg_x_bin, arg_y_bin):   # evaluates and returns z(x, y)
    arg_x = -5 + 0.001 * int(arg_x_bin, 2)   # converts x from binary to integer
    arg_y = -5 + 0.001 * int(arg_y_bin, 2)   # converts y from binary to integer
    if arg_x > 5 or arg_y > 5:
        return 0.001  # Out-of-range points get penalized.
    first_term = (4 - 2.1*pow(arg_x, 2) + pow(arg_x, 4)/3) * pow(arg_x, 2)
    third_term = (-4 + 4*pow(arg_y, 2)) * pow(arg_y, 2)
    z = first_term + arg_x * arg_y + third_term
    return 1.0 / (z + 2)


def wheel_selection(arg_pop_arr):
    fitness_arr = []
    for bin_str in arg_pop_arr:
        fitness_arr.append(fitness(bin_str[0:14], bin_str[14:28]))
    fitness_sum = sum(fitness_arr)
    # Record the avg fitness for the current population:
    avg_fitness_arr.append(fitness_sum/len(fitness_arr))

    # Calculate probabilities:
    p_arr = []  # Array of probabilities
    best_fitness = 0
    # print("fitness_arr:", fitness_arr)
    for fitness_val in fitness_arr:
        p_arr.append(fitness_val/fitness_sum)
        if fitness_val > best_fitness:
            best_fitness = fitness_val
    # print("best_fitness:", best_fitness)
    best_ind_fitness_arr.append(best_fitness)  # records the best fitness

    # Start selecting (wheel-and-pointer simulation):
    num_selected = 0
    selected_parents = []
    while num_selected < pop_size:
        wheel_ptr_val = random.uniform(0, 1)
        p_sum = 0
        p_idx = 0
        for p_val in p_arr:
            p_sum += p_val
            if wheel_ptr_val < p_sum:
                selected_parents.append(arg_pop_arr[p_idx])
                break
            p_idx += 1
        num_selected += 1
    return selected_parents


def crossover(arg_parents):
    var_children = []
    i = 0
    for parent in arg_parents:
        if i % 2 == 0:  # crossover with the next one:
            xover_idx = random.randint(1, 27)  # indices: 0 ~ 27
            var_children.append(parent[0:xover_idx] + arg_parents[i + 1][xover_idx:28])
            var_children.append(arg_parents[i + 1][0:xover_idx] + parent[xover_idx:28])
        i += 1
    return var_children


def mutation(arg_children):
    mut_p = 1.0/28  # probability of flipping a bit
    mutated_children = []
    for child_str in arg_children:
        i_child_str = 0
        for child_char in child_str:  # loops through the binary and mutate chars
            if random.uniform(0, 1) < mut_p:
                mut_str = child_str[0:i_child_str] + str(1-int(child_char)) + child_str[i_child_str+1:28]  # flips
                mutated_children.append(mut_str)
        i_child_str += 1

    return mutated_children


def search_for_optimum():
    global population
    # 1. Initialization of Population
    init_population()
    generations = 0
    while generations < 100000 and best_ind_fitness_arr[-1] != 1.0/(2-1.0316):
        # print(best_ind_fitness_arr[-1], 1.0/(2-1.0316))
        # 2. Parent Selection
        parents = wheel_selection(population)
        # 3. Crossover
        children = crossover(parents)
        # 4. Mutation
        mutated = mutation(children)
        # 5. Survivor Selection
        population = mutated.copy()
        # print("population:", population)
        print("avg", avg_fitness_arr[-1])
        generations += 1


search_for_optimum()
