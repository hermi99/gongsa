import sqlite3

from flask import Flask, render_template, request
import pandas as pd

from module.db_module import Database

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/map')
def map():
    # return render_template('map.html')

    # db_class = Database()
    # sql = "select * from guksa_table"
    # guksas = db_class.executeAll(sql)
    #
    # sql = "select * from gongsa_table"
    # gongsas = db_class.executeAll(sql)

    guksas = [{'GUKSA':'구로국사', 'ADDR':'서울특별시 관악구 조원중앙로1길(신림동 1660)', 'CENTER':'서울남부', 'LNG':'126.9029487', 'LAT':'37.48106781'},
              {'GUKSA': '수원국사', 'ADDR': '경기도 수원시 장안구 정조로 947 (영화동 306-1)', 'CENTER': '경기남부', 'LNG': '127.0113397', 'LAT': '37.29200017'}]

    return render_template('map.html', guksas=guksas)

@app.route('/map_edit')
def map_edit():
    return render_template('map_edit.html')


@app.route('/map_post', methods=["POST"])
def map_post():
    name = request.form['name']
    description = request.form['description']
    category = request.form['category']
    print(name, description, category)

    return 'name={}, desc={}, category={}'.format(name, description, category)


if __name__ == '__main__':
    app.run()
