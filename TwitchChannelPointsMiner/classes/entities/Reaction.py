
from enum import Enum
import random


class Reaction(Enum):
    HYPE = "HYPE",
    FUNNY = "FUNNY",
    LOVE = "LOVE",
    WHAAAT = "WHAAAT",
    OH_NO = "OH_NO",

class ReactionSettings:
    def __init__(self, reactions: list[Reaction] = 
                 [Reaction.HYPE, Reaction.FUNNY, Reaction.LOVE, Reaction.WHAAAT, Reaction.OH_NO],
                 interval_s: int = 300):
        self.reactions = reactions
        self.interval_s = interval_s
        
    def select_reaction(self):
        return random.choice(self.reactions)