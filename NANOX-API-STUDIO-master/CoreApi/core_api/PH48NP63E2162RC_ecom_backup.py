import os
import subprocess
from datetime import datetime
def custom_api(db, data):
# Variables
    current_date = datetime.now().strftime("%d-%m-%Y-%H-%M %p")
    backup_dir = f"/Backup/ECOM/{current_date}"
    backup_log = "/Backup/ECOM/LOG"
    destination_dir = "/SK/CLOUDSERVER BACKUP/CENTOS/ECOM/"

    # Ensure backup directory exists
    os.makedirs(backup_dir, exist_ok=True)

    # Ensure log directory exists
    os.makedirs(backup_log, exist_ok=True)

    # Backup command
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M%p")

    backup_file = "{}/{}-{}.sql".format(backup_dir, db["db_user"], timestamp)
    dump_command = "PGPASSWORD='{}' pg_dump -U '{}' -d '{}' --schema '{}' > '{}' --verbose 2> '{}/ECOM-{}'".format(db["db_password"], db["db_user"], db["db_name"], db["db_user"], backup_file, backup_log, timestamp)
    subprocess.run(dump_command, shell=True, check=True)
    # return 
    # backup_file = f"{backup_dir}/{db["db_user"]}-{timestamp}.sql"
    # return backup_file
    # dump_command = f"PGPASSWORD='{db["db_password"]}' pg_dump -U '{db["db_user"]}' -d '{db["db_name"]}' --schema '{db["db_user"]}' > '{backup_file}' --verbose 2> '{backup_log}/ECOM-$TIMESTAMP'"
    # subprocess.run(dump_command, shell=True, check=True)

    # Move the backup directory to the destination directory
    subprocess.run(["mv", backup_dir, destination_dir], check=True)
    
    return {"message": "Successfully completed"}
