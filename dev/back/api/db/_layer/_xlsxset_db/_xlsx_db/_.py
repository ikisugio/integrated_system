import _Xlsx_RawDf._ as Xlsx_RawDf
import _RawDf_ShapedDf._ as RawDf_ShapedDf
import _ShapedDf_Db._ as ShapedDf_Db

def _(*args, **kwargs):
    xlsx_rawdf = Xlsx_RawDf._(*args, **kwargs)
    rawdf_shapeddf = RawDf_ShapedDf._(xlsx_rawdf)
    shapeddf_db = ShapedDf_Db._(rawdf_shapeddf)