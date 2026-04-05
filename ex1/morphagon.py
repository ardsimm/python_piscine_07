from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        self.name, self.type = "Morphagon", "Normal/Dragon"
        self.state = "normal"

    def attack(self) -> str:
        attack_type: str

        if self.state == "normal":
            attack_type = "attacks normally."
        else:
            attack_type = "unleashes a devastating morph strike!"

        return f"{self.name} {attack_type}"

    def transform(self) -> str:
        self.state = "transformed"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.state = "normal"
        return f"{self.name} stabilizes its form."
