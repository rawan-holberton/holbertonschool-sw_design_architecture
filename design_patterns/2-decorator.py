#!/usr/bin/env python3
from __future__ import annotations


class Beverage:
    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator:
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator:
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


# ✅ YOU ADD THIS
class CaramelDecorator:
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main() -> None:
    coffee1 = MilkDecorator(Beverage())
    print(coffee1.description(), coffee1.cost())

    coffee2 = MilkDecorator(SugarDecorator(Beverage()))
    print(coffee2.description(), coffee2.cost())

    coffee3 = CaramelDecorator(MilkDecorator(SugarDecorator(Beverage())))
    print(coffee3.description(), coffee3.cost())


if __name__ == "__main__":
    main()
