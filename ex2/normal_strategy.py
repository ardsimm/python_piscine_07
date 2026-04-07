from ex0.creature import Creature
from ex2.battle_strategy import BattleStrategy
from ex2.invalid_strategy_exception import InvalidStrategyException


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                creature.name, "normal"
            )
        print(creature.attack())
