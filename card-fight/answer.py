from typing import List, Optional


total_moves, hp = list(map(int, input().split()))
dika_moves: List[str] = list(input())
dina_moves: List[str] = list(input())


class Player:
    def __init__(self, name: str, hp: int, moves: List[str]):
        self.name = name
        self.hp = hp
        self.moves = moves
        self.stats = 1  # DEF and ATK, they're always the same.
        self.last_move: Optional[str] = None

    def attack(self, target: "Player"):
        deal = self.stats
        if target.last_move == "D":
            deal -= target.stats

            # Ensure damage dealt is positive.
            # We don't want to heal the enemy when we attack them.
            deal = max(0, deal)

        target.hp -= deal

    def support(self):
        self.stats += 1


dika = Player("Dika", hp, dika_moves)
dina = Player("Dina", hp, dina_moves)

winner: Optional[Player] = None
for i in range(total_moves):
    for current, target in (
        (dika, dina),
        (dina, dika),
    ):
        current_move = current.moves[i]

        # Our last move is not a Support card, therefore
        # we've used our buffed stats with something else.
        # Thus we can just reset it.
        if current.last_move != "S":
            current.stats = 1

        if current_move == "A":
            current.attack(target)
        elif current_move == "S":
            current.support()

        current.last_move = current_move
        if target.hp <= 0:
            winner = current
            break

    if winner:
        break

if winner:
    print(winner.name)
else:
    if dika.hp > dina.hp:
        print("Dika")
    elif dika.hp == dina.hp:
        print("Seri")
    else:
        print("Dina")
