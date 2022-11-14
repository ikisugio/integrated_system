import os


def get_file_name_list(folder_path):
    
    file_name_list = os.listdir(folder_path)
    
    return file_name_list


def filter_list(obj_list, condition="all"): 
    
    filtered_list = obj_list
    
    if condition == "all":
        pass
    elif type(condition) is int:
        filtered_list = filtered_list[:condition]
        
    return filtered_list


def get_full_path_file(folder_path, file_name):
    return folder_path + file_name


def _(func_iter, folder_path, filter, db_path):
    
    file_name_list = get_file_name_list(folder_path)
    file_name_list_filtered = filter_list(file_name_list, filter)
    
    for file_name in file_name_list_filtered:
        full_path_file = get_full_path_file(folder_path, file_name)
        func_iter(full_path_file, db_path)
        
    return  None