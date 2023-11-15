import pandas as pd
import numpy as np
from scipy.stats import norm
import warnings
import numpy as np
from unidecode import unidecode
import pandas as pd
from django.db import connection
warnings.filterwarnings('ignore')
from django.conf import settings
from .models import *

    
class DataProcessor:
    def __init__(self, file) -> None:
        filename = file.name.strip()
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            self.df = pd.read_excel(file, skiprows=8, skipfooter=2, header=[0])
        elif filename.endswith(".csv"):
            self.df = pd.read_csv(file, skiprows=8, skipfooter=2, header=[0])
        self.df.replace(np.nan, -1, inplace=True)
        self.df['Mã sinh viên'] = self.df['Mã sinh viên'].astype(int).astype(str)
        
    def get_subject_credit(self):
        df = self.df.drop(columns=['STT', 'Mã sinh viên', 'Họ đệm', 'Tên', 'Học lực'], axis=0)
        df.drop(columns=df.columns[-6:], axis=0, inplace=True)
        return df.iloc[0].to_dict()
    
    def get_all_student_detail(self, class_name):
        first_col = self.df.columns[1]
        last_col = self.df.columns[-7:-2]
        df = self.df[[first_col] + list(last_col)]
        df.columns = df.iloc[0]
        df.drop(index=0, inplace=True)
        df.columns = ['student_id', 'passed_credit', 'score_10', 'score_4', 'score_char', 'rank']
        res = df.to_dict(orient='records')
        
        df = self.df[['Mã sinh viên', 'Họ đệm', 'Tên']].drop(index=0)
        df.columns = ['student_id', 'first_name', 'lastname']
        df['student_name'] = df['first_name'] + " " + df['lastname']
        df['last_name2'] = df.apply(lambda x: unidecode(x['lastname'].lower()), axis=1)
        df['student_gmail'] = df.apply(lambda x: f"{x['lastname']}.{x['student_id']}@iuh.edu.vn", axis=1)
        df.drop(columns=['first_name', 'last_name2'], inplace=True)
        data = df.to_dict(orient='records')
        
        dict1_map = {d['student_id']: d for d in data}
        res = [dict({**d, **dict1_map.get(d['student_id'], {})}) for d in res]
        result_df = pd.DataFrame(res)
        result_df['class_name'] = class_name
        res = result_df.to_dict(orient='records')
        
        Student.objects.bulk_create([Student(
            student_id=d['student_id'],
            passed_credit=d['passed_credit'],
            score_10=d['score_10'],
            score_4=d['score_4'],
            score_char=d['score_char'],
            rank=d['rank'],
            lastname=d['lastname'],
            student_name=d['student_name'],
            student_gmail=d['student_gmail'],
            class_name=class_name
        ) for d in res])    
        
        return True


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
    