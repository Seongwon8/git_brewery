import requests
import sqlite3

# 1. API 호출
url = 'https://api.openbrewerydb.org/v1/breweries'
response = requests.get(url)
data = response.json()

# 2. SQLite 연결
conn = sqlite3.connect("brewery.db")
cur = conn.cursor()

# 3. 테이블 생성
cur.execute('''
CREATE TABLE IF NOT EXISTS breweries (
    id TEXT PRIMARY KEY,
    name TEXT,
    brewery_type TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    longitude TEXT,
    latitude TEXT
)
''')

# 4. 데이터 삽입
for b in data:
    cur.execute('''
    INSERT OR REPLACE INTO breweries VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        b.get("id"),
        b.get("name"),
        b.get("brewery_type"),
        b.get("city"),
        b.get("state"),
        b.get("country"),
        b.get("longitude"),
        b.get("latitude")
    ))

conn.commit()
conn.close()

print("데이터 저장 완료!")
