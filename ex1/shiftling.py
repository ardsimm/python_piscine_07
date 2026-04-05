from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        self.name, self.type = "Shiftling", "Normal"
        self.state = "normal"

    def attack(self) -> str:
        attack_type: str

        if self.state == "normal":
            attack_type = "attacks normally."
        else:
            attack_type = "performs a boosted strike!"

        return f"{self.name} {attack_type}"

    def transform(self) -> str:
        self.state = "transformed"
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.state = "normal"
        return f"{self.name} returns to normal."
