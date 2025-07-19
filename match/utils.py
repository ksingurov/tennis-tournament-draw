# UTILS for Match class 
from .core import Match
import json
import math


def build_tournament(players: list[int], max_rounds: int | None = None) -> list[Match]:
    n = len(players)
    if n == 1:
        raise ValueError("Number of players must be more than 1 to build a draw")
    if n <= 0 and (n & (n - 1)) != 0:
        raise ValueError("Number of players must be a power of 2 to build a valid draw")
    if max_rounds is not None and max_rounds < 1:
        raise ValueError("max_rounds must be a positive integer")

    num_rounds = int(math.log2(n))
    max_rounds = max_rounds or num_rounds
    all_matches = []
    round_matches = []
    for round_n in range(1, num_rounds + 1):
        min_id = len(all_matches) + 1
        if round_n == 1:
            for match_id, i in enumerate(range(0, len(players), 2), start=min_id):
                m = Match(
                    match_id=match_id,
                    _players_input=(players[i], players[i+1])
                )
                round_matches.append(m)
            all_matches.extend(round_matches)
        elif round_n <= max_rounds and len(round_matches) > 1:
            next_round_matches = []
            for match_id, i in enumerate(range(0, len(round_matches), 2), start=min_id):
                m = Match(
                    match_id=match_id,
                    top_match=round_matches[i],
                    bottom_match=round_matches[i+1]
                )
                next_round_matches.append(m)
            all_matches.extend(next_round_matches)
            round_matches = next_round_matches
        else:
            break
    return all_matches


def list_to_json(matches: list[Match]) -> str:
    return json.dumps([m.to_json() for m in matches])
