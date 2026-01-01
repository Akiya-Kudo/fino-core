from fino_core.infrastructure.adapter.storage.local import LocalStorage
from fino_core.infrastructure.adapter.storage.s3 import S3Storage
from fino_core.interface.port.document_storage import DocumentStoragePort
from fino_core.public.config.storage import LocalConfig, S3Config


def create_storage(config: LocalConfig | S3Config) -> DocumentStoragePort:
    if isinstance(config, LocalConfig):
        return LocalStorage(config)
    else:
        return S3Storage(config)
