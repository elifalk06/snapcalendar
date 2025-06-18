from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta
import os
import dateparser

app = Flask(__name__)
DATABASE = 'calendar.db'

# Ensure database exists

def init_db():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS events
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        start DATETIME,
                        reminder_minutes INTEGER)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS preferences
                       (category TEXT PRIMARY KEY,
                        reminder_minutes INTEGER)''')
        con.commit()

init_db()

def get_events():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute('SELECT id, title, start, reminder_minutes FROM events ORDER BY start')
        return cur.fetchall()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['events']
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        for line in lines:
            # parse line like "Meeting at 2pm tomorrow"
            dt = dateparser.parse(line, settings={'PREFER_DATES_FROM': 'future'})
            if dt:
                title = line.replace(str(dt.date()), '').strip()
                with sqlite3.connect(DATABASE) as con:
                    con.execute('INSERT INTO events (title, start, reminder_minutes) VALUES (?, ?, ?)',
                                (title or line, dt.isoformat(), get_default_reminder('default')))
        return redirect(url_for('index'))
    events = get_events()
    return render_template('index.html', events=events)

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'POST':
        category = request.form['category']
        minutes = int(request.form['minutes'])
        with sqlite3.connect(DATABASE) as con:
            con.execute('REPLACE INTO preferences (category, reminder_minutes) VALUES (?, ?)',
                        (category, minutes))
        return redirect(url_for('preferences'))
    prefs = get_preferences()
    return render_template('preferences.html', prefs=prefs)

def get_default_reminder(category):
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute('SELECT reminder_minutes FROM preferences WHERE category=?', (category,))
        row = cur.fetchone()
        return row[0] if row else 60  # default 60 minutes


def get_preferences():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute('SELECT category, reminder_minutes FROM preferences')
        return cur.fetchall()

if __name__ == '__main__':
    app.run(debug=True)
