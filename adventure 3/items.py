class Items(object):
    def __init__(self):
        pass
    pass
    class Consumables(Items):
        def __init__(self, hp_regen, hp_instant_heal):
            self.hp_regen = hp_regen
        pass
        class Potions(Consumables):
    