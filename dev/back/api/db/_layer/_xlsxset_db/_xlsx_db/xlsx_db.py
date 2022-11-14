import info
import util

def read_xlsx(path):
    unshaped_df = None
    return unshaped_df

def shape_df(df):
    shaped_df = None
    return shaped_df

def inject_db(df):
    def connect_db():
        return info.connect_db()
    def commit_db(df):
        return None
    def disconnect_db():
        return None
    connect_db()
    commit_db(df)
    disconnect_db
    return None


def from_xlsx_to_db(xlsx_name, db_name):
    xlsx_path = info.return_xlsx_path(xlsx_name)
    db_path = info.return_db_path(db_name)
    raw_df = read_xlsx(xlsx_path)
    shaped_df = shape_df(raw_df)
    inject_db(shaped_df, db_path)