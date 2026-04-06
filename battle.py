#!/usr/bin/python3.10

from typing import List
from ex0.aqua_factory import AquaFactory
from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory
from ex0.flame_factory import FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    basic: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()
    print(basic.describe())
    print(basic.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factories: List[CreatureFactory]) -> None:
    print("Testing battle")

    creatures = [factory.create_base() for factory in factories]

    creature_len = len(creatures)
    i = 0

    for creature in creatures:
        print(creature.describe())
        if i < creature_len - 1:
            print(" vs.")
        i += 1

    print(" fight!")

    for creature in creatures:
        print(creature.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle([flame_factory, aqua_factory])


if __name__ == "__main__":
    main()
