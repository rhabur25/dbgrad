import sqlite3
import csv

# Create connection to database
conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

# Create batting table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS batting (
        playerID TEXT,
        Name TEXT,
        Team TEXT,
        Position TEXT,
        G INTEGER,
        AB INTEGER,
        R INTEGER,
        H INTEGER,
        "2B" INTEGER,
        "3B" INTEGER,
        HR INTEGER,
        RBI INTEGER,
        BB INTEGER,
        SO INTEGER,
        SB INTEGER,
        CS INTEGER,
        BA REAL,
        OBP REAL,
        SLG REAL,
        OPS REAL
    )
''')

# Read CSV and insert data
with open('batting.csv', 'r') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, 1):
        cursor.execute('''
            INSERT INTO batting (playerID, Name, Team, Position, G, AB, R, H, "2B", "3B", HR, RBI, BB, SO, SB, CS, BA, OBP, SLG, OPS)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (i, row['Name'], row['Team'], row['Position'], int(row['G']), int(row['AB']), 
              int(row['R']), int(row['H']), int(row['2B']), int(row['3B']), int(row['HR']), 
              int(row['RBI']), int(row['BB']), int(row['SO']), int(row['SB']), int(row['CS']), 
              float(row['BA']), float(row['OBP']), float(row['SLG']), float(row['OPS'])))

conn.commit()
conn.close()

print("Database 'baseball.db' created successfully with batting table!")
