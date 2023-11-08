import os
import subprocess

import dotenv

from common.helper import helper

dotenv.load_dotenv(".env")


class Postgres:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST")
        self.port = int(os.getenv("POSTGRES_PORT")) or 5432
        self.database = os.getenv("POSTGRES_DATABASE")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")

    def backup(self, folder_backup_location, file_name):
        backup_file_name = f"{file_name}_{helper.current_timestamps()}.sql"
        backup_file_location = f"{folder_backup_location}/{backup_file_name}"
        subprocess.run(
            [
                "pg_dump",
                f"--host={self.host}",
                f"--port={self.port}",
                f"--dbname={self.database}",
                f"--username={self.user}",
                f"--file={backup_file_location}"
            ]
        )
        return backup_file_location
