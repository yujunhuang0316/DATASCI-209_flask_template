from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def w209():
    file='about9.jpg'
    return render_template('w209.html',file=file)

@app.route('/api')
def api():
    return {"x": 666}

@app.route('/players/count')
def player_count():
    conn = sqlite3.connect('players_20.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    count = cursor.fetchone()[0]
    conn.close()
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run()