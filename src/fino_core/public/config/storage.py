from pydantic import BaseModel, field_validator


class LocalConfig(BaseModel):
    absolute_path: str


class S3Config(BaseModel):
    bucket_name: str
    region: str
    prefix: str | None = None

    @field_validator("prefix", mode="after")
    def validate_absolute_path(self) -> str:
        if not self.prefix:
            return ""
        return self.prefix.strip()
