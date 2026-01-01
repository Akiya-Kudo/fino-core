from fino_core.interface.port.document_storage import DocumentStoragePort


class LocalStorage(DocumentStoragePort):
    def __init__(self, absolute_path: str) -> None:
        self.absolute_path = absolute_path

    def save(self, document: Document, file: bytes) -> None:
        with open(self.absolute_path, "wb") as f:
            f.write(file)

    def get(self, document: Document) -> bytes:
        with open(self.absolute_path, "rb") as f:
            return f.read()
