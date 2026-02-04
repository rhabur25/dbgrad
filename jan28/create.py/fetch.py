import sqlite3


conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
query = "SELECT playerID, yearID, teamID, HR
            FROM batting
            WHERE HR > 40"
cursor.execute(query)
results = cursor.fetchall()
conn.close()

print(records)