import os
import sqlite3
import pandas as pd


def db_write():
    pass

#folderが平坦化されている前提で(not recursive)
data_axis_path = "../../../"
csv_folder_relative_path = "origin_data/csv/2022_06/"
db_name = "db.sqlite3"

csv_folder_full_path = data_axis_path + csv_folder_relative_path
db_full_path = data_axis_path + db_name



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

def get_swap_dict(d):
    return {v: k for k, v in d.items()}

versus_df_db = get_swap_dict(versus_db_df)


def create_dataframe(i):
    index_space_in_name = csv_file_name_list[i].find('\u3000')
    care_service_code = csv_file_name_list[0][:index_space_in_name]
    column_to_add = pd.DataFrame({'ADDED': range(len(df))})
    
    df = pd.read_excel(csv_folder_full_path + csv_file_name_list[i])
    df = df.assign(id=care_service_code)

    for row in len(df):
        care_office_code = df.loc[row]["No"]
        id = care_office_code + "@" + care_service_code
        df.loc[row][""]
        # address = "string:fake"


#CSVから読み込み
csv_file_name_list = os.listdir(csv_folder_full_path)
df_cluster = list()
for csv_file_name in csv_file_name_list:
    create_dataframe(csv_file_name)



stamp_set = set()
stamp_set.add("")

conn = sqlite3.connect(db_full_path)
db_write()
conn.close()