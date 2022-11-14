from conf import info
from . import _iter_in_folder
from . import _xlsx_db


def _(folder_path, filter, db_path):
    
    _iter_in_folder._(
        _xlsx_db._,
        folder_path,
        filter,
        db_path,
    )
    
    return None