import enum


class WalkState(enum.Enum):
    RELAX = False
    WALK = True


class MinState(enum.Enum):
    STOP = False
    PLAY = True


class GeneralGawsState(enum.Enum):
    HIDDEN = False
    NOTABLE = True


class EndingsStates(enum.Enum):
    NOT_END = 0
    FAIL_END = 7
    CANON_END = 8
    BORING_END = 9
    FUN_END = 10
