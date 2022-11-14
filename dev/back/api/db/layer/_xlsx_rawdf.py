import pandas as pd


def extract_care_service_code(xlsx_full_path):
    
    def trim_prev_and_post(
            target_string, 
            boundary_token, 
            digit_of_code):
        index_start_boundary = target_string.find(boundary_token)
        
        return target_string[:index_start_boundary][-digit_of_code:]


    CHAR_CODE_FULL_WIDTH_SPACE = '\u3000'
    DIGIT_OF_CARE_SERVICE_CODE = 3
    
    care_service_code = trim_prev_and_post(
        xlsx_full_path,
        CHAR_CODE_FULL_WIDTH_SPACE,
        DIGIT_OF_CARE_SERVICE_CODE,
    )
    
    return care_service_code


def get_file_info(xlsx_full_path):
    
    file_name = xlsx_full_path[xlsx_full_path.rfind("/")+1:]
    folder_path = xlsx_full_path[:xlsx_full_path.rfind("/")+1]
    parent_folder_path = folder_path[:folder_path[:-1].rfind("/")+1]
    file_info = {
        "file_name": file_name,
        "folder_path": folder_path,
        "parent_folder_path": parent_folder_path
    }
    
    return file_info


def add_column(raw_df, xlsx_full_path):
    
    care_service_code = extract_care_service_code(xlsx_full_path)
    df_added_id = raw_df.assign(id=care_service_code)
    df_added_all = df_added_id
    
    return df_added_all


def _(xlsx_full_path): 
    
    raw_df = pd.read_excel(xlsx_full_path)
    df_added_all = add_column(raw_df, xlsx_full_path)
    file_info = get_file_info(xlsx_full_path)
    
    return df_added_all, file_info
