from collections import deque

from project.setting import Setting


class Bfs:
    def __init__(self, start: tuple[int, int], map: dict[tuple[int, int], 'Creature'], setting: Setting):
        self.queue = deque([start])
        self.visited = set()
        self.found_objects = dict()
        self.parent = dict()
        self.start = start
        self.map = map
        self.setting = setting

    def bfs(self, goal):
        while self.queue:
            current = self.queue.popleft()
            if current in self.visited:
                continue
            self.visited.add(current)
            if type(self.map.get(current, None)) == goal:
                # Проверка на достижение цели
                return self.construct_path(self.start, current)  # Построение пути

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + x, current[1] + y)
                if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < self.setting.width and neighbor[1] < self.setting.height:
                    if neighbor not in self.visited and type(self.map.get(neighbor, None)) in (type(None), goal):
                        self.queue.append(neighbor)
                        self.parent[neighbor] = current

    def construct_path(self, start: tuple[int, int], goal: tuple[int, int]) -> list[tuple[int, int]]:
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
