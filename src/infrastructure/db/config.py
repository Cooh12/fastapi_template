from dataclasses import dataclass


@dataclass
class DBConfig:
    type_: str = 'postgresql'
    connector: str = 'asyncpg'
    host: str = "localhost"
    port: int = 5432
    login: str = ""
    password: str = ""
    database: str = ""
    echo: bool = False

    @property
    def full_url(self) -> str:
        return f'{self.type_}+{self.connector}://{self.login}:{self.password}@{self.host}:{self.port}/{self.database}'
