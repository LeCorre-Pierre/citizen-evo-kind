from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Individual:
    name: str
    surname: str
    gender: str  # "Male" or "Female"
    age: int
    max_age: int
    job: Optional[str] = None  # None if child, else job name
    injuries: int = 0
    hunger: int = 100
    skills: Optional[Dict[str, int]] = None
    position: Optional[Dict[str, float]] = None  # {"x": float, "y": float}
    destination: Optional[Dict[str, int]] = None  # {"x": int, "y": int}
    speed: float = 1.0
