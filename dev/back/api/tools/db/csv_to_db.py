import csv
import sqlite3


def db_write():
    pass

#folderが平坦化されている前提で(not recursive)
csv_folder_path = "../../data/csv/"
target_folder_path = "2022_06/"
dest_db_name = "name:fake"

conn = sqlite3.connect(dest_db_name)
db_write()
conn.close()