from player.utils import create_dummy_players


if __name__ == "__main__":
    N_PLAYERS = 128
    N_SEEDED = 32
    players = create_dummy_players(n_players=N_PLAYERS, n_seeded=N_SEEDED)
    print("ℹ️ List of Player instances created:")
    for p in players:
        print("   -", p)
