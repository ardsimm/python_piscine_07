#!/usr/bin/python3


from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("Testing Creature with healing capability")
    healing_creature_factory = HealingCreatureFactory()
    base = healing_creature_factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    evolved = healing_creature_factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")
    transform_creature_factory = TransformCreatureFactory()
    base = transform_creature_factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    evolved = transform_creature_factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    test_healing()
    print()
    test_transform()


if __name__ == "__main__":
    main()
