import pandas as pd
import numpy as np
from scipy.stats import norm

def kde_line(data_dict, h, num_points = 50):
    data = np.array(list(data_dict.values()))
    std = h * np.std(data)
    x = np.linspace(np.min(data), np.max(data), num_points)
    y = np.zeros_like(x)
    for i in range(len(x)):
        kde_i = 0
        for j in range(len(data)):
            kde_i += norm.pdf((x[i] - data[j]) / std)
        y[i] = kde_i / (len(data) * std)
    return [[x[i], y[i]] for i in range(len(x))]

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
    df.to_dict()[score_type]
    return df.to_dict()[score_type]