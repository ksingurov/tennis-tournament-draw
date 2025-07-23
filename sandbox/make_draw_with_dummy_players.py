from player.utils import generate_seed_mappings, create_players_list, make_draw
from constants import SEEDS_TIERS, SEEDED_DRAW_POSITIONS, N_PLAYERS, N_SEEDED


if __name__ == "__main__":
    seed_tiers_positions, unseeded_positions = generate_seed_mappings(
        seeds_tiers=SEEDS_TIERS,
        seeded_draw_positions=SEEDED_DRAW_POSITIONS,
        n_players=N_PLAYERS,
    )

    print("--------------------------------------------------------------------------------------------")
    print("SEDDED:")
    for k, v in seed_tiers_positions.items():
        print(f"  tier: {k} | seeds-to-positions: {v}")
    print(f"\nUNSEEDED:\n  {unseeded_positions}")


    players = create_players_list(n_players=N_PLAYERS, n_seeded=N_SEEDED)

    # print("--------------------------------------------------------------------------------------------")
    # print("ℹ️ CREATE List of Player instances:")
    # for p in players:
    #     print("   -", p)


    make_draw(
        players=players,
        seed_tiers_positions=seed_tiers_positions,
        unseeded_positions=unseeded_positions
    )

    print("--------------------------------------------------------------------------------------------")
    print("ℹ️ DRAW: SEEDED Player instances:")
    for p in players:
        if p.seed_id is not None:
            print("   -", p)
    print("--------------------------------------------------------------------------------------------")
    print("ℹ️ DRAW: UNSEEDED Player instances:")
    for p in players:
        if p.seed_id is None:
            print("   -", p)
