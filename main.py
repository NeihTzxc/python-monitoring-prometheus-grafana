import sys

from common.helper import helper
from common.notification.telegram import Telegram
from mysql.mysql import Mysql
from postgres.postgres import Postgres


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py backup postgres")
        sys.exit()

    action = sys.argv[1]

    if action == "backup_postgres":
        postgres = Postgres()
        folder_backup_location = "/tmp"
        file_name = "bida-api"
        try:
            postgres.backup(folder_backup_location, file_name)
            print("PostgresSQL backup completed successfully.")
            telegram = Telegram()
            telegram.send_message(
                f"PostgresSQL backup completed successfully: {file_name} at: {helper.current_date_and_time()}")
        except Exception as e:
            print(f"An error occurred during the backup: {str(e)}")
    elif action == "backup_mysql":
        mysql = Mysql()
        folder_backup_location = "/tmp"
        file_name = "bida-api"
        try:
            mysql.backup(folder_backup_location, file_name)
            print("MySQL backup completed successfully")
            telegram = Telegram()
            telegram.send_message(
                f"MySQL backup completed successfully: {file_name} at: {helper.current_date_and_time()}"
            )
        except Exception as e:
            print(f"An error occurred during the backup: {str(e)}")
    else:
        print("Back up is invalid")


if __name__ == "__main__":
    main()
