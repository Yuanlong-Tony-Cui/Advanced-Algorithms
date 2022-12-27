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
open_queue = [[11, 2]]
closed_queue = []
exit_found = False


def point_is_valid(coord):
    # Valid means: Within map + Not blocked
    return (0 <= coord[0] <= 24) and (0 <= coord[1] <= 24) and maze[coord[0]][coord[1]] == 0


def gen_node(curr_node, direction):
    generated_node = [curr_node[0], curr_node[1], direction]
    # e.g. [11, 3, "L"] means this node is the left node of its parent.
    if direction == "left":
        generated_node[1] = curr_node[1] - 1
    elif direction == "up":
        generated_node[0] = curr_node[0] + 1
    elif direction == "right":
        generated_node[1] = curr_node[1] + 1
    elif direction == "down":
        generated_node[0] = curr_node[0] - 1

    if not point_is_valid(generated_node):
        return None

    # Assumption: each coordinate appears at most once in the search tree.

    for node in open_queue:
        if generated_node[0:2] == node[0:2]:    # Only compares the coordinate
            return None
    for node in closed_queue:
        if generated_node[0:2] == node[0:2]:    # Only compares the coordinate
            return None
    return generated_node


def expand_node(arg_search_alg, arg_tie_breaking_rule):
    # print("B4 Open queue:", open_queue)
    # print("B4 Closed queue:", closed_queue)

    seq = []
    if arg_tie_breaking_rule == 1:
        seq = ["left", "up", "right", "down"]
    elif arg_tie_breaking_rule == 2:
        seq = ["right", "up", "left", "down"]

    # Need to: 1. Remove one node from the open queue, 2. Add node(s) to the closed queue.
    if arg_search_alg == "BFS":
        # Add new nodes to the right, and pop expanded nodes from the left.
        node_to_expand = open_queue[0]
        open_queue.pop(0)
        closed_queue.append(node_to_expand)
        for i in seq:
            generated_node = gen_node(node_to_expand, i)
            if generated_node is not None:
                open_queue.append(generated_node)
    elif arg_search_alg == "DFS":
        # First pop expanded nodes from the right, and then add new nodes to the right as well.
        node_to_expand = open_queue[-1]
        open_queue.pop()
        closed_queue.append(node_to_expand)
        temp_arr = []   # Used for adding new nodes in reversed order for DFS
        for i in seq:
            generated_node = gen_node(node_to_expand, i)
            if generated_node is not None:
                temp_arr.append(generated_node)
        # print("temp_arr:", temp_arr)
        temp_arr.reverse()
        for i in temp_arr:
            open_queue.append(i)

    global exit_found
    if closed_queue[-1][0:2] == [19, 23]:
        print("Exit found: E1")
        exit_found = True
    if closed_queue[-1][0:2] == [21, 2]:
        print("Exit found: E2")
        exit_found = True

    # print("AFTER Open queue:", open_queue)
    # print("AFTER Closed queue:", closed_queue)


search_alg = "BFS"  # "BFS" or "DFS"
tie_breaking_rule = 2  # 1 or 2


def search_for_exit():
    goal_node_found = False
    count = 0
    while len(open_queue) > 0 and exit_found is False and count <= 10000:   # TODO: remove the limit
        # print("Number of expanded nodes:", count)
        expand_node(search_alg, tie_breaking_rule)
        count = count + 1
    # print("Closed queue:", closed_queue)
    print("Number of nodes explored:", len(closed_queue))
    # print("Program terminated.")


search_for_exit()
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



