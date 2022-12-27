maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
]

"""
S = (2, 11) = maze[11][2] = [11, 2]
E1 = (23, 19) = maze[19][23] = [19, 23]
E2 = (2, 21) = maze[21][2] = [21, 2]
"""

# A* Algorithm


def manhattan_dist(arg_curr_node):
    manh_dist_to_e1 = abs(arg_curr_node[0] - 19) + abs(arg_curr_node[1] - 23)
    manh_dist_to_e2 = abs(arg_curr_node[0] - 21) + abs(arg_curr_node[1] - 2)
    if manh_dist_to_e1 <= manh_dist_to_e2:
        return manh_dist_to_e1
    else:
        return manh_dist_to_e2


open_queue = [[11, 2, "S", 0, manhattan_dist([11, 2])]]
closed_queue = []
exit_found = False

"""
Example node: [11, 3, "right", 1, manhattan_dist]
where 1 is the cost from the start point to the current location
"""


def point_is_valid(coord):
    # Valid means: Within map + Not blocked
    return (0 <= coord[0] <= 24) and (0 <= coord[1] <= 24) and maze[coord[0]][coord[1]] == 0


def node_visited(coord):
    for visited_node in closed_queue:
        if coord[0:2] == visited_node[0:2]:
            return True
    return False


def total_cost(arg_node):   # Helper function that gives the sorting criterion
    return arg_node[3] + arg_node[4]    # current cost + estimated cost


def node_in_open_queue(arg_node):
    # Nodes with the same coordinates AND existing & estimated costs are considered as duplicated states
    for node in open_queue:
        if arg_node[0:2] == node[0:2] and total_cost(arg_node) == total_cost(node):
            # print("Duplicated state found in the open queue:", node)
            return True
    return False


def expand_node():
    node_to_expand = open_queue[0]

    # 1. Check if this node is already in the closed queue:
    open_queue.pop(0)
    if node_visited(node_to_expand):
        return  # i.e. Exit without actually expanding this node

    # 2. Expand this node and add its children to the open queue:
    closed_queue.append(node_to_expand)
    # print("Expanded node:", node_to_expand)
    new_nodes = [
        [node_to_expand[0], node_to_expand[1] - 1, "left", -1, -1],
        [node_to_expand[0] + 1, node_to_expand[1], "up", -1, -1],
        [node_to_expand[0], node_to_expand[1] + 1, "right", -1, -1],
        [node_to_expand[0] - 1, node_to_expand[1], "down", -1, -1]
    ]
    for new_node in new_nodes:
        # Update the last two indices:
        new_node[3] = node_to_expand[3] + 1
        new_node[4] = manhattan_dist(new_node[0:2])
        if point_is_valid(new_node) and not node_visited(new_node) and not node_in_open_queue(new_node):
            open_queue.append(new_node)

    # 3. Since the algorithm is A*, the open queue is sorted by estimated total costs:
    open_queue.sort(key=total_cost)

    # 4. Check if the last node expanded is one of the exits:
    global exit_found
    if closed_queue[-1][0:2] == [19, 23]:
        print("Exit found: E1")
        exit_found = True
    if closed_queue[-1][0:2] == [21, 2]:
        print("Exit found: E2")
        exit_found = True


def search_for_exit():
    count = 0
    while len(open_queue) > 0 and exit_found is False and count <= 1000:
        expand_node()
        count = count + 1
    print("Number of nodes explored:", len(closed_queue))


search_for_exit()

# The backtracking algorithm is the same from Assignment 2
solution_path = [[11, 2], closed_queue[-1][0:2]]   # We know for sure that the start and exit points are in the path.


def retrieve_parent_node(curr_node):
    # curr_node = closed_queue[-1]
    parent_node = curr_node[0:2]

    if curr_node[2] == "left":
        parent_node[1] = curr_node[1] + 1
    elif curr_node[2] == "up":
        parent_node[0] = curr_node[0] - 1
    elif curr_node[2] == "right":
        parent_node[1] = curr_node[1] - 1
    elif curr_node[2] == "down":
        parent_node[0] = curr_node[0] + 1
    else:
        print("Error: direction undetermined.")
    return parent_node


backtracking_completed = False


def track_path():
    global backtracking_completed
    while not backtracking_completed:
        # 1. Loop through closed_queue to find the full info of the target node (e.g. [22, 6, "left"]):
        # The target node is always at Index 1 of solution_path
        input_node = solution_path[1]
        parent_node = []
        for node in closed_queue:
            if node[0:2] == input_node:
                # 2. Find its parent node and add it to solution_path:
                parent_node = retrieve_parent_node(node)
        # Stop condition:
        if parent_node == [11, 2]:
            backtracking_completed = True
            break
        solution_path.insert(1, parent_node)
    # print("solution_path:", solution_path)
    print("Cost:", len(solution_path) - 1)  # Excluding the start point
    print("Complete path:", format_solution_path(solution_path))


def format_solution_path(arg_solution_path):
    # e.g. from [22, 6] to (6, 22)
    coord_path = []
    for point in arg_solution_path:
        coord = "(" + str(point[1]) + ", " + str(point[0]) + ")"
        coord_path.append(coord)
    return coord_path


track_path()
