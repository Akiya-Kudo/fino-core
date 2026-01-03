from abc import ABC, abstractmethod


class DocumentStoragePort(ABC):
    @abstractmethod
    def exists(self, path: str) -> bool: ...

    @abstractmethod
    def save(self, path: str, file: bytes) -> None: ...
