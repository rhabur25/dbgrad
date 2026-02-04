import csv

# Read the batting.csv file
with open('batting.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Print the data
for player in data:
    print(player)

print(f"\nTotal players: {len(data)}")
