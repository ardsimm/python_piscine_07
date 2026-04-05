from ex0.creature import Creature
from ex1.heal_capacity import HealCapability


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name, self.type = "Bloomelle", "Grass/Fairy"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"
