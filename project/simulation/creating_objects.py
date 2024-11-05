class CreatingObjects:
    creating_objects = []
    moving_creatures = []

    dct = {'Pred': moving_creatures}

    @staticmethod
    def remove_creature(x: int, y: int, name='Pred'):
        for creature in CreatingObjects.dct[name]:
            if creature.x == x and creature.y == y:
                CreatingObjects.dct[name].remove(creature)
                break
