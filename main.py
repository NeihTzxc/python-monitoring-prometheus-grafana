import datetime
import subprocess
import os

# Define the database details
DATABASE_NAME = 'mydatabase'
DATABASE_HOST = 'localhost'
DATABASE_PORT = 5432
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'password'

# Define the backup file path
BACKUP_PATH = "./backups"

# Create the backup file name
back_up_file_name = f"{DATABASE_NAME}-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.sql"

# Construct the backup command
backup_command = f"pg_dump -h {DATABASE_HOST} -p {DATABASE_PORT} -U {DATABASE_USER} -d {DATABASE_NAME} > {BACKUP_PATH}{back_up_file_name}"
subprocess.call(backup_command)
print(f"Database backup completed successfully: {BACKUP_PATH}{back_up_file_name}")
