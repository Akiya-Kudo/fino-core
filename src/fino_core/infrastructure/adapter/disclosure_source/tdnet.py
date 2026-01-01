from fino_core.domain.entity.disclosure_source import DisclosureSource
from fino_core.domain.entity.document import Document
from fino_core.domain.value.document_id import DocumentId
from fino_core.domain.value.document_search_criteria import DocumentSearchCriteria
from fino_core.interface.port.disclosure_source import DisclosureSourcePort


# FIXME: TODO: 実装
class TDNetAdapter(DisclosureSourcePort):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def get_source(self) -> DisclosureSource:
        return DisclosureSource(
            source_id="edinet",
            name="EDINET",
        )

    def list_available_documents(self, criteria: DocumentSearchCriteria) -> list[Document]:
        return []

    def download_document(self, document_id: DocumentId) -> bytes:
        return b""
