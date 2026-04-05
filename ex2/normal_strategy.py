from ex0.creature import Creature
from ex2.battle_strategy import BattleStrategy


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid creature {creature.name}" +
                " for this normal strategy"
            )
        print(creature.attack())
