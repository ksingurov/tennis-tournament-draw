# UTILS for Player class
from .core import Player
# from constants import SEEDS_TIERS, SEEDED_DRAW_POSITIONS, N_PLAYERS, N_SEEDED
import random
import json


# ==================================================================================================
def create_dummy_players(n_players: int, n_seeded: int) -> list[Player]:
    players = [
        Player(
            number_id=f"#{i}",
            seed_id=i if i <= n_seeded else None
        )
        for i in range(1, n_players + 1)
    ]
    return players


# ==================================================================================================
# NOTE: fields_mapping: attributes-to-entry-fields
def load_players_from_json(
        json_path: str, 
        fields_mapping: dict[str, str]
) -> list[Player]:
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    players = [
        Player(
            **{key: entry.get(value) for key, value in fields_mapping.items()}
        )
        for entry in data
    ]
    return players

    # For [DEBUG]
    # players = []
    # for entry in data:
    #     class_attributes = {
    #         key: entry.get(value)
    #         for key, value in fields_mapping.items()
    #     }
    #     p = Player(**class_attributes)
    #     players.append(p)
    # return players


# ==================================================================================================
# NOTE: load_players_from_json2() is more flexibale utility function which accept "dynamic" mapping
def load_players_from_json2(
        json_path: str, 
        fields_mapping: dict[str, callable]
) -> list[Player]:
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    players = [
        Player(**{key: func(entry) for key, func in fields_mapping.items()})
        for entry in data
    ]
    return players

# --------------------------------------------------------------------------------------------------
# "dynamic" field mapping - which could be used for load_players_from_json2()
# if seeded are limited based on input
def make_fields_mapping_with_limit(
    base_mapping: dict[str, str],
    limits: dict[str, int] | None = None
) -> dict[str, callable]:
    limits = limits or {}
    result = {}

    for target_attr, source_key in base_mapping.items():
        if target_attr in limits:
            limit = limits[target_attr]
            result[target_attr] = lambda entry, sk=source_key, lim=limit: (
                entry[sk] if entry[sk] <= lim else None
            )
        else:
            result[target_attr] = lambda entry, sk=source_key: entry[sk]
    return result

# --------------------------------------------------------------------------------------------------
# "dynamic" field mapping - which could be used for load_players_from_json2()

def make_fields_mapping_with_1_to_many_fiels(
        fields_mapping: dict[str, str | tuple[str, ...]]
) -> dict[str, callable]:
    def build_callable(source):
        if isinstance(source, tuple):
            return lambda entry, keys=source: " ".join(entry[k] for k in keys)
        else:
            return lambda entry, k=source: entry[k]

    return {target: build_callable(source) for target, source in fields_mapping.items()}


# ==================================================================================================
def generate_seed_mappings(
        seeds_tiers: dict[int, list[int]],
        seeded_draw_positions: dict[int, list[int]],
        n_players: int,
        # n_seeded: int
) -> tuple[dict[int, tuple[list[int], list[int]]], list[int]]:
    
    all_seeded_positions = [pos for bracket in seeded_draw_positions.values() for pos in bracket]
    unseeded_positions = list(set(range(1, n_players + 1)) - set(all_seeded_positions))

    seed_tiers_positions = {}

    # NOTE: sorted() ensures that resulting dictionary is ordered even if seeds_tiers and seeded_draw_positions are not
    for tier in sorted(seeds_tiers):
        seeds_brackets = seeds_tiers[tier]
        seeds = list(range(seeds_brackets[0], seeds_brackets[1] + 1))
        positions = seeded_draw_positions[tier]
        seed_tiers_positions[tier] = seeds, positions
    return seed_tiers_positions, unseeded_positions


# ==================================================================================================
def make_draw(
        players: list[Player],
        seed_tiers_positions: dict[int, tuple[list[int], list[int]]],
        unseeded_positions: list[int],
        random_seed: int = 42
) -> dict[int, int]:
    
    random.seed(random_seed)

    # lookup dicts for seeded and unseeded players
    seeded_players = {p.seed_id: p for p in players if p.seed_id is not None}
    unseeded_players = {p.number_id: p for p in players}

    # seeded players
    for _, (seeds, positions) in seed_tiers_positions.items():
        random.shuffle(seeds)
        for s, pos in zip(seeds, positions):
            player = seeded_players.get(s)
            player.draw_position = pos

    # unseeded players
    unseeded_ids = [p.number_id for p in players if p.seed_id is None]
    random.shuffle(unseeded_ids)
    for pos, id in zip(unseeded_positions, unseeded_ids):
        player = unseeded_players.get(id)
        player.draw_position = pos

    # NOTE: version with BUG
    # # seeded players
    # for _, (seeds, positions) in seed_tiers_positions.items():
    #     random.shuffle(seeds)
    #     for s, pos in zip(seeds, positions):
    #         player = next((p for p in players if p.seed_id == s))
    #         player.draw_position = pos
    # # unseeded players
    # unseeded_ids = [p.number_id for p in players if p.seed_id is None]
    # random.shuffle(unseeded_ids)
    # pairs = zip(unseeded_positions, unseeded_ids)
    # for pos, id in pairs:
    #     player = next((p for p in players if p.number_id == id))
    #     player.draw_position = pos
    # # return None
