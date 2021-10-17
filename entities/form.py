from dataclasses import dataclass


@dataclass
class Form:
    throws: str
    pitch_speed_kmh: float
    pitch_speed_mph: float
    pitch_type: str
