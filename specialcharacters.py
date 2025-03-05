import re 
def contains_special_characters(s):
    return bool(re.search(r'[^a-zA-z0-9]',s))

print(contains_special_characters("Hello@World"))  #True
print(contains_special_characters("Hello123"))   #False