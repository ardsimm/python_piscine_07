from ex0.creature import Creature
from ex1.heal_capacity import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name, self.type = "Sproutling", "Grass"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"
