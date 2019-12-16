import re
import pprint
from collections import Counter

text = "Awesome, I am doing the #100DaysOfCode challenge"

# print(text.startswith("Awesome"))
# print(text.endswith("challenge"))
# print("100daysofcode" in text.lower())
# print(text.replace("100", "200"))
# print(re.search(r"I am", text)) 
# print(re.match(r"I am.*#", text)) 


hundred = "Awesome, I am doing the #100DaysOfCode challenge"
two_hundred = "Awesome, I am doing the #200DaysOfCode challenge"

match = re.match(r'.*(#\d+DaysOfCode).*', hundred)
# print(match.groups()[0])

search = re.search(r'(#\d+DaysOfCode)', two_hundred)
# print(search.groups()[0])




text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

# print(re.findall(r"\d+", text))



text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""

# pprint.pprint(re.findall(r"\w+", text))
# pprint.pprint(text.split()[:5])
# pprint.pprint(re.findall(r'[A-Z][a-z0-9]+', text))

cnt = Counter(re.findall(r'[A-Z][a-z0-9]+', text))
# pprint.pprint(cnt)
# print(cnt.most_common(5))




movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')
movies

pat = re.compile(r'''
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $             # end of string
                  ''', re.VERBOSE)

# for movie in movies:
    # print(movie) #pat.match(movie))



text = '''Awesome, I am doing #100DaysOfCode, #200DaysOfDjango and of course #365DaysOfPyBites'''

# print(text.replace("200", "100").replace("365", "100"))
# print(re.sub(r"\d+", "100", text))
print(re.sub(r"(#\d+DaysOf)\w+", r"\1Python", text))