__author__ = 'aganiger'

import re

data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

for d in data:
    print(re.sub("\(.*\)", "", d))

for d in data:
    print(re.sub("[\(|\| )]", "", d))

text = "The quick brown fox jumps over the lazy dog."
# remove words between 1 and 3
shortword = re.compile(r'\W*\b\w{1,3}\b')
print(shortword.sub("", text))


# Spit from capital letter
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))

# find URL in a strin
text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'

print(re.findall('http[s]://[^">]+', text))