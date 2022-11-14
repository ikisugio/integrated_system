import os


def return_swap_dict(d):
    return {v: k for k, v in d.items()}

def connect_db(db_path):
    return None

def get_xlsx_folder_path(data_axis_path, xlsx_folder_relative_path):
    xlsx_folder_full_path = data_axis_path + xlsx_folder_relative_path
    return xlsx_folder_full_path

def get_xlsx_path(data_axis_path, xlsx_name, xlsx_folder_relative_path):
    xlsx_full_path = get_xlsx_folder_path(data_axis_path, xlsx_folder_relative_path) + xlsx_name
    return xlsx_full_path

def get_db_path(data_axis_path, db_name):
    db_full_path = data_axis_path + db_name
    return db_full_path

def get_df_db_dict(versus_db_df):
    versus_df_db = get_swap_dict(versus_db_df)
    return versus_df_db

def get_file_name_list(folder_path):
    file_name_list = os.listdir(folder_path)
    return file_name_list

# 未完成 condition でフィルターする部分 現状MOCK
def filter_list(obj_list, condition="all"):
    filtered_list = list
    if condition == "all":
        filtered_list = obj_list
    return filtered_list

def iter_in_list(func, list):
    for elem in list:
        func(elem)
    return None

def iter_in_folder(func, folder_path, condition="all"):
    file_name_list_in_folder = get_file_name_list(folder_path)
    file_name_list_filtered = filter_list(file_name_list_in_folder, condition)
    iter_in_list(func, file_name_list_filtered)
    return None