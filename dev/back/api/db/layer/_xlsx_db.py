from . import _xlsx_raw
from . import _rawdf_shapeddf
from . import _shapeddf_db

def _(*args, **kwargs):
    print("begin xlsx_db")
    _ = _xlsx_raw._()
    _ = _rawdf_shapeddf._(_)
    _ = _shapeddf_db._(_)
    print("end xlsx_db")