from enum import StrEnum


class IDType(StrEnum):
    TIME_SORTABLE = 'time-sortable'
    ALPHANUMERIC = 'alphanumeric'
    INTEGER = 'integer'