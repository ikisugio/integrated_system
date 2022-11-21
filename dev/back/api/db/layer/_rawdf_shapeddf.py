

def shape_df(df_added):
    
    # id = care_office_number + "_" + care_service_code
    # df_added = df_added.assign(id=care_service_code)
    df_shaped = df_added
    print()
    
    return df_shaped


def _(df_added_all, file_info):
    
    df_shaped = shape_df(df_added_all)
    
    return df_shaped, file_info