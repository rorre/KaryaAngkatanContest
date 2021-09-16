import random
import os
from typing import List, Tuple

from answer import main

TOTAL = 20
BASE_PATH = os.path.dirname(__file__)
random.seed("cola-addict")

for i in range(2, TOTAL):
    x = random.randint(0, 999)
    n = random.randint(1, 50)
    y = random.randint(1, 500)

    stores: List[Tuple[int, int]] = []
    for _ in range(n):
        stores.append((random.randint(1, 10), random.randint(1, 10)))

    res = main(x, n, y, stores)
    input_file = os.path.join(BASE_PATH, f"tests/input/input{i}.txt")
    output_file = os.path.join(BASE_PATH, f"tests/output/output{i}.txt")

    with open(input_file, "w") as f:
        f.writelines(
            [
                f"{x} {n} {y}\n",
                *[f"{xi} {xj}\n" for xi, xj in stores],
            ]
        )

    with open(output_file, "w") as f:
        f.write(str(res))
