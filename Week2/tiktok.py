countries = ["America", "Canada", "Australia", "China", "Chile"]
# for c in countries:
#     if c.startswith("C"):
#         countries.remove(c)
# print(countries)

# using list comprehension
countries = [c for c in countries if not c.startswith("C")]
# this will create a new list with only the countries that do not start with "C"
print(countries)