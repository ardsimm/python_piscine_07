from typing import Literal, Protocol


class TransformCapableCreature(Protocol):

    def attack(self) -> str:
        ...

    def describe(self) -> str:
        ...

    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...

    @property
    def state(self) -> Literal["normal", "transformed"]:
        ...

    @state.setter
    def state(
        self,
        state: Literal["normal", "transformed"]
    ) -> None:
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
