from dataclasses import dataclass

from fino_core.domain.entity.document import Document
from fino_core.domain.value.document_id import DocumentId
from fino_core.domain.value.market import Market
from fino_core.interface.config.disclosure import EdinetConfig
from fino_core.interface.port.disclosure_source import DisclosureSourcePort
from fino_core.util import TimeScope


@dataclass(frozen=True, slots=True, kw_only=True)
class EdinetDocumentSearchCriteria:
    market: Market
    timescope: TimeScope


# FIXME: TODO: 実装
class EdinetAdapter(DisclosureSourcePort[EdinetDocumentSearchCriteria]):
    def __init__(self, config: EdinetConfig) -> None:
        self.api_key = config.api_key

    def list_available_documents(
        self, criteria: EdinetDocumentSearchCriteria
    ) -> list[Document]:
        return []

    def download_document(self, document_id: DocumentId) -> bytes:
        return b""
