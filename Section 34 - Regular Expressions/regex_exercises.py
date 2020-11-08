# Don't forget to import re!
import re

# Define is_valid_time below: -> using the proper time format 1-2 digits colon 2 digits
def is_valid_time(input_str):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$') #(r'^\d\d?:\d\d$')
    if time_regex.search(input_str):
        return True
    else:
        return False

# define parse_bytes below: -> identify groups of bytes of 0-1 that are size of 8
def parse_bytes(input_str):
    byte_regex = re.compile(r'\b[01]{8}\b')
    matches = byte_regex.findall(input_str)
    return matches

#define parse_date below -> parses data according to dd/mm/yyyy format
def parse_date(input_str):
    date_regex = re.compile(r'(?P<day>[0-3]{1}[0-9]{1})[/,\.](?P<month>[01]{1}[0-9]{1})[/,\.](?P<year>[0-9]{4})')
    match = date_regex.search(input_str)
    if match:
        return {'d': match.group('day'), 'm': match.group('month'), 'y': match.group('year')}
    return None

# substituting any profane words that start with frack in it and are case insensitive

def censor(input_str):
    regex = re.compile(r'\bfrack\w\b*', re.IGNORECASE)
    return regex.sub("CENSORED", input_str)