from player.utils import generate_seed_mappings
from constants import SEEDS_TIERS, SEEDED_DRAW_POSITIONS, N_PLAYERS, N_SEEDED


if __name__ == "__main__":
    mappings = generate_seed_mappings(
        seeds_tiers=SEEDS_TIERS,
        seeded_draw_positions=SEEDED_DRAW_POSITIONS,
        n_players=N_PLAYERS
    )

    print("SEDDED:")
    for k, v in mappings[0].items():
        print(f"  tier: {k} | seeds-to-positions: {v}")
    print(f"UNSEEDED:\n  {mappings[1]}")
