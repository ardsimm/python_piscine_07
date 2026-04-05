from typing import Union

from ex0.creature import Creature
from ex1.transform_capability import TransformCapability
from ex2.battle_strategy import BattleStrategy


class AgressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Union[Creature, TransformCapability]) -> bool:
        return (
            hasattr(creature, "transform")
            and hasattr(creature, "revert")
            and hasattr(creature, "attack")
        )

    def act(self, creature: Union[Creature, TransformCapability]) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid creature {creature.name}" +  # type: ignore
                " for this agressive strategy"
            )
        print(creature.transform())  # type: ignore
        print(creature.attack())  # type: ignore
        print(creature.revert())  # type: ignore
