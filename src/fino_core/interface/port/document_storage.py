from abc import ABC, abstractmethod

from fino_core.domain.entity.document import Document


class DocumentStoragePort(ABC):
    @abstractmethod
    def save(self, document: Document, file: bytes) -> None: ...

    @abstractmethod
    def get(self, document: Document) -> bytes: ...
