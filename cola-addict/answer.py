from typing import List, Tuple


def main(money: int, n: int, price: int, stores: List[Tuple[int, int]]):
    highest = 0

    # The cola we can get WITHOUT bonuses
    base_colas = money // price
    for i in range(n):
        bonus, minimum = stores[i]

        acquired_bonus = (base_colas // minimum) * bonus
        total = base_colas + acquired_bonus
        if total > highest:
            highest = total

    return highest


if __name__ == "__main__":
    x, n, y = list(map(int, input().split()))
    stores: List[Tuple[int, int]] = []
    for _ in range(n):
        stores.append(tuple(map(int, input().split())))  # type: ignore

    print(main(x, n, y, stores))
