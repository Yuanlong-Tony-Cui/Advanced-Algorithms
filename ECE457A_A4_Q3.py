import math
import random

"""
State: [x1, x2, t]
(x1, x2) gives the coord, and t is the current temperature.
"""
max_iterations = 5000  # TODO
initial_temperature = 140  # TODO
alpha = 1
# alpha = 0.95  # TODO
tolerance = 0.05    # i.e. within 1% tolerance TODO

initial_point = [random.randrange(-100, 100), random.randrange(-100, 100)]
# initial_point = [3, 3]
curr_point = initial_point  # holds the current solution
curr_temperature = initial_temperature
limit = 1   # Lowest limit for temperature as a stop condition TODO
solution_found = False

# Number of solutions rejected/accepted by the acceptance function when delta_c > 0.
worse_solutions_rejected = 0
worse_solutions_accepted = 0
solutions_generated = 0


def easom_func(arg_coord):
    x1 = arg_coord[0]
    x2 = arg_coord[1]
    # print(pow(x1 - math.pi, 2), pow(x2 - math.pi, 2), math.exp(-pow(x1 - math.pi, 2) - pow(x2 - math.pi, 2)))
    return -math.cos(x1) * math.cos(x2) * math.exp(-pow(x1 - math.pi, 2) - pow(x2 - math.pi, 2))


def gen_neighbour(arg_coord):  # implements the neighbourhood function
    global solutions_generated
    solutions_generated = solutions_generated + 1
    return [arg_coord[0] + random.random() * random.choice([-1, 1]),
            arg_coord[1] + random.random() * random.choice([-1, 1])]


def calc_cost(arg_coord):   # implements the cost function
    return -1-easom_func(arg_coord)


def new_point_accepted(arg_neighbour):   # implements the acceptance function
    global worse_solutions_accepted
    global worse_solutions_rejected
    # delta_c = calc_cost(arg_neighbour) - calc_cost(curr_point)
    delta_c = - easom_func(arg_neighbour) + easom_func(curr_point)
    if delta_c > 0:
        # To accept it, the random percentage should be within the acceptance probability:
        if random.random() <= math.exp(-delta_c/curr_temperature):
            # print("P =", math.exp(-delta_c / curr_temperature))
            worse_solutions_accepted = worse_solutions_accepted + 1
            return True
        else:
            worse_solutions_rejected = worse_solutions_rejected + 1
            return False
    else:
        # print("delta_c:", delta_c)
        return True


def solution_found_with_tolerance(arg_coord):
    # print(easom_func(arg_coord))
    if (easom_func(arg_coord)/-1) > (1-tolerance):
        return True
    else:
        return False


def iterate_at_curr_temperature():  # continuously updates the current point
    global curr_point
    global solution_found
    for i in range(max_iterations):
        if solution_found_with_tolerance(curr_point):
            print("Solution found!")
            solution_found = True
            return
        neighbour = gen_neighbour(curr_point)
        # print("neighbour:", neighbour)
        if new_point_accepted(neighbour):
            curr_point = neighbour  # updates curr_point
            # print("curr_point:", curr_point)


def iterate_with_decreased_temperatures():
    global solution_found
    global curr_temperature
    while curr_temperature >= limit and solution_found is False:
        iterate_at_curr_temperature()
        curr_temperature = curr_temperature - alpha   # Linear
        # curr_temperature = curr_temperature * alpha   # Geometric
        print("curr_temperature:", curr_temperature)
    print("Number of generated solution:", solutions_generated)
    print("Number of worse solutions that were rejected:", worse_solutions_rejected)
    print("Number of worse solutions that were accepted:", worse_solutions_accepted)
    # print("easom_func([pi, pi])", easom_func([math.pi, math.pi]))
    # print("easom_func([..., ...])", easom_func([5, 5]))
    if solution_found:
        print("solution found!")
    else:
        print("solution not found.")
    print("Program terminated.")


def adjust_initial_temperature():
    global initial_temperature
    global curr_temperature
    iterate_at_curr_temperature()
    print("Number of worse solutions that were rejected:", worse_solutions_rejected)
    print("Number of worse solutions that were accepted:", worse_solutions_accepted)
    # A good initial temperature accepts ~60% (e.g. [55%, 65%]) of the worse moves
    acceptance_rate = worse_solutions_accepted/(worse_solutions_rejected + worse_solutions_accepted)
    while acceptance_rate > 0.65 or acceptance_rate < 0.55:
        if acceptance_rate > 0.65:
            initial_temperature = initial_temperature - 10
        elif acceptance_rate < 0.55:
            initial_temperature = initial_temperature + 10
        curr_temperature = initial_temperature
        print("curr_temperature:", curr_temperature)
        iterate_at_curr_temperature()
        acceptance_rate = worse_solutions_accepted / (worse_solutions_rejected + worse_solutions_accepted)


# adjust_initial_temperature()
iterate_with_decreased_temperatures()
