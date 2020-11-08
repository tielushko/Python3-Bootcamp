import re

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.)([A-Za-z]) ([a-z])+', re.IGNORECASE)


#1st arg - the string you want to work as a sub, and second the sting in which matches occured
print(pattern.sub("\g<2>\g<1>", text)) 


