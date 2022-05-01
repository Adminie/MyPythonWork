import sqlite3
import datetime
from flask import Flask,render_template, request
DATABASE = 'data/data.db'
app = Flask(__name__)
@app.route("/")
def hello():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("SELECT * FROM sensorlog WHERE sensorid =1")
    data = cur.fetchall()
    cur.close()
    db.close()
    temp1 = data[len(data) - 1]
    temp=temp1[2]
    return render_template('vews.html', data=data,temp=temp)

#Adding data
@app.route("/input",methods=['POST','GET'])
def add_data():
    if request.method == 'POST':
        sensorid = int(request.form.get('id'))
        sensorvalue = float(request.form.get('val'))
    else:
        sensorid = int(request.args.get('id'))
        sensorvalue = float(request.args.get('val')) 
    nowtime = datetime.datetime.now()
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("INSERT INTO sensorlog(sensorid,sensorvalue,updatetime) VALUES(%d,%f,'%s')" %(sensorid,sensorvalue,nowtime) )
    db.commit()
    cur.execute("SELECT * FROM sensorlist where sensorid = %d"% sensorid)
    rv = cur.fetchall()
    cur.close()
    db.close()
    maxrv = rv[0][2]
    minrv = rv[0][3]
    if sensorvalue > maxrv or sensorvalue < minrv:
        return '1'
    else:
        return '0'

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000)
