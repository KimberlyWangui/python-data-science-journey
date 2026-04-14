exo_data = [
    ['Name', 'Distance (LY)', 'Orbital Period (Days)', 'Number of Moons', 'Habitable Zone', 'Potential for Liquid Water'],
    ['Kepler-186f', '512', '136', '1', 'True', 'High'],
    ['TRAPPIST-1d', '40', '4.05', '0', 'True', 'High'],
    ['Gliese 581 g', '20', '37', '0', 'False', 'Possible'],
    ['LHS 1140b', '40.5', '38.1', '0', 'False', 'Possible'],
    ['KOI-3140b', '178', '4.5', '0', 'False', 'Low'],
    ['Kepler-1708b', '5600', '131', '2', 'False', 'None'],
    ['Kepler-452b', '1400', '385', '0', 'False', 'Likely'],
    ['Kepler-10b', '186', '0.8', '0', 'False', 'None'],
    ['HD 132563 b', '218', '259.4', '1', 'False', 'Possible'],
    ['Kepler-442b', '1120', '112', '0', 'False', 'Possible']
]

# Dealing with Integers
# loop over words. Keep track of index so we can skip the first row
for ix, row in enumerate(exo_data):
    if ix > 0: #  this skips the header row
        row[3] = int(row[3]) # this converts the number of moons to an integer

print(type(exo_data[6][3]) is int) # this checks if the number of moons for Kepler-1708b is an integer

lqwater = []
for i, elem in enumerate(exo_data):
    if i > 0: # skip header
        lqwater.append(elem[5]) # this appends the potential for liquid water to a new list

print(lqwater)

value_mapper = {'None': 0, 'Low': 1, 'Possible': 2, 'Likely': 3, 'High': 4}
for i, elem in enumerate(exo_data):
    if i > 0: # skip header
        elem[5] = value_mapper[elem[5]] # this maps the potential for liquid water to a numerical value

print(exo_data)