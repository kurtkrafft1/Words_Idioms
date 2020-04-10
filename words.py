"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
word_definitions['Epstien'] = 'A human piece of garbage'
word_definitions["didn't"] = "A contraction combining 'did' and 'not'"
word_definitions["kill"] = "To end the existence of a person, place, or thing"
word_definitions["himself"] = "he or him personally"
# print(word_definitions)

keyAndValuePairs = word_definitions.items()
for duo in keyAndValuePairs:
    print(duo) 


