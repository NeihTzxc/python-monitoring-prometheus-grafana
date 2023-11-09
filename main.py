import sys

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
        except Exception as e:
            print(f"An error occurred during the backup: {str(e)}")
    else:
        print("Invalid action, Use 'backup_postgres'")


if __name__ == "__main__":
    main()
