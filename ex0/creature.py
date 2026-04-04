from abc import ABC, abstractmethod


class Creature(ABC):
    __type: str
    __name: str

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type
