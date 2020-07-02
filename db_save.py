import os
import sqlite3

import pandas as pd
import pymysql

from sqlalchemy import create_engine

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()


db_file = 'db/database.db'
db_conn = sqlite3.connect(db_file)


def save_to_db():
    excel_file = "./자료/국사자료.xlsx"
    df = pd.read_excel(excel_file, sheet_name=0, header=0)
    df.to_sql('guksa_table', db_conn, if_exists="replace")

def save_to_mysql_db():
    engine = create_engine("mysql+mysqldb://root:" + "kt95000#" + "@211.107.85.60/gongsa", encoding='utf-8')
    # conn = engine.connect()
    #
    # db = pymysql.connect(host='211.107.85.60',
    #                      port=3306,
    #                      user='root',
    #                      passwd='kt95000#',
    #                      db='gongsa',
    #                      charset='utf8')
    # cursor = db.cursor()

    # # 1. 국사
    # excel_file = "./자료/국사자료.xlsx"
    # df = pd.read_excel(excel_file, sheet_name=0, header=0)
    # df.to_sql('guksa_table', engine, if_exists="replace")

    # 2. 공사장
    excel_file = "./자료/공사장자료.xlsx"
    df = pd.read_excel(excel_file, sheet_name=0, header=0)
    df.to_sql('gongsa_table', engine, if_exists="replace")


if __name__ == '__main__':
    save_to_mysql_db()
