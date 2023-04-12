from typing import NamedTuple

class Position(NamedTuple):
    Id: int
    ParentId: int
    Level: int
    Title: str
    ProfArea: str
    OtherNames: str
    