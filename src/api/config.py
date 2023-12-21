from dataclasses import dataclass, field

from src.infrastructure.db.config import DBConfig
from src.infrastructure.log.config import LoggingConfig


@dataclass
class APIConfig:
    host: str = "127.0.0.1"
    port: int = 5000
    debug: bool = __debug__


@dataclass
class Config:
    db: DBConfig = field(default_factory=DBConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    api: APIConfig = field(default_factory=APIConfig)
