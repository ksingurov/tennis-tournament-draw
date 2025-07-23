from player.utils import load_players_from_json


if __name__ == "__main__":
    FIELDS_MAPPING = {
        "name": "surname",
        "number_id": "entry#",
        "seed_id": "entry#"
    }
    print(f"  FIELDS_MAPPING: {FIELDS_MAPPING}")
    
    JSON_PATH = "data/wimbledon.com/processed/players.json"
    players = load_players_from_json(
        json_path=JSON_PATH,
        fields_mapping=FIELDS_MAPPING
    )
    print("🏟️ 2025 WIMBLEDON CHAMPIONSHIPS\n  GENTLEMEN'S SINGLES: ENTRY LIST")
    for p in players:
        print("  🎾", p)



# # NOTE: actually wise versa is needed
# # entry-fields-to-attributes
# # FIELDS_MAPPING = {
# #     "entry#": "number_id",
# #     "surname": "name",
# #     # "surname": "surname",
# #     # "country": "country",
# #     # "seed": "seed_id"
# # }
# # attrbiutes-to-entry-fields
# FIELDS_MAPPING = {
#     "number_id": "entry#",
#     "name": "surname"
# }
# print(f"  FIELDS_MAPPING: {FIELDS_MAPPING}")

# entry = {
#     "entry#": 1,
#     "surname": "SINNER",
#     "name": "Jannik",
#     "country": "ITA",
#     "entry_info": None,
#     "rank": 1
# }
# print(f"  entry: {entry}")

# # attributes = {
# #     "name": entry["surname"],
# #     "number_id":  entry["entry#"]
# # }
# attributes = {
#     key: entry[value]
#     for key, value in FIELDS_MAPPING.items()
# }
# print(f"  attributes: {attributes}")


