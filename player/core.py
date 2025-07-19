from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional
import json


@dataclass
class Player:
    name: Optional[str] = None
    number_id: Optional[str] = None    # a chip/ball number in the pot for drawing
    seed_id: Optional[int] = None
    draw_position: Optional[int] = None

    # NOTE: when creating an instance either name or number should be non-empty
    def __post_init__(self):
        if not self.name and not self.number_id:
            raise ValueError("Either 'name' or 'number' must be provided to create Player instance")

    @classmethod
    def from_json(cls, data: str) -> Player:
        return cls(**json.loads(data))
    
    def to_json(self):
        return json.dumps(asdict(self))
