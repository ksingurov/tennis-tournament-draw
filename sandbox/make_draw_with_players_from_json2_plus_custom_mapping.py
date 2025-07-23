# <<< NOTE: DEVELOPING >>>

from player.utils import generate_seed_mappings, load_players_from_json2, make_draw
from constants import SEEDS_TIERS, SEEDED_DRAW_POSITIONS, N_PLAYERS, N_SEEDED


if __name__ == "__main__":
    def make_custom_fields_mapping(n_seeded: int | None = None) -> dict[str, callable]:
        return {
            "name": lambda entry: f"{entry["name"]} {entry["surname"]}",
            "number_id": lambda entry: entry["entry#"],
            "seed_id": (
                lambda entry: entry["entry#"] if entry["entry#"] <= n_seeded else None
                if n_seeded is not None else
                lambda entry: entry["entry#"]
            )
        }

    # N_SEEDED = 32
    custom_mapping = make_custom_fields_mapping(n_seeded=N_SEEDED)

    JSON_PATH = "data/wimbledon.com/processed/players.json"
    players = load_players_from_json2(
        json_path=JSON_PATH,
        fields_mapping=custom_mapping
    )

    seed_tiers_positions, unseeded_positions = generate_seed_mappings(
        seeds_tiers=SEEDS_TIERS,
        seeded_draw_positions=SEEDED_DRAW_POSITIONS,
        n_players=N_PLAYERS,
    )

    make_draw(
        players=players,
        seed_tiers_positions=seed_tiers_positions,
        unseeded_positions=unseeded_positions
    )

    print("\n=========================================================================================")
    print("🏟️ 2025 WIMBLEDON CHAMPIONSHIPS | GENTLEMEN'S SINGLES")
    seeded_players = []
    unseeded_players = []
    [seeded_players.append(p) if p.seed_id is not None else unseeded_players.append(p) for p in players]
    print("-----------------------------------------------------------------------------------------")
    print("🌱 SEEDED PLAYERS:")
    print("-----------------------------------------------------------------------------------------")
    for p in seeded_players:
        print("  🎾", p)
    print("-----------------------------------------------------------------------------------------")
    print("🎲 UNSEEDED PLAYERS:")
    print("-----------------------------------------------------------------------------------------")
    for p in unseeded_players:
        print("  🎾", p)
    print("=========================================================================================\n")

