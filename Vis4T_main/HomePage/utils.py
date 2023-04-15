import pandas as pd

def query_student_data_with_ordinal_data(student_data, column_name):
    df = pd.DataFrame(student_data)
    new_df = df.groupby(column_name).aggregate({'student_id': 'count'}).rename(columns={'student_id': 'count'})
    return new_df.to_dict()

def get_student_final_score(student_data, score_type='score_10'):
    df = pd.DataFrame(student_data)
    df = df[['student_name', score_type]].set_index('student_name')
    return df.to_dict()[score_type]