# UTILS for Player and raw 
from .core import Player
# from constants import SEEDS_TIERS, SEEDED_DRAW_POSITIONS, N_PLAYERS, N_SEEDED
import random


def create_players_list(n_players: int, n_seeded: int):
    players = [
        Player(
            number_id=f"#{i}",
            seed_id=i if i <= n_seeded else None
        )
        for i in range(1, n_players + 1)
    ]
    return players
