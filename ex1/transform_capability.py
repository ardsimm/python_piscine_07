from abc import ABC, abstractmethod
from typing import Literal


class TransformCapability(ABC):

    __state: Literal["normal", "transformed"]

    def __init__(
        self,
        state: Literal["normal", "transformed"]
    ) -> None:
        self.state = state
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

    @property
    def state(self) -> Literal["normal", "transformed"]:
        return self.__state

    @state.setter
    def state(
        self,
        state: Literal["normal", "transformed"]
    ) -> None:
        self.__state = state
