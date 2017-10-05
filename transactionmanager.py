from flask import Flask, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '20083156'
app.config['MYSQL_DATABASE_DB'] = 'tran_app'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'



@app.route('/')
def index():
    transactons = [
        {
            'name': 'Make web site in Flask',
            'id' : 1,
            'sum' : 45000,
            'note': 'Make site with BlackJack and hore'
        },
        {
            'name': 'Craete app',
            'id': 2,
            'sum': 15000,
            'note': 'Make site for android'
        }
    ]
    return render_template("index.html",
                           transactons = transactons)

@app.route('/show/<id>')
def show(id):
    return 'Id page is ' + id

if __name__ == '__main__':
    app.run(debug=True)
