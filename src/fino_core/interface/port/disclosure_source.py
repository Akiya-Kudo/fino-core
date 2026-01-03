from typing import Protocol

from fino_core.domain.entity.document import Document
from fino_core.domain.repository.document import DocumentSearchCriteria
from fino_core.domain.value.document_id import DocumentId
from fino_core.domain.value.format_type import FormatType


class DisclosureSourcePort(Protocol):
    """開示ソースからドキュメントを取得するポート

    各実装は、DocumentSearchCriteriaのサブタイプ（例: EdinetDocumentSearchCriteria）を
    受け取ることができますが、ProtocolとしてはDocumentSearchCriteriaとして定義します。
    これにより、型変数の分散の問題を回避できます。
    """

    def list_available_documents(
        self, criteria: DocumentSearchCriteria
    ) -> list[Document]: ...
    def download_document(
        self, document_id: DocumentId, format_type: FormatType
    ) -> bytes: ...
