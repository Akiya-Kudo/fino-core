from fino_core.domain.entity.document import Document
from fino_core.interface.port.document_storage import StoragePort


# FIXME: TODO: 実装
class S3Storage(StoragePort):
    def __init__(self, bucket_name: str, region: str, prefix: str) -> None:
        self.bucket_name = bucket_name
        self.region = region
        self.prefix = prefix

    def save(self, document: Document, file: bytes) -> None:
        pass

    def get(self, document: Document) -> bytes:
        pass
