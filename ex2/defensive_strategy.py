from ex1.healing_capable_creature import HealingCapableCreature
from ex2.battle_strategy import BattleStrategy
from ex2.invalid_strategy_exception import InvalidStrategyException


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: HealingCapableCreature) -> bool:
        return (
            hasattr(creature, "heal")
            and hasattr(creature, "attack")
        )

    def act(self, creature: HealingCapableCreature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                creature.name, "defensive"
            )
        print(creature.attack())
        print(creature.heal())
