from collections import deque


class Bfs:
    def __init__(self, start, map):
        self.queue = deque([start])
        self.visited = set()
        self.found_objects = dict()
        self.parent = dict()
        self.start = start
        self.map = map

    def bfs(self, goal):
        while self.queue:
            current = self.queue.popleft()
            if current in self.visited:
                continue
            self.visited.add(current)
            if self.map[current].name == goal:
                # Проверка на достижение цели
                return self.construct_path(self.start, current)  # Построение пути

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + x, current[1] + y)
                if neighbor in self.map and neighbor not in self.visited and self.map[neighbor].name in (' ', goal):
                    self.queue.append(neighbor)
                    self.parent[neighbor] = current

    def construct_path(self, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = self.parent.get(current)
            if current is None:  # Если мы не можем найти путь
                return None
        path.append(start)
        path.reverse()
        return path
