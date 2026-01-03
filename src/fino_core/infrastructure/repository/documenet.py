from typing import Optional

from fino_core.domain.entity.document import Document
from fino_core.domain.repository.document import DocumentRepository, DocumentSearchCriteria
from fino_core.domain.value.document_id import DocumentId
from fino_core.interface.port.document_storage import DocumentStoragePort


class DocumentRepositoryImpl(DocumentRepository):
    def __init__(self, storage: DocumentStoragePort) -> None:
        self.storage = storage

    def get(self, document_id: DocumentId) -> Optional[Document]:
        return self.storage.get()

    # FIXME: 実装
    def save(self, document: Document, file: bytes) -> None:
        pass

    # FIXME: 実装
    def list(self, criteria: DocumentSearchCriteria) -> list[Document]:
        return []
