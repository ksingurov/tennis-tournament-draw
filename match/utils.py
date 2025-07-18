# UTILS for Match class 
from match.core import Match
import json


def power_of_2(N: int) -> int | None:
    if N < 1:
        return None
    power = 0
    n = N
    while n > 1:
        if n % 2 != 0:
            return None
        n //= 2
        power += 1
    return power


def build_draw(players: list[int], max_rounds: str | int = 'all') -> list[Match]:
    num_rounds = power_of_2(len(players))
    if num_rounds == 0:
        raise ValueError("Number of players must be more than 1 to build a draw")
    if not num_rounds:
        raise ValueError("Number of players must be a power of 2 to build a valid draw")

    # created first round matches
    min_id = 1
    all_matches = []
    for i in range(0, len(players), 2):
        m = Match(match_id=min_id + i, _players_input=(players[i], players[i+1]))
        all_matches.append(m)

    # iteratively create matches for next rounds
    max_rounds = num_rounds if max_rounds == 'all' else max_rounds
    next_round = max_rounds - 1
    round_matches = all_matches
    min_id = len(all_matches) + 1
    while len(round_matches) > 1 and next_round > 1 and next_round <= max_rounds:
        next_round_matches = []
        for i in range(0, len(round_matches), 2):
            m = Match(match_id=min_id + i, top_match=round_matches[i], bottom_match=round_matches[i+1])
            next_round_matches.append(m)
        all_matches.extend(next_round_matches)
        round_matches = next_round_matches
        min_id = len(all_matches) + 1
        next_round -= 1
    
    return all_matches


def list_to_json(matches: list[Match]) -> str:
    return json.dumps([m.to_json() for m in matches])
