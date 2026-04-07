class InvalidStrategyException(ValueError):
    def __init__(self, creature_name: str, strategy_name: str) -> None:
        super().__init__(
            f"Invalid creature {creature_name}" +
            f" for this {strategy_name} strategy"
        )
