import csv

track_times = [
    [13.10, 13.59, 13.44],
    [13.93, 13.85, 13.47],
    [14.12, 14.41, 13.89],
    [14.42, 13.55, 13.43]
]

# Initialize an empty string
track_times_csv = ""

# Loop over all lists in the overall list
for index, athlete_times in enumerate(track_times):

    # Join together the values in the nested list using a comma separator
    athlete_times_string = ",".join([str(time) for time in athlete_times])

    # Append values to the overall string
    track_times_csv += athlete_times_string

    # Append a newline, unless this is the last row
    if index < len(track_times) - 1:
        track_times_csv += "\n"

print(track_times_csv)

# Writing the string to a file
with open("track_times.csv", "w") as file:
    file.write(track_times_csv)

track_times_from_disk = []
with open("track_times.csv") as f:
    # iterate over list of lines. each line is a string
    for row in f:
        # list comprehesion to split row into a list on delimiter and convert each value to a float
        # and iterate over all elements converting them to float
        times= [float(time) for time in row.split(",")]

        # append to row (now a list of floats) to outer list
        track_times_from_disk.append(times)

print(track_times_from_disk)

# Using the csv module to write to a file
with open("track_times.csv") as f:

    # Pass the file in to a "reader" object and specify that values without explicit quotes (i.e. all values in this
    # dataset) should be treated as numbers
    # return reader object that can act as an iterator
    # each element of the iterator contains a fully processed line as a list with types already converted
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

    # Get all of the data from the reader using `list`
    # list() explicitly converts iterator to a list
    track_times_with_csv_module = list(reader)

print(track_times_with_csv_module)

