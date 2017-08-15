grid = [[0, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]]

start_vertex = (0, 2)
xs = [0, 1, -1, 0]
ys = [1, 0, 0, -1]


def paint_fill(color=2, x=start_vertex[0], y=start_vertex[1]):
    # Check the validity of this position.
    def is_valid(x, y, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited:
            return True
        return False

    visited = [(x, y)]
    grid[x][y] = color
    for index, val in enumerate(xs):
        new_x = val + x
        new_y = ys[index] + y
        if is_valid(new_x, new_y, visited):  # if valid
            grid[new_x][new_y] = color  # paint this one
            visited.append((new_x, new_y))  # add to visited
            paint_fill(color, new_x, new_y)  # recurse


paint_fill()
print(grid)
