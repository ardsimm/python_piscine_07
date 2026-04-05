from typing import Union
from ex0.creature import Creature
from ex1.heal_capacity import HealCapability
from ex2.battle_strategy import BattleStrategy


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return (
            hasattr(creature, "heal")
            and hasattr(creature, "attack")
        )

    def act(self, creature: Union[Creature, HealCapability]) -> None:
        if not self.is_valid(creature):  # type: ignore
            raise ValueError(
                f"Invalid creature {creature.name}" +  # type: ignore
                " for this defensive strategy"
            )
        print(creature.attack())  # type: ignore
        print(creature.heal())  # type: ignore
