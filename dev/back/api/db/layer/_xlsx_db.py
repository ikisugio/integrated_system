from . import _xlsx_rawdf
from . import _rawdf_shapeddf
from . import _shapeddf_db


def _(full_path_xlsv, full_path_db):
    
    df_added_all, file_info  = _xlsx_rawdf._(full_path_xlsv)
    df_shaped, file_info = _rawdf_shapeddf._(df_added_all, file_info)
    _ = _shapeddf_db._(df_shaped, file_info, full_path_db)
    # print("PATH_xlsv => " + full_path_xlsv)
    # print("PATH_db => " + full_path_db)
    
    return None
