import csv

with open("text.csv", "r") as data:
    reader = csv.DictReader(data)
    rows = list(reader)


alma_mater_list = [row["Alma Mater"] for row in rows]
print(alma_mater_list)

alma_dtype = []

for elem in alma_mater_list:
    alma_dtype.append(type(elem))

print(alma_dtype)

print(alma_mater_list[0] == alma_mater_list[9])

alma_mater_list = [elem.strip() for elem in alma_mater_list]
print(alma_mater_list)

cleaned_list = []

for elem in alma_mater_list:
    cleaned_list.append(elem.title())

print(cleaned_list)

name_list = [row["Name"] for row in rows]
print(name_list)

cleaned_names = [elem.replace('@', '').replace('#', '') for elem in name_list]
print(cleaned_names)
