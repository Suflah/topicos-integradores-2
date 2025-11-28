from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'clients.db'

def init_db():
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  name TEXT NOT NULL, 
                  email TEXT, 
                  phone TEXT)''')
    conn.commit()
    conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

def get_db_conn():
    if 'db' not in g:
        g.db = sqlite3.connect(str(DB_PATH))
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

init_db()

@app.route('/')
def index():
    conn = get_db_conn()
    clients = conn.execute('SELECT * FROM clients ORDER BY id DESC').fetchall()
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()

        if name:
            conn = get_db_conn()
            conn.execute(
                'INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)',
                (name, email, phone)
            )
            conn.commit()
            return redirect(url_for('index'))

    return render_template('add_client.html')

@app.route('/delete/<int:client_id>', methods=['POST'])
def delete(client_id):
    conn = get_db_conn()
    conn.execute('DELETE FROM clients WHERE id = ?', (client_id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    conn = get_db_conn()

    if not query:
        clients = conn.execute('SELECT * FROM clients ORDER BY id DESC').fetchall()
    else:
        clients = conn.execute(
            """
            SELECT * FROM clients
            WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?
            ORDER BY id DESC
            "",
            (f"%{query}%", f"%{query}%", f"%{query}%")
        ).fetchall()

    return render_template('index.html', clients=clients)

@app.route('/count')
def count_clients():
    conn = get_db_conn()
    total = conn.execute('SELECT COUNT(*) AS total FROM clients').fetchone()['total']
    return {"total_clients": total}

if __name__ == '__main__':
    app.run(debug=True)
