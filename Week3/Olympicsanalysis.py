import csv

# with open("Week3/results.csv", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     # Printing only the header and first 5 rows of data
#     for _ in range(6):
#         print(next(reader))

with open("Week3/results.csv", encoding="utf-8") as f:
        # pass the file object into the DictReader instead of the reader
        reader = csv.DictReader(f) # creates an iterable
        # now convert to list
        olympics_data = list(reader)

    # Print the first 5 rows of data
for index in range(5):
    print(olympics_data[index])

print(len(olympics_data))

# Get the gold medalists
gold_medals = []

for row in olympics_data:
    if row["Medal"] == "G":
        gold_medals.append(row)
print(f"""Out of {len(olympics_data)} total medals, this dataset 
contains information about {len(gold_medals)} gold medals""")

usa_2016_gold_medals = []

for row in olympics_data:
    if row["Medal"] == "G" and row["Nationality"] == "USA" and row["Year"] == "2016":
        usa_2016_gold_medals.append({"Event": row["Event"], "Name": row["Name"]})
print(usa_2016_gold_medals)

with open("usa_2016_gold_medals.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["Event", "Name"])
    writer.writeheader()
    for row in usa_2016_gold_medals:
        writer.writerow(row)