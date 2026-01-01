from dataclasses import dataclass

from fino_core.domain.entity.document import Document


@dataclass(frozen=True, slots=True)
class ListDocumentOutput:
    available_documents: list[Document]
    stored_documents: list[Document]
