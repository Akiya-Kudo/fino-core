from fino_core.domain.entity.document import Document


class DocumentPathPolicy:
    def generate_path(self, document: Document) -> str:
        return f"{document.market.value.value}/{document.ticker.value}/{document.disclosure_type.value.value}/{document.document_id.value}"
