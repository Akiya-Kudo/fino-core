from fino_core.domain.entity.document import Document
from fino_core.domain.repository.document import DocumentRepository, DocumentSearchCriteria
from fino_core.infrastructure.policy.document_path import DocumentPathPolicy
from fino_core.interface.port.document_storage import DocumentStoragePort


class DocumentRepositoryImpl(DocumentRepository):
    def __init__(self, storage: DocumentStoragePort) -> None:
        self._storage = storage
        self._path_policy = DocumentPathPolicy

    # FIXME: 実装
    def save(self, document: Document, file: bytes) -> None:
        path = self._path_policy.generate_path(document)
        self._storage.save(path=path, file=file)

    # FIXME: 実装
    def list(self, criteria: DocumentSearchCriteria) -> list[Document]:
        