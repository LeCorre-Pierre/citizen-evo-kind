from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Cell:
    x: int
    y: int
    type: str  # "Green", "Dirt", "Town"
    occupied: bool = False
    resource: Optional[str] = None  # "plant", "mineral", "wheat", etc.
    growth: Optional[int] = None
    mine: Optional[bool] = None

@dataclass
class MapData:
    width: int
    height: int
    cells: List[Cell] = None
