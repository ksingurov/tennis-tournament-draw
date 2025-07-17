from __future__ import annotations
from dataclasses import dataclass, asdict
import json
from typing import Optional


@dataclass
class Match:
    match_id: Optional[int] = None # default None or not?
    top_match: Optional[Match] = None
    bottom_match: Optional[Match] = None
    winner: Optional[int] = None
    _players_input: Optional[tuple[Optional[int], Optional[int]]] = None  # manually assigned for leaves

    def __repr__(self):
        parts = []
        if self.match_id is not None:
            parts.append(f"match_id={self.match_id}")
        if self.top_match is not None:
            parts.append(f"top_match=Match(match_id={self.top_match.match_id})")
        if self.bottom_match is not None:
            parts.append(f"bottom_match=Match(match_id={self.bottom_match.match_id})")
        if self.winner is not None:
            parts.append(f"winner={self.winner}")
        if self._players_input is not None:
            parts.append(f"players={self._players_input}")
        return f"Match({', '.join(parts)}"

    @property
    def players(self):
        if self.top_match is None and self.bottom_match is None:
            return self._players_input or (None, None)
        top_winner = self.top_match.winner if self.top_match else None
        bottom_winner = self.bottom_match.winner if self.bottom_match else None
        return top_winner, bottom_winner
    
    @players.setter
    def players(self, value: tuple[int, int]):
        if self.top_match is not None or self.bottom_match is not None:
            raise ValueError("It is not possible to manually assign players to non-leaf matches")
        if not all(isinstance(x, int) for x in value):
            raise ValueError("Each player must be an int")
        self._players_input = value
    
    @classmethod
    def from_json(cls, data: str) -> Match:
        return cls(**json.loads(data))
    
    def to_json(self):
        return json.dumps(asdict(self))


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


if __name__ == "__main__":
    N = 8
    players = list(range(1, N + 1))
    draw = build_draw(players=players, max_rounds=1)
    for m in draw:
        print(m)

