def inject_df(df, df_info, db_name):
    
    parent_folder_path = df_info["parent_folder_path"]
    csv_name_to_save = parent_folder_path + "csv_test/" + "office.csv"
    df.to_csv(csv_name_to_save, sep=",", mode='a', header=False)
    
    return None


def _(df, df_info, db_name):
    
    inject_df(df, df_info, db_name)
    
    return None