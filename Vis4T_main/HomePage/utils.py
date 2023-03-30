import pandas as pd

def query_student_data_with_nominal_data(student_data, column_name):
    df = pd.DataFrame(student_data)
    new_df = df.groupby(column_name).aggregate({'student_id': 'count'}).rename(columns={'student_id': 'count'})
    return new_df.to_dict()