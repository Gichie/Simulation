class CreatingObjects:
    creating_objects = []
    moving_creatures = [creature for creature in creating_objects if creature.name in ('Pred', 'Herb')]

    @staticmethod
    def remove_creature(x,y):
        for creature in CreatingObjects.moving_creatures:
            if creature.x == x and creature.y == y:
                CreatingObjects.moving_creatures.remove(creature)
                break