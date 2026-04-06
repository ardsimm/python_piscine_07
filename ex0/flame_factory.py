from ex0 import Creature
from ex0 import CreatureFactory
from ex0.flameling import Flameling
from ex0.pyrodon import Pyrodon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()
