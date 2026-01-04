from abc import ABC, abstractmethod

from fino_core.domain.entity.document import Document
from fino_core.domain.value.format_type import FormatType


class DocumentRepository(ABC):
    @abstractmethod
    def exists(self, document: Document, format_type: FormatType) -> bool: ...
    @abstractmethod
    def save(self, document: Document, file: bytes) -> None: ...
