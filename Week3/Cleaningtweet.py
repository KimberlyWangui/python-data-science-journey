free_text = "\t       Mary had a littl0e lamb and th0en I ate it \n "
print(free_text)

cleaned_free_text = free_text.strip().replace('0', '').lower()
print(cleaned_free_text)

token_list = cleaned_free_text.split()
print(token_list)

# Joining the list of tokens back into a string
joined_text = ' '.join(token_list)
print(joined_text)
