import heapq


def heuristic(a, b):
    """计算启发式函数值，这里使用曼哈顿距离作为例子。"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(graph, start, goal):
    """A*搜索算法。"""
    # 优先级队列
    open_set = []
    heapq.heappush(open_set, (0, start))

    # 跟踪到达每个节点的最短路径
    came_from = {}
    cost_so_far = {}

    # 初始点的成本为0
    came_from[start] = None
    cost_so_far[start] = 0

    while open_set:
        current_priority, current = heapq.heappop(open_set)

        # 如果达到了目标点
        if current == goal:
            break

        # 遍历当前节点的邻接点
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(open_set, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    """通过came_from字典重建路径。"""
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


# 示例用法
class Grid:
    """示例网格类来表示图结构和边的代价。"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self, a, b):
        return 1


def print_gird(gird):
    for y in range(grid.height):
        for x in range(grid.width):
            if (x, y) in grid.walls:
                print("X", end=" ")
            elif (x, y) == start:
                print("A", end=" ")
            elif (x, y) == goal:
                print("B", end=" ")
            else:
                print(" ", end=" ")
        print()


def print_path(gird, path):
    for y in range(grid.height):
        for x in range(grid.width):
            if (x, y) in grid.walls:
                print("X", end=" ")
            elif (x, y) == start:
                print("A", end=" ")
            elif (x, y) == goal:
                print("B", end=" ")
            elif (x, y) in path:
                print(".", end=" ")
            else:
                print(" ", end=" ")
        print()


grid = Grid(10, 10)
# 设置障碍物用x表示障碍物
grid.walls = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
              (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
              (6, 5), (7, 5), (8, 5), (9, 5)]

start = (0, 0)  # 用A表示起点
goal = (7, 8)  # 用B表示终点

# 绘制图像：
print("Grid:")
print_gird(grid)

came_from, cost_so_far = a_star_search(grid, start, goal)
path = reconstruct_path(came_from, start, goal)

print("Path found:", path)

# 绘制结果
print("res:")
print_path(grid, path)
