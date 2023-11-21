import numpy as np
from unidecode import unidecode
import pandas as pd
import os, json
from .postgres_tools import PostgresTools

vi2en = {
    "Mã sinh viên": "student_id",
    "Họ đệm": "first_name",
    "Tên": "last_name",
    "Điểm tổng kết": "score",
    "Điểm 10": "score_10",
    "Điểm 4": "score_4",
    "Điểm chữ": "score_char",
    "Số tín chỉ": "passed_credit",
    "Xếp loại": "rank",
}

class DataProcessor():
    def __init__(self, path_excel, class_name='KHDL16A'):
        self.path_excel = path_excel
        self.class_name = class_name
        self.df = pd.read_excel(self.path_excel, skiprows=8, skipfooter=2, header=[0])

    def get_student(self):
        '''
        class_name là tên lớp học khi giáo viên thêm lớp mới nhập vào.
        '''
        pg = PostgresTools()
        cols = pg.get_columns('Student')
        pg.close()
        #-- get data
        df_student = self.df.iloc[1:, 1:4]
        df_score = self.df.iloc[:, -7:-2]
        df_score.columns = self.df.iloc[0, -7:-2]
        df_score = df_score[1:]
        df_concat = pd.concat([df_student, df_score], axis=1)
        df_concat.rename(columns=vi2en, inplace=True)
        df_concat['student_id'] = df_concat['student_id'].astype(int)
        df_concat['student_name'] = df_concat['first_name'] + " " + df_concat['last_name']
        df_concat.rename(columns={'last_name': 'lastname'}, inplace=True)
        df_concat['student_gmail'] = df_concat[['student_id', 'lastname']].apply(lambda x: f"{x['student_id']}.{unidecode(x['lastname'].lower())}@iuh.edu.vn", axis=1)
        df_concat['class_name_id'] = self.class_name
        df_concat['is_graduated'] = False
        df_concat = df_concat[cols]
        return df_concat

    def get_subject_student(self):
        # -- get subject and subject_id
        pg = PostgresTools()
        id_subject = pg.query('SELECT * FROM "Subject"', False)
        subject2id = {subject: id for id, subject in id_subject}
        cols = pg.get_columns('Subject_student')
        pg.close()
        # -- process
        df_student = self.df.iloc[1:, 1:2]
        df_score = self.df.iloc[1:, 4:-7]
        df_concat = pd.concat([df_student, df_score], axis=1)
        df_concat.rename(columns=vi2en, inplace=True)
        df_concat['student_id'] = df_concat['student_id'].astype(int)
        df_concat = pd.melt(df_concat, id_vars=['student_id'], value_vars=list(df_concat.columns[1:])).rename(columns={'variable': 'subject_name', 'value': 'score_10'})
        df_concat['subject_name'] = df_concat['subject_name'].apply(lambda x: x.strip().lower())
        df_concat['subject_id'] = df_concat['subject_name'].map(subject2id)
        df_concat = df_concat[cols[1:]]
        return df_concat

    def get_subject_class(self):
        pg = PostgresTools()
        cols = pg.get_columns('Subject_class')
        id_subject = pg.query('SELECT * FROM "Subject"', False)
        subject2id = {subject: id for id, subject in id_subject}
        pg.close()
        #-- get data
        df_header = self.df.iloc[:1]
        subject_names = df_header.columns[4:-7]
        credits = df_header.values[0][4:-7]
        df_subject = pd.DataFrame({'subject_id': subject_names, 'credit': credits})
        df_subject['subject_id'] = df_subject['subject_id'].apply(lambda x: x.strip().lower()).map(subject2id)
        df_subject['credit'] = df_subject['credit'].map(int)
        df_subject['class_name_id'] = self.class_name
        df_subject['semester_id'] = None
        df_subject['is_mandatory'] = False
        df_subject = df_subject[cols[1:]]
        return df_subject
