#1
import re
def match_ab(string):
    pattern = 'ab*'
    if re.match(pattern, string):
        return True
    return False
#2
def match_abb(string):
    pattern = 'ab{2,3}'
    if re.match(pattern, string):
        return True
    return False
#3
def find_sequences(string):
    pattern = '[a-z]+_[a-z]+'
    return re.findall(pattern, string)
#4
def find_upper_followed_by_lower(string):
    pattern = '[A-Z][a-z]*'
    return re.findall(pattern, string)
#5
def match_a_anything_b(string):
    pattern = 'a.*b$'
    if re.match(pattern, string):
        return True
    return False
#6
def replace_with_colon(string):
    return re.sub('[ ,.]', ':', string)
#7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
#8
def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)
#9
def insert_spaces(string):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", string)
#10
def camel_to_snake(camel_str):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()
