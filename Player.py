from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional
import json


@dataclass
class Player:
    name: Optional[str] = None
    seed: Optional[int] = None
    draw_position: Optional[int] = None

    @classmethod
    def from_json(cls, data: str) -> Player:
        return cls(**json.loads(data))
    
    def to_json(self):
        return json.dumps(asdict(self))
