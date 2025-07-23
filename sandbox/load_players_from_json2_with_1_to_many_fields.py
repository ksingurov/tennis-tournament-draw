from player.utils import make_fields_mapping_with_1_to_many_fiels, load_players_from_json2


if __name__ == "__main__":
    FIELDS_MAPPING = {
        "name": ("name", "surname"),
        "number_id": "entry#",
        "seed_id": "entry#"
    }
    print(f"  FIELDS_MAPPING: {FIELDS_MAPPING}")
    
    mapping = make_fields_mapping_with_1_to_many_fiels(fields_mapping=FIELDS_MAPPING)

    JSON_PATH = "data/wimbledon.com/processed/players.json"
    players = load_players_from_json2(
        json_path=JSON_PATH,
        fields_mapping=mapping
    )
    print("🏟️ 2025 WIMBLEDON CHAMPIONSHIPS\n  GENTLEMEN'S SINGLES: ENTRY LIST")
    for p in players:
        print("  🎾", p)
