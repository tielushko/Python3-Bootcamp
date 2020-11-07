import re

# define the phone number regex
# r is used as raw string, so that we don't have to escape characters
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a string with our regex - returns a match object
res = pattern.search('Call me at 813 895-6015!')

res.group() # extracts the match for us - but only the first location of the match - doesn't support 2 or more matches

#returns a list of all matches present
res = pattern.findall('Call me at 813 895-6015! or 812 141-1515')

# alternative search without compile method
match = re.search(r'\d{3} \d{3}-\d{4}', 'Call me at 813 895-6015!').group()
matches = re.findall(r'\d{3} \d{3}-\d{4}', 'Call me at 813 895-6015! or 812 141-1515')