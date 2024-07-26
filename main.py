import requests
import sqlite3

# 1. API İsteği Gönderme
url = "https://cat-fact.herokuapp.com/facts"
response = requests.get(url)
cat_facts = response.json()

# 2. SQLite Veritabanı Oluşturma
conn = sqlite3.connect('cat_facts.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS facts (
    id TEXT PRIMARY KEY,
    text TEXT
)
''')
conn.commit()

# 3. Veri Kaydetme
for fact in cat_facts:
    c.execute('''
    INSERT OR IGNORE INTO facts (id, text)
    VALUES (?, ?)
    ''', (fact['_id'], fact['text']))
conn.commit()
conn.close()

# 4. Veri Görüntüleme
conn = sqlite3.connect('cat_facts.db')
c = conn.cursor()
c.execute('SELECT * FROM facts')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
