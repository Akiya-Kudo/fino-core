from dataclasses import dataclass

from fino_core.domain.entity.document import Document


# Finoのデータレイクストレージのパス構造に合わせたポリシー
# @see: .cursor/rules/project.mdc#Storage Rules
@dataclass(frozen=True, slots=True)
class DocumentPathPolicy:
    """文書のパスを生成するポリシー"""

    document: Document

    @property
    def folder(self) -> str:
        return f"{self.document.market.value}/{self.document.ticker.value}/{self.document.disclosure_type.value}"

    @property
    def filename(self) -> str:
        return (
            f"{self.document.document_id.value}_{self.document.disclosure_date.value.isoformat()}"
        )

    @staticmethod
    def generate_path(document: Document) -> str:
        return f"{document.market.value}/{document.ticker.value}/{document.disclosure_type.value}/{document.document_id.value}_{document.disclosure_date.value.isoformat()}"  # noqa: E501
