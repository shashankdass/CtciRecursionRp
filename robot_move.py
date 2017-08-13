"""
grid = [1,1,1]
"""
from collections import namedtuple

import math

grid = [[1 for _ in range(5)] for _ in range(5)]

# ===== 1st part find ways ====#
def robot_move_maths(grid, dest_x, dest_y):
    if dest_x <= 0 or dest_y <= 0:
        return 1
    return robot_move_maths(grid, dest_x - 1, dest_y) + robot_move_maths(grid, dest_x, dest_y - 1)


def check_by_math():
    num_rows = len(grid)
    num_cols = len(grid[0])
    fact = math.factorial
    res = fact(num_rows + num_cols) // fact(num_cols) // fact(num_rows)
    return res


print(robot_move_maths(grid, 5, 5))
print(check_by_math())

# ==== Follow Up ====#
obstacle_grid = [[1, 0, 1, 1],
                 [0, 0, 1, 1],
                 [0, 1, 1, 1],
                 [1, 1, 0, 0]]
xs = [1, 0]
ys = [0, -1]
Vertex = namedtuple("Vertex", "x y")


def robot_path_obstacles(path_till_now, cur_x, cur_y, visited):
    # Breaking condition for recursion
    if cur_x == len(obstacle_grid) - 1 and cur_y == 0:
        # return after pring path.
        print(path_till_now)
        return

    # Check down and right
    for index in range(2):
        # check for validity
        if is_valid(cur_x + xs[index], cur_y + ys[index], path_till_now):
            # append if valid
            path_till_now.append(Vertex(x=cur_x + xs[index], y=cur_y + ys[index]))
            # recurse for the valid index
            robot_path_obstacles(path_till_now, cur_x + xs[index], cur_y + ys[index], visited)

    # if not found return
    return


def is_valid(x, y, visited):
    if 0 <= x < len(obstacle_grid) and 0 <= y < len(obstacle_grid[0]) and Vertex(x, y) not in visited and \
                    obstacle_grid[x][y] == 1:
        return True
    return False


def robot_path_obstacles_driver():
    path_till_now = []
    cur_x = 0
    cur_y = len(obstacle_grid[0]) - 1
    visited = []
    start_vertex = Vertex(cur_x, cur_y)
    visited.append(start_vertex)
    path_till_now.append(start_vertex)
    robot_path_obstacles(path_till_now, 0, cur_y, visited)


robot_path_obstacles_driver()
