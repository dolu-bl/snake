# -*- coding: utf-8 -*-

from enum import Enum, auto

def getSetting(settings, value, defaultValue):
    if settings.__contains__(value):
        return settings[value]
    return defaultValue

class Direction(Enum):
    Up = auto()
    Right = auto()
    Down = auto()
    Left = auto()
