from ex0.creature_factory import CreatureFactory
from ex1.bloomelle import Bloomelle
from ex1.sproutling import Sproutling


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
