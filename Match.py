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
