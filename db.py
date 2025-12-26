import sqlite3

def init_db():
    conn = sqlite3.connect('productivity.db')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   description TEXT,
                   duration INTEGER
                   )
                   ''')



def add_activity(date, description, duration):
    conn = sqlite3.connect('productivity.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO activities (date, description, duration) VALUES (?, ?, ?)',
        (date, description, duration)
    )

    conn.commit()
    conn.close()


def get_activities():
    conn = sqlite3.connect("productivity.db")
    cursor = conn.cursor()

    cursor.execute("SELECT date, description, duration FROM activities")
    rows = cursor.fetchall()

    conn.close()

    activities = []
    for r in rows:
        activities.append({
            "date": r[0],
            "description": r[1],
            "duration": r[2]
        })
    return activities