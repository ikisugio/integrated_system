import os
import sqlite3
import pandas as pd
import conf


# 副作用が生じないよう、copyを操作しそれを返す
def injection_df(data, df, row_number, column_name):
    copied_df = df
    copied_df.at[row_number, column_name] = data
    return copied_df

def extract_prev(target_string, boundary_token):
    index_start_boundary = target_string.find(boundary_token)
    return target_string[:index_start_boundary]


def create_dataframe(i):
    care_service_code = extract_prev(csv_file_name_list[i], '\u3000')
    
    df = pd.read_excel(csv_folder_full_path + csv_file_name_list[i])
    df = df.assign(id=care_service_code)
    df['id'] = ''

    for row in len(df):
        # digit_care_office_code について
        # 介護労働保険番号の桁数 厚生労働省の指定に依存する
        # 2022年11月現在は10桁で指定されている
        digit_care_office_code = 10
        care_office_code = str(df.loc[row]["No"]).zfill(digit_care_office_code)
        id = care_office_code + "_" + care_service_code
        # dfの'id'列にidをセットする
        id_injected_df = injection_df(id, df, row, 'id')

for csv_file_name in csv_file_name_list:
    create_dataframe(csv_file_name)


def main():
    pass

stamp_set = set()
stamp_set.add("")

conn = sqlite3.connect(db_full_path)
db_write()
conn.close()