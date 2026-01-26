from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int           
    b: float = 1.1   
    c = 'spam'       

from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)