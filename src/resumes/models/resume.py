from typing import NamedTuple

class Resume(NamedTuple):
    Id: int
    CityId: int
    City: str
    PositionId: int
    Title: str
    Salary: int
    Currency: str
    Specialization: list[str]
    ExperienceDuration: str
    Languages: list[str]
    Skills: list[str]
    DateUpdate: str
    Url: str
