from collections import deque
from project.Simulation.Map import Map
from project.Simulation.actions import Actions

class Bfs:
    def __init__(self, start):
        self.queue = deque([start])
        self.visited = set()
        self.found_objects = dict()

    def bfs(self):
        while self.queue:
            current = self.queue.popleft()
            if current in self.visited:
                continue
            self.visited.add(current)

            entity = map.map.get(current)
            if entity and entity != '(..)':
                self.found_objects[current] = entity

            for x,y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + x, current[1] + y)
                if neighbor in map.map and neighbor not in self.visited:
                    self.queue.append(neighbor)

        return self.found_objects


if __name__ == '__main__':
    Actions.creature()
    map = Map()
    map.create_map()
    map.display_map()
    b = Bfs((0,0))
    b.bfs()
    print(b.found_objects)

    


