from abc import ABC, abstractmethod
from typing import Protocol

from fino_core.domain.entity.document import Document


class DocumentSearchCriteria(Protocol): ...


class DocumentRepository(ABC):
    @abstractmethod
    def save(self, document: Document, file: bytes) -> None: ...

    @abstractmethod
    def list(self, criteria: DocumentSearchCriteria) -> list[Document]: ...
