# Test under the Python Command-Line Interpreter

import re   # Need module 're' for regular expression

# Try find: re.findall(regexStr, inStr) -> matchedSubstringsList
# r'...' denotes raw strings which ignore escape code, i.e., r'\n' is '\'+'n'
print(re.findall(r'^st[a-z]*[aeiou]+[a-z]*st$', 'stast'))
re.findall(r'[0-9]+', 'abcxyz')
re.findall(r'[0-9]+', 'abc00123xyz456_0')
re.findall(r'\d+', 'abc00123xyz456_0')

# Try substitute: re.sub(regexStr, replacementStr, inStr) -> outStr
re.sub(r'[0-9]+', r'*', 'abc00123xyz456_0')

# Try substitute with count: re.subn(regexStr, replacementStr, inStr) -> (outStr, count)
re.subn(r'[0-9]+', r'*', 'abc00123xyz456_0')
   # Return a tuple of output string and count