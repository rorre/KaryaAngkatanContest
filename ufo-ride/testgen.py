import random
import os
import string

from answer import main

TOTAL = 20
BASE_PATH = os.path.dirname(__file__)
random.seed("ufo-ride")


def random_str(N):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(N))


for i in range(TOTAL // 2 + 1):
    res = ""
    n = random.randint(2, 19)
    while res != "PERGI":
        a1 = random_str(n)
        a2 = random_str(n)
        res = main(a1, a2)

    input_file = os.path.join(BASE_PATH, f"tests/input/input{i}.txt")
    output_file = os.path.join(BASE_PATH, f"tests/output/output{i}.txt")

    with open(input_file, "w") as f:
        f.writelines([str(n) + "\n", a1 + "\n", a2 + "\n"])

    with open(output_file, "w") as f:
        f.write(res)

for i in range(TOTAL // 2 + 1, TOTAL):
    res = ""
    n = random.randint(2, 19)
    while res != "TETAP":
        a1 = random_str(n)
        a2 = random_str(n)
        res = main(a1, a2)

    input_file = os.path.join(BASE_PATH, f"tests/input/input{i}.txt")
    output_file = os.path.join(BASE_PATH, f"tests/output/output{i}.txt")

    with open(input_file, "w") as f:
        f.writelines([str(n) + "\n", a1 + "\n", a2 + "\n"])

    with open(output_file, "w") as f:
        f.write(res)
