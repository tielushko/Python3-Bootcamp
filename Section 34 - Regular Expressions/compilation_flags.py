import re

#include VERBOSE tag to ignore whitespace in the regex that allows to split it up on multiple lines and make comments
# for space, just use \ to have it included

# to include additional flags, need to use | it'll use both flags

pattern = re.compile(r"""
    ^([a-z0-9_\.-]+)    # email name
    @                   # single @
    ([0-9a-z\.-]+)      # email provider
    \.                  # single dot
    ([a-z\.]{2,6})$     # top-level domain
""", re.VERBOSE | re.IGNORECASE)

match = pattern.search('tomas123@yahoo.com')

print(match.group())
print(match.groups())
