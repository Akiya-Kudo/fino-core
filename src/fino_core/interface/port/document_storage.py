from abc import ABC, abstractmethod


class DocumentStoragePort(ABC):
    @abstractmethod
    def get(self, key: str) -> bytes: ...

    @abstractmethod
    def save(self, key: str, file: bytes) -> None: ...
