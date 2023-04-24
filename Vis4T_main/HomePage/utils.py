import pandas as pd

def query_student_data_with_ordinal_data(student_data, column_name):
    df = pd.DataFrame(student_data)
    res = {}
    try:
        stats_ = df[column_name].value_counts().to_dict()
        keys = None
        if column_name == "score_char":
            keys = ['A+', 'A ', 'B+', 'B ', 'C+', 'C ', 'D+', 'D ', 'F ']
        elif column_name == "rank":
            keys = ['Xuất sắc', 'Giỏi', 'Khá', 'Trung bình', 'Trung bình yếu']
    except:
        return 
        
    stats = {key: (stats_[key] if key in stats_.keys() else 0) for key in keys}
    res['count'] = stats
    return res

def get_student_final_score(student_data, score_type='score_10'):
    df = pd.DataFrame(student_data)
    df = df[['student_name', score_type]].set_index('student_name')
    return df.to_dict()[score_type]