import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    matches = phone_regex.findall(input)
    return matches

def is_valid_phone(input):
    phone_regex = re.compile(r'^\b\d{3} \d{3}-\d{4}\b$')
    match = phone_regex.search(input)
    # can instead reuse the regex without ^$ but with regex.fullmatch(input)
    if match:
        return True
    return False


# print(extract_phone('my number is 813 895-6015'))
# print(extract_phone('my number is 813123 895-601315'))
# print(extract_phone('813 895-6015'))
# print(extract_phone('my number is 813 895-6015 awdwadawd'))
# print(extract_all_phones('Call me at 813 895-6015! or 812 141-1515'))
print(is_valid_phone('my number is 813 895-6015'))
print(is_valid_phone('my number is 813123 895-601315'))
print(is_valid_phone('813 895-6015'))