import os
import sqlite3

basedir = os.path.abspath(os.getcwd())
db_path = os.path.join(basedir, 'instance', 'risklens.db')
print('db_path=', db_path)
print('exists=', os.path.exists(db_path))
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='assets'")
row = cur.fetchone()
print('assets table sql=', row[0] if row else None)
con.close()

from app import create_app
app = create_app()
with app.app_context():
    client = app.test_client()
    payload = {
        'name': 'Metasploitable',
        'target': '192.168.56.101',
        'ip_address': '192.168.56.101',
        'description': 'Practice VM'
    }
    res = client.post('/assets', json=payload)
    print('status', res.status_code)
    print('body', res.get_data(as_text=True))
