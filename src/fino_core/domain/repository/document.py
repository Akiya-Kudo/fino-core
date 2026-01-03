from abc import ABC, abstractmethod
from typing import Protocol

from fino_core.domain.entity.document import Document
from fino_core.domain.value.format_type import FormatType
from fino_core.domain.value.market import Market


class DocumentSearchCriteria(Protocol):
    market: Market  # @propertyではなく、フィールドとして
    format_type: FormatType


class DocumentRepository(ABC):
    @abstractmethod
    def exists(self, document: Document) -> bool: ...

    @abstractmethod
    def save(self, document: Document, file: bytes) -> None: ...
