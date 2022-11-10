import os


def get_swap_dict(d):
    return {v: k for k, v in d.items()}

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

def exec_in_folder(func, folder_path, condition="all"):
    file_name_list_in_folder = get_file_name_list(folder_path)
    file_name_list_filtered = filter_list(file_name_list_in_folder, condition)
    iter_in_list(func, file_name_list_filtered)
    return None