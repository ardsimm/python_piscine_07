from ex0 import Creature
from ex0 import CreatureFactory
from ex0.aquabub import Aquabub
from ex0.torragon import Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
