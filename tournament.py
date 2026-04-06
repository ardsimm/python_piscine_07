#!/usr/bin/python3.10

from typing import Dict, List, Tuple, TypedDict
from ex0.aqua_factory import AquaFactory
from ex0.creature_factory import CreatureFactory
from ex0.flame_factory import FlameFactory
from ex1.healing_creature_factory import HealingCreatureFactory
from ex1.transform_creature_factory import TransformCreatureFactory
from ex2.agressive_strategy import AgressiveStrategy
from ex2.battle_strategy import BattleStrategy
from ex2.defensive_strategy import DefensiveStrategy
from ex2.normal_strategy import NormalStrategy

Oponent = Tuple[CreatureFactory, BattleStrategy]


def op_has_met(
    op1: Oponent,
    op2: Oponent,
    op_map: dict[Oponent, List[Oponent]]
) -> bool:
    op1_met = op_map.get(op1) or []
    op2_met = op_map.get(op2) or []
    return op1 in op2_met or op2 in op1_met


def update_op_met(
    op1: Oponent,
    op2: Oponent,
    op_met: Dict[Oponent, List[Oponent]]
) -> None:
    op_met[op1].append(op2)
    op_met[op2].append(op1)


def battle(oponents: List[Oponent]) -> None:
    op_met: dict[Oponent, List[Oponent]] = {
        op: []
        for op in oponents
    }

    for op1 in oponents:
        factory1 = op1[0]
        strategy1 = op1[1]
        creature1 = factory1.create_base()
        for op2 in oponents:
            if (
                op1 == op2
                or op_has_met(op1, op2, op_met)
            ):
                continue

            update_op_met(op1, op2, op_met)

            factory2 = op2[0]
            strategy2 = op2[1]
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print(" vs")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except ValueError as err:
                print("Battle error, aborting tournament:", err)
                break


def run_tournament(
        index: int,
        description: str,
        oponents: List[Oponent]
) -> None:
    print(f"\n*** Tournament {index} ({description}) ***")
    print(f"{len(oponents)} oponents involved")
    print(oponents)
    battle(oponents)


class Tournament(TypedDict):
    index: int
    description: str
    oponents: List[Oponent]


def main() -> None:

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_creature_factory = HealingCreatureFactory()
    transform_creature_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    defensive_strategy = DefensiveStrategy()
    agressive_strategy = AgressiveStrategy()

    tournaments: List[Tournament] = [
        {
            "index": 0,
            "description": "basic",
            "oponents": [
                (flame_factory, normal_strategy),
                (healing_creature_factory, defensive_strategy),
            ]
        }, {
            "index": 1,
            "description": "error",
            "oponents": [
                (flame_factory, agressive_strategy),
                (healing_creature_factory, defensive_strategy),
            ]
        }, {
            "index": 2,
            "description": "multiple",
            "oponents": [
                (aqua_factory, normal_strategy),
                (healing_creature_factory, defensive_strategy),
                (transform_creature_factory, agressive_strategy),
            ]
        }
    ]

    for tournament in tournaments:
        run_tournament(
            tournament["index"],
            tournament["description"],
            tournament["oponents"]
        )


if __name__ == "__main__":
    main()
