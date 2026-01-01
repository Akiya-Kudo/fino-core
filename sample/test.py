from fino_core.domain.entity.disclosure_source import DisclosureSource
from fino_core.interface.facade.config.storage import LocalConfig
from fino_core.interface.facade.document_collector import DocumentCollector

_ = DocumentCollector(
    disclosure_source=DisclosureSource(
        source_id="test-source-id",
        name="test-disclosure-source",
    ),
    storage_config=
)
