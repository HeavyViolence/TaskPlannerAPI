from model.id.custom_id import CustomID

import secrets
import base64
import time

class TimeSortableID(CustomID):
    TIME_BYTES: int = 8
    MIN_RANDOM_BYTES: int = 2

    def __init__(self, byte_length: int = CustomID.MIN_BYTE_LENGTH):
        super().__init__(byte_length)
        self._time_bytes = time.time_ns().to_bytes(self.TIME_BYTES, "big", signed=False)
        self._random_bytes = secrets.token_bytes(max(byte_length - self.TIME_BYTES, self.MIN_RANDOM_BYTES))

    def get_time_bytes(self) -> bytes:
        return self._time_bytes

    def get_random_bytes(self) -> bytes:
        return self._random_bytes

    def get_timestamp_ns(self) -> int:
        return int.from_bytes(self.get_time_bytes(), "big", signed=False)

    def __repr__(self):
        return f'{__class__.__name__}({self.byte_length})'

    def __str__(self):
        return base64.b85encode(self.get_time_bytes() + self.get_random_bytes()).decode('ascii')

    def __eq__(self, other):
        if not isinstance(other, TimeSortableID):
            return NotImplemented
        return (self.get_time_bytes() == other.get_time_bytes() and
                self.get_random_bytes() == other.get_random_bytes())

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if not isinstance(other, TimeSortableID):
            return NotImplemented
        if self.get_time_bytes() != other.get_time_bytes():
            return self.get_time_bytes() < other.get_time_bytes()
        return self.get_random_bytes() < other.get_random_bytes()

    def __le__(self, other):
        if not isinstance(other, TimeSortableID):
            return NotImplemented
        if self.get_time_bytes() != other.get_time_bytes():
            return self.get_time_bytes() <= other.get_time_bytes()
        return self.get_random_bytes() <= other.get_random_bytes()

    def __gt__(self, other):
        if not isinstance(other, TimeSortableID):
            return NotImplemented
        if self.get_time_bytes() != other.get_time_bytes():
            return self.get_time_bytes() > other.get_time_bytes()
        return self.get_random_bytes() > other.get_random_bytes()

    def __ge__(self, other):
        if not isinstance(other, TimeSortableID):
            return NotImplemented
        if self.get_time_bytes() != other.get_time_bytes():
            return self.get_time_bytes() >= other.get_time_bytes()
        return self.get_random_bytes() >= other.get_random_bytes()

    def __hash__(self):
        return hash((self.get_time_bytes, self.get_random_bytes()))