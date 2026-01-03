from abc import ABC, abstractmethod


class DocumentStoragePort(ABC):
    @abstractmethod
    def get(self, path: str) -> bytes: ...

    @abstractmethod
    def save(self, path: str, file: bytes) -> None: ...
