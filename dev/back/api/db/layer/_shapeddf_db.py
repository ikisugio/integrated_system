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
    # SessionClass = sessionmaker(engine)
    # session = SessionClass()
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
    
    # office = Office()
    
    def insert(data):

        office = Office()
        SessionClass = sessionmaker(engine)
        session = SessionClass()

        # print("insert_info => ", data["No"])
        office_id = str(data["No"]).zfill(10) + "_" + data["care_service_code"]
        office_address = data["住所"] + str(data["方書（ビル名等）"])
        capacity = data["定員"]
        # capacity = data["定員"].fillna(0).astype('int64')
        # office_test.id = office_id
        print("insert_id => ", office_id)
        # print("insert_name => ", data["事業所名"])
        # print("insert_town_code => ", data["都道府県コード又は市町村コード"])
        # print("insert_address => ", office_address)
        # print("insert_company => ", data["法人の名称"])
        # print("insert_latitude => ", data["緯度"])
        # print("insert_longitude => ", data["経度"])
        # print("insert_phone => ", data["電話番号"])
        # print("insert_fax => ", data["FAX番号"])
        # print("insert_url => ", data["URL"])
        # print("insert_capacity => ", capacity)
        # print("insert_care_service_code => ", data["care_service_code"])
        # print("insert_care_office_code => ", data["No"])

        office.id = office_id
        office.name = data["事業所名"]
        office.town_code = data["都道府県コード又は市町村コード"]
        office.address = office_address
        office.company = data["法人の名称"]
        office.latitude = data["緯度"]
        office.longitude = data["経度"]
        office.phone = data["電話番号"]
        office.fax = data["FAX番号"]
        office.url = data["URL"]
        office.capacity_of_guests = capacity
        office.care_office_code = data["No"]
        office.care_service_code = data["care_service_code"]

        session.add(office)
        session.commit()
        session.close()
    
    
    i = 0
    for index, data in df.iterrows():
        insert(data)
        i += 1
        # if i == 1000:
        #     break
    

    return None


def _(df, df_info, db_path):
    # df_db(df, df_info)
    db_connect(db_path, df, df_info)
    
    return None