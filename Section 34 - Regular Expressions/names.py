import re

def parse_name(input_str):
    # ?P<name> is used to name the group matches 
    name_regex = re.compile(r'^(?P<prefix>Mr\.|Mrs\.|Madame\.|Miss\.|Ms\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input_str)
    #we can later reference that group later by its key name first or last for example
    print(matches.group('first'))


parse_name("Mrs. Tilda Swanson")