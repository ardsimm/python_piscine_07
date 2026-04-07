from typing import Protocol


class HealingCapableCreature(Protocol):

    def attack(self) -> str:
        ...

    def describe(self) -> str:
        ...

    def heal(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, name: str) -> None:
        ...

    @property
    def type(self) -> str:
        ...

    @type.setter
    def type(self, type: str) -> None:
        ...
