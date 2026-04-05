from ex0.creature_factory import CreatureFactory
from ex1.morphagon import Morphagon
from ex1.shiftling import Shiftling


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
