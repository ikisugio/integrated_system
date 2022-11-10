import util
from db import conf, xlsx_to_db


util.exec_in_folder(xlsx_to_db.main, conf.csv_folder_full_path)