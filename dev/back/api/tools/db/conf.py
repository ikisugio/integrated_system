import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .. import util

#folderが平坦化されている前提で(not recursive)
data_axis_path = "../../../"
csv_folder_relative_path = "origin_data/csv/2022_06/"
db_name = "db.sqlite3"

versus_db_df = {
    "name": "事業所名",
    "postal_code": "郵便番号",
    "address": "住所",
    "longitude": "経度",
    "latitude": "緯度",
    "url": "URL",
    "company": "法人の名称",
    "fax": "FAX番号",
    "phone": "電話番号",
}

versus_df_db = util.get_swap_dict(versus_db_df)

csv_folder_full_path = data_axis_path + csv_folder_relative_path
db_full_path = data_axis_path + db_name