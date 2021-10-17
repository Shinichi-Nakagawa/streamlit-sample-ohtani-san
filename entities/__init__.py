from enum import Enum


class AtBat(Enum):
    """
    打撃結果のステータス
    """
    READY = 0
    HOME_RUN = 4
    OUTS = -1


class Throw(Enum):
    """
    利き腕
    """
    R = 'R'
    L = 'L'


class PitchType(Enum):
    """
    球種
    """
    CH = 'CH'
    CS = 'CS'
    CU = 'CU'
    EP = 'EP'
    FA = 'FA'
    FC = 'FC'
    FF = 'FF'
    FS = 'FS'
    FT = 'FT'
    KC = 'KC'
    KN = 'KN'
    SC = 'SC'
    SI = 'SI'
    SL = 'SL'
