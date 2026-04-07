from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__
