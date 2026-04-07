from ex1.transform_capable_creature import TransformCapableCreature
from ex2.battle_strategy import BattleStrategy
from ex2.invalid_strategy_exception import InvalidStrategyException


class AgressiveStrategy(BattleStrategy):

    def is_valid(self, creature: TransformCapableCreature) -> bool:
        return (
            hasattr(creature, "transform")
            and hasattr(creature, "revert")
            and hasattr(creature, "attack")
        )

    def act(self, creature: TransformCapableCreature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                creature.name, "agressive"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
