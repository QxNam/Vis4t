import psycopg2
from tabulate import tabulate
from .configs import *

class PostgresTools():
    def __init__(self, host=HOST, user=USER, port=PORT, password=PASSWORD, database=DATABASE):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            port=port,
            password=password
        )
        self.cur = self.conn.cursor()
    
    def close(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql_query, show=True):
        self.cur.execute("ROLLBACK")
        self.cur.execute(sql_query)
        if show:
            rows = self.cur.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in self.cur.description], tablefmt='psql'))
        else:
            return self.cur.fetchall()
        
    def get_columns(self, table_name):
        self.cur.execute("ROLLBACK")
        self.cur.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{table_name}'".format(table_name=table_name))
        cols = [i[0] for i in self.cur.fetchall()]
        return cols
