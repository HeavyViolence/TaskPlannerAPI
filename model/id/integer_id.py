from model.id.custom_id import CustomID

import secrets


class IntegerID(CustomID):
    def __init__(self, byte_length: int = CustomID.MIN_BYTE_LENGTH):
        super().__init__(byte_length)
        self._random_bytes = secrets.token_bytes(byte_length)

    def get_random_bytes(self) -> bytes:
        return self._random_bytes

    def __repr__(self):
        return f'{__class__.__name__}({self.byte_length})'

    def __str__(self):
        return f'{int.from_bytes(self.get_random_bytes(), byteorder='big', signed=False):,}'

    def __eq__(self, other):
        if not isinstance(other, IntegerID):
            return NotImplemented
        return self.get_random_bytes() == other.get_random_bytes()

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if not isinstance(other, IntegerID):
            return NotImplemented
        return self.get_random_bytes() < other.get_random_bytes()

    def __le__(self, other):
        if not isinstance(other, IntegerID):
            return NotImplemented
        return self.get_random_bytes() <= other.get_random_bytes()

    def __gt__(self, other):
        if not isinstance(other, IntegerID):
            return NotImplemented
        return self.get_random_bytes() > other.get_random_bytes()

    def __ge__(self, other):
        if not isinstance(other, IntegerID):
            return NotImplemented
        return self.get_random_bytes() >= other.get_random_bytes()

    def __hash__(self):
        return hash(self.get_random_bytes())