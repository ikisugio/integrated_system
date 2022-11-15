import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker


def df_csv(df, df_info):
    parent_folder_path = df_info["parent_folder_path"]
    csv_name_to_save = parent_folder_path + "csv_test/" + "office.csv"
    df.to_csv(csv_name_to_save, sep=",", mode='w', header=True)
    
    return None


def db_connect(db_path):
    # con = sqlite3.connect(db_name)
    print("connected " + db_path)
    engine = create_engine('sqlite:///../../db.sqlite3', echo=True)
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    Base = declarative_base(bind=engine)

    class Office(Base):  # クラス名は何でもok
        __tablename__ = "api_office"
        __table_args__ = {"autoload": True}

    # offices = session.query(Office).all()
    insert_info = {
        "id": "test_id2",
        "name": "test_name2",
        "company": "test_company2",
        "care_office_code": "test_office_code2",
        "care_service_code": "test_service_code2",
    }
    office_test = Office()
    office_test.id = insert_info["id"]
    office_test.name = insert_info["name"]
    office_test.company = insert_info["company"]
    office_test.care_office_code = insert_info["care_office_code"]
    office_test.care_service_code = insert_info["care_service_code"]
    session.add(office_test)
    session.commit()

    return None


def _(df, df_info, db_path):
    df_csv(df, df_info)
    db_connect(db_path)
    
    return None