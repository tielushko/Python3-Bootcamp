import re

url_regex = re.compile(r'(https?)://www\.?([-a-zA-Z0-9@:%._+~#=]{2,256})\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

match = url_regex.search('http://www.youtube.com/videos/asd/ds/asd')
print(match.group())
print(match.groups()) # returns a tuple of the grouped objects that are identified by parentheses

#or can do the numbering of groups
print(f'Full Link: {match.group(0)}') # the whole thing
print(f'Protocol: {match.group(1)}') # 1st group
print(f'Domain: {match.group(2)}') # 2nd group
print(f'Parameters: {match.group(3)}') # 3rd group

