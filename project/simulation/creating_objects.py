class CreatingObjects:
    creating_objects = []
    moving_creatures = []
    grasses = []
    dct = {'Pred': moving_creatures, 'Herb': grasses}

    @staticmethod
    def remove_creature(x,y, name):
        for creature in CreatingObjects.dct[name]:
            if creature.x == x and creature.y == y:
                CreatingObjects.dct[name].remove(creature)
                break

