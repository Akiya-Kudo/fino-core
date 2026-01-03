from typing import Generic, Protocol, TypeVar

from fino_core.domain.entity.disclosure_source import (
    DisclosureSource as DisclosureSource,
)
from fino_core.domain.entity.document import Document
from fino_core.domain.repository.document import DocumentSearchCriteria
from fino_core.domain.value.document_id import DocumentId

TCriteria = TypeVar("TCriteria", bound=DocumentSearchCriteria, contravariant=True)


class DisclosureSourcePort(Protocol, Generic[TCriteria]):
    def list_available_documents(self, criteria: TCriteria) -> list[Document]: ...
    def download_document(self, document_id: DocumentId) -> bytes: ...
