from dbconn.conf import Database
from dbconn.engine import Engine, Executable


class PsqlExecutable(Executable):
    def get_command(db: Database, host: str | None = None, port: int | None = None):
        return [
            "psql",
            "-U",
            db.user,
            "--host",
            host or db.host,
            "--port",
            str(self.port),
            "--db",
            db.database,
        ]


class PgcliExecutable(Executable):
    def get_command(db: Database, host: str | None = None, port: int | None = None):
        return [
            "pgcli",
            "-U",
            db.user,
            "--host",
            host or db.host,
            "--port",
            str(port or self.port),
            "--dbname",
            db.database,
        ]


class PostgresEngine(Engine):
    supported_executables = {
        "psql": PsqlExecutable,
        "pgcli": PgcliExecutable,
    }
    default_executable = "pgcli"
    default_port = 5432
