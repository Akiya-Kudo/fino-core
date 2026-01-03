from abc import ABC, abstractmethod
from typing import Optional, Protocol

from fino_core.domain.entity.document import Document
from fino_core.domain.value.document_id import DocumentId


class DocumentSearchCriteria(Protocol): ...


class DocumentRepository(ABC):
    @abstractmethod
    def get(self, document_id: DocumentId) -> Optional[Document]: ...

    @abstractmethod
    def save(self, document: Document, file: bytes) -> None: ...

    @abstractmethod
    def list(self, criteria: DocumentSearchCriteria) -> list[Document]: ...
