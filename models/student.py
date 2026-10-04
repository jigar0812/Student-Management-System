from dataclasses import dataclass
@dataclass
class Student:
    name:str; roll_no:str; email:str; course:str; id:int|None=None
