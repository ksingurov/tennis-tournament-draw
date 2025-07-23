from player.utils import load_players_from_json2


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

    N_SEEDED = 32
    custom_mapping = make_custom_fields_mapping(n_seeded=N_SEEDED)

    JSON_PATH = "data/wimbledon.com/processed/players.json"
    players = load_players_from_json2(
        json_path=JSON_PATH,
        fields_mapping=custom_mapping
    )

    print("\n=========================================================================================")
    print("🏟️ 2025 WIMBLEDON CHAMPIONSHIPS | GENTLEMEN'S SINGLES | ENTRY LIST 📋")
    print("-----------------------------------------------------------------------------------------")
    for p in players:
        print("  🎾", p)
    print("=========================================================================================\n")
