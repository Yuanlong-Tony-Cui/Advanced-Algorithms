import random
import pandas as pd

distances = pd.read_csv('A5-Distance.csv').to_dict()    # between positions
flows = pd.read_csv('A5-Flow.csv').to_dict()    # between departments

# print(distances["position 1"][19])  # gives distance from position 1 to 20
# print(flows["dep 1"][19])   # gives flow from dep 1 to 20

# Each index holds a department number.
initial_plan_1 = [1, 2, 3, 4, 5,
                  6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20]
initial_plan_2 = [11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20,
                  1, 2, 3, 4, 5,
                  6, 7, 8, 9, 10]
initial_plan_3 = [2, 3, 5, 7, 11, 13, 17, 19,
                  1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
curr_plan = initial_plan_1
optimal_solution_found = False
lowest_cost_so_far = 1000000    # A very large value like 1M.

# Tabu memory is a 20x20 matrix filled with zeros.
tabu_mem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i_mem = 0
while i_mem < 20:
    tabu_mem[i_mem] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i_mem += 1
# print(tabu_mem)


# cost_of_plan() returns the sum of (flow * dist) for all possible pairs of departments
def cost_of_plan(arg_plan):
    total_cost = 0
    for src_dep in arg_plan:
        for des_dep in arg_plan:
            src_idx = arg_plan.index(src_dep)
            des_idx = arg_plan.index(des_dep)
            if des_idx > src_idx:
                dist_val = distances["position "+str(src_idx+1)][des_idx]   # idx: [0, 19]
                flow_val = flows["dep "+str(src_dep)][des_dep-1]    # dep: [1, 20]
                total_cost += dist_val * flow_val
    return total_cost


def gen_all_neighbours():
    neighbours = []
    for depA in curr_plan:
        for depB in curr_plan:
            i = curr_plan.index(depA)
            j = curr_plan.index(depB)
            if j > i:
                new_plan = curr_plan.copy()
                new_plan[i], new_plan[j] = new_plan[j], new_plan[i]
                neighbours.append(new_plan)
    # print("Generated all neighbours:", len(neighbours))
    return random.sample(neighbours, 95)     # picks random 50% of the neighbours


def is_tabu_move(arg_curr_plan, arg_next_move):
    swapped_positions = find_swapped_positions(arg_curr_plan, arg_next_move)
    # print("swapped_positions:", swapped_positions)
    return tabu_mem[swapped_positions[0]][swapped_positions[1]] > 0


def freq(arg_curr_plan, arg_next_move):
    swapped_positions = find_swapped_positions(arg_curr_plan, arg_next_move)
    return tabu_mem[swapped_positions[1]][swapped_positions[0]]


def next_move():
    global lowest_cost_so_far
    neighbours = gen_all_neighbours()
    lowest_cost_local = 1000000   # A large enough value (1M)
    best_plan = []
    for neighbour in neighbours:
        if is_tabu_move(curr_plan, neighbour) is False or (is_tabu_move(curr_plan, neighbour) is True and cost_of_plan(neighbour) < lowest_cost_so_far):
            if cost_of_plan(neighbour) < lowest_cost_local:
                lowest_cost_local = cost_of_plan(neighbour)
                best_plan = neighbour
    if lowest_cost_local < lowest_cost_so_far:
        lowest_cost_so_far = lowest_cost_local
    print("Best plan identified. Cost:", lowest_cost_local)
    return best_plan


def find_swapped_positions(arg_curr_plan, arg_next_move):
    swapped_positions = []
    i = 0
    while i < 20:
        if arg_curr_plan[i] != arg_next_move[i]:
            swapped_positions.append(i)
        i += 1
    swapped_positions.sort()
    return swapped_positions


def update_tabu_mem(arg_curr_plan, arg_next_move):
    # Compare the plans to find the swapped departments:
    swapped_positions = find_swapped_positions(arg_curr_plan, arg_next_move)
    # print("swapped positions:", swapped_positions)
    # Decrement existing non-zero tabu memory locations:
    for row in tabu_mem:
        for col in tabu_mem:
            row_i = tabu_mem.index(row)
            col_i = tabu_mem.index(col)
            if col_i > row_i:
                if tabu_mem[row_i][col_i] != 0:
                    tabu_mem[row_i][col_i] -= 1
    # Update the tabu memory location to indicate the current swap:
    tabu_mem[swapped_positions[0]][swapped_positions[1]] = 21  # Tabu Tenure: sqrt(190) = 14
    # Update freq-based memory:
    tabu_mem[swapped_positions[1]][swapped_positions[0]] += 1


def find_optimal_solution():
    global curr_plan
    global optimal_solution_found
    iteration = 0
    while optimal_solution_found is False and iteration < 10000:
        next_plan = next_move()
        print("Iteration #:", iteration)
        # print("curr_plan:", curr_plan)
        # print("next_plan:", next_plan)
        update_tabu_mem(curr_plan, next_plan)
        curr_plan = next_plan
        print("curr_plan:", curr_plan)
        if cost_of_plan(curr_plan) == 1285:
            optimal_solution_found = True
            break
        iteration += 1


find_optimal_solution()