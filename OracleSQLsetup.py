#WIP need to comment out script

import os
import subprocess

def check_directory(path):
    if not os.path.exists(path):
        print(f"Directory '{path}' does not exist.")
        return False
    if not os.path.isdir(path):
        print(f"'{path}' is not a valid directory path.")
        return False
    return True

def setup_oracle_database(directory):

    oracle_home = os.environ.get("ORACLE_HOME")
    if not oracle_home:
        print("ORACLE_HOME environment variable is not set. Make sure Oracle client is installed and configured.")
        return

    db_name = input("Enter the name of the Oracle database: ")
    username = input("Enter a username for the database: ")
    password = input("Enter a password for the database: ")

    try:
        subprocess.run([
            "dbca",
            "-silent",
            "-createDatabase",
            "-templateName", "General_Purpose.dbc",
            "-gdbname", db_name,
            "-sid", db_name,
            "-responseFile", f"{oracle_home}/assistants/dbca/templates/General_Purpose.dbc.rsp",
            "-SysPassword", password,
            "-SystemPassword", password,
            "-emConfiguration", "NONE",
            "-datafileDestination", directory,
            "-storageType", "FS"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print("Error creating Oracle database:", e)
        return

    print("Oracle database setup complete.")

def main():
    data_directory = input("Enter a local directory path for the database: ")

    if not check_directory(data_directory):
        return

    setup_oracle_database(data_directory)

if __name__ == "__main__":
    main()