from abc import ABC, abstractmethod
from ex0 import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__
