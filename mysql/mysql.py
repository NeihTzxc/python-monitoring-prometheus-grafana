import os
import subprocess

import dotenv

from common.helper import helper

dotenv.load_dotenv("mysql/.env")


class Mysql:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.port = os.getenv("MYSQL_PORT")
        self.database = os.getenv("MYSQL_DATABASE")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")

    def backup(self, folder_backup_location, file_name):
        backup_file_name = f"{file_name}_{helper.current_timestamps()}.sql"
        backup_file_location = f"{folder_backup_location}/{backup_file_name}"

        try:
            subprocess.run([
                'mysqldump',
                f"--host={self.host}",
                f"--user={self.user}",
                f"--password={self.password}",
                f"--databases={self.database}",
                f"--result-file={backup_file_location}"
            ])
            return backup_file_location
        except Exception as e:
            print(f"An error occurred during the backup: {str(e)}")
        finally:
            print("FINALLY")
