import os
import subprocess

import dotenv

from common.helper import helper

dotenv.load_dotenv("postgres/.env")


class Postgres:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST")
        self.port = int(os.getenv("POSTGRES_PORT", "5432"))
        self.database = os.getenv("POSTGRES_DATABASE")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")

    def backup(self, folder_backup_location, file_name):
        backup_file_name = f"{file_name}_{helper.current_timestamps()}.sql"
        backup_file_location = f"{folder_backup_location}/{backup_file_name}"

        # Set the PGPASSWORD environment variable to provide the password
        os.environ['PGPASSWORD'] = self.password

        subprocess.run(
            [
                "pg_dump",
                "--column-inserts",
                "--no-owner",
                f"--host={self.host}",
                f"--port={self.port}",
                f"--dbname={self.database}",
                f"--username={self.user}",
                f"--file={backup_file_location}"
            ]
        )
        return backup_file_location
