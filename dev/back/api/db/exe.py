from conf import info
from util import funcs
from layer import _xlsxset_to_db

xlsx_folder_full_path = funcs.get_xlsx_folder_path(
    info.DATA_AXIS_PATH,
    info.XLSX_FOLDER_RELATIVE_PATH
)
db_path = funcs.get_db_path(
    info.DATA_AXIS_PATH,
    info.DB_NAME
)
filter = 1


def _():
    print("XLSX_FOLDER_FULL_PATH = " + xlsx_folder_full_path)
    # FUNC_TO_EXE(FOLDER_PATH_TO_EXE)
    _xlsxset_to_db._(xlsx_folder_full_path, filter, db_path)


if __name__ == '__main__':
    _()