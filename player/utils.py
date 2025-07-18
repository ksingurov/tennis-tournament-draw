# UTILS for Player and raw 
from player.core import Player
from constants import SEEDS_TIERS, SEEDED_DRAW_POSITIONS, N_PLAYERS, N_SEEDS


# ============ UTILS for Draw ============
all_seeded_positions = [pos for bracket in SEEDED_DRAW_POSITIONS.values() for pos in bracket]
unseeded_draw_positions = list(set(range(1, N_PLAYERS + 1)) - set(all_seeded_positions))
# print(unseeded_draw_positions)

tiers = {}
for t in SEEDS_TIERS.keys():
    seeds = list(range(SEEDS_TIERS[t][0], SEEDS_TIERS[t][1] + 1))
    positions = SEEDED_DRAW_POSITIONS[t]
    tiers[t] = (seeds, positions)


# ============ UTILS for Player ============
N_PLAYERS = 128
N_SEEDED = 32

def create_players_list(n_players: int, n_seeded: int):
    players = []
    for i in range(1, n_players + 1):
        player = Player(
            name=f"#{i}",
            seed=i if i <= n_seeded else None
        )
        players.append(player)
    return players
