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


def df_db(df, df_info):
    i = 0
    for index, data in df.iterrows():
        print("index => ", index)
        print("No => ", data["No"])
        print("======================")
        i += 1
        if i == 1:
            break
    
    return None


def db_connect(db_path, df, df_info):
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
    # insert_info = {
    #     "id": "test_id2",
    #     "name": "test_name2",
    #     "company": "test_company2",
    #     "care_office_code": "test_office_code2",
    #     "care_service_code": "test_service_code2",
    # }
    
    office_test = Office()
    
    def insert(data):
        # office_test = Office()
        
        # print("insert_info => ", data["No"])
        office_id = str(data["No"]) + "_" + data["care_service_code"]
        office_address = data["方書（ビル名等）"]
        # office_test.id = office_id
        print("insert_id => ", office_id)
        print("insert_name => ", data["事業所名"])
        print("insert_company => ", data["法人の名称"])
        print("insert_care_office_code => ", data["No"])
        print("insert_care_service_code => ", data["care_service_code"])
        print("insert_address => ", data["住所"])
        print("insert_town_code => ", data["都道府県コード又は市町村コード"])
        print("insert_latitude => ", data["緯度"])
        print("insert_longitude => ", data["経度"])
        print("insert_owner => ", data["経度"])
        # office_test.name = data["name"]
        # office_test.company = data["company"]
        # office_test.care_office_code = data["care_office_code"]
        # office_test.care_service_code = data["care_service_code"]
        # session.add(office_test)
        # session.commit()
    
    
    i = 0
    for index, data in df.iterrows():
        insert(data)
        i += 1
        if i == 10:
            break
    

    return None


def _(df, df_info, db_path):
    # df_db(df, df_info)
    db_connect(db_path, df, df_info)
    
    return None