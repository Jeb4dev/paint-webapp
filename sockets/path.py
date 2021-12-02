from dataclasses import dataclass


@dataclass
class Point:
    px: float
    py: float
    x: float
    y: float
    color: str
    width: int
    tool: str
    fulfill: bool
