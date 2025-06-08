from abc import ABC, abstractmethod


class CustomID(ABC):
    MIN_BYTE_LENGTH: int = 8
    MAX_BYTE_LENGTH: int = 32

    def __init__(self, byte_length: int):
        if byte_length < self.MIN_BYTE_LENGTH:
            raise ValueError(f"Byte length must be at least {self.MIN_BYTE_LENGTH} bytes!")
        if byte_length > self.MAX_BYTE_LENGTH:
            raise ValueError(f"Byte length must be at most {self.MAX_BYTE_LENGTH} bytes!")
        self._byte_length = byte_length

    @property
    def byte_length(self) -> int:
        return self._byte_length

    @abstractmethod
    def get_random_bytes(self) -> bytes:
        pass

    def total_unique_tokens(self) -> int:
        return 256 ** self.byte_length

    def global_unique_tokens(self) -> int:
        return int(self.total_unique_tokens() ** 0.5)

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass